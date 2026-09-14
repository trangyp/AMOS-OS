#!/usr/bin/env python3
from __future__ import annotations

import base64
import importlib.util
import json
import socket
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

MOD_PATH = Path(__file__).parents[1] / "17_OBSERVABILITY" / "trace_transport_runtime.py"
spec = importlib.util.spec_from_file_location("trace_transport_runtime", MOD_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)

OtlpHttpJsonClient = mod.OtlpHttpJsonClient
OtlpHttpJsonEncoder = mod.OtlpHttpJsonEncoder
RetryPolicy = mod.RetryPolicy
RoundTripVerifier = mod.RoundTripVerifier
TransportContractError = mod.TransportContractError
TransportQueue = mod.TransportQueue


def span(span_id="0123456789abcdef", parent=None, *, name="root", kind="AGENT", status="OK", effect="NONE"):
    return {"trace_id":"00112233445566778899aabbccddeeff","span_id":span_id,"parent_span_id":parent,"kind":kind,"name":name,"subject":"agent:alpha","subject_version":"build-1","event_time":1000.0,"observed_at":1000.1,"started_at":1000.0,"ended_at":1000.2,"status":status,"input_hash":"a"*64,"output_hash":"b"*64,"capture_mode":"METADATA_ONLY","authority_ref":None,"effect_state":effect,"provenance_root":"prov:root","environment":"test","correlation_id":"corr-1","error_type":None,"error_message":None}


class BackendState:
    status=200; body={}; headers={}; received=[]


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        n=int(self.headers.get("Content-Length","0")); body=self.rfile.read(n); BackendState.received.append((self.path,dict(self.headers.items()),body)); self.send_response(BackendState.status)
        for k,v in BackendState.headers.items(): self.send_header(k,v)
        self.send_header("Content-Type","application/json"); self.end_headers(); self.wfile.write(json.dumps(BackendState.body).encode())
    def log_message(self,fmt,*args): pass


class Server:
    def __enter__(self):
        BackendState.status=200; BackendState.body={}; BackendState.headers={}; BackendState.received=[]; self.httpd=ThreadingHTTPServer(("127.0.0.1",0),Handler); self.thread=threading.Thread(target=self.httpd.serve_forever,daemon=True); self.thread.start(); self.url=f"http://127.0.0.1:{self.httpd.server_address[1]}/v1/traces"; return self
    def __exit__(self,*exc): self.httpd.shutdown(); self.thread.join(timeout=2); self.httpd.server_close()


class Tests(unittest.TestCase):
    def test_otlp_json_encoder_uses_base64_ids_and_amos_attrs(self):
        payload=OtlpHttpJsonEncoder.encode([span()],run_id="run-1",build_id="sha-1"); otel=payload["resourceSpans"][0]["scopeSpans"][0]["spans"][0]; self.assertEqual(base64.b64decode(otel["traceId"]).hex(),span()["trace_id"]); self.assertEqual(base64.b64decode(otel["spanId"]).hex(),span()["span_id"]); attrs={x["key"]:next(iter(x["value"].values())) for x in otel["attributes"]}; self.assertEqual(attrs["amos.run.id"],"run-1"); self.assertEqual(attrs["amos.build.id"],"sha-1"); self.assertEqual(otel["kind"],1); self.assertEqual(otel["status"]["code"],1)
    def test_encoder_rejects_open_span(self):
        with self.assertRaises(TransportContractError): OtlpHttpJsonEncoder.encode([span(status="STARTED")],run_id="r",build_id="b")
    def test_queue_persists_across_reopen(self):
        with tempfile.TemporaryDirectory() as td:
            db=Path(td)/"q.db"; q=TransportQueue(db); eid=q.enqueue(trace_id=span()["trace_id"],run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); q.close(); q2=TransportQueue(db); self.assertEqual(q2.get(eid)["state"],"QUEUED"); q2.close()
    def test_http_200_ack_is_not_readback_verification(self):
        with tempfile.TemporaryDirectory() as td, Server() as srv:
            q=TransportQueue(Path(td)/"q.db"); payload=OtlpHttpJsonEncoder.encode([span()],run_id="r",build_id="b"); eid=q.enqueue(trace_id=span()["trace_id"],run_id="r",build_id="b",endpoint=srv.url,payload=payload); self.assertEqual(OtlpHttpJsonClient().send_once(q,eid),"ACKED"); self.assertEqual(q.receipt(eid)["transport_semantics"],"HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION"); self.assertEqual(BackendState.received[0][0],"/v1/traces"); q.close()
    def test_otlp_retryable_http_codes_are_bounded(self):
        with tempfile.TemporaryDirectory() as td:
            q=TransportQueue(Path(td)/"q.db")
            for code in (429,502,503,504):
                eid=q.enqueue(trace_id=f"t-{code}",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":code}); q.begin_attempt(eid,now=100.0); self.assertEqual(q.mark_response(eid,http_status=code,response_body='{}',headers={},now=100.0,retry_policy=RetryPolicy(max_attempts=2,jitter_fraction=0)),"RETRYABLE")
            eid=q.enqueue(trace_id="t-500",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":500}); q.begin_attempt(eid); self.assertEqual(q.mark_response(eid,http_status=500,response_body='{}',headers={}),"PERMANENT_FAILURE"); q.close()
    def test_http_400_is_permanent(self):
        with tempfile.TemporaryDirectory() as td, Server() as srv:
            BackendState.status=400; BackendState.body={"message":"bad data"}; q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint=srv.url,payload={"x":1}); self.assertEqual(OtlpHttpJsonClient().send_once(q,eid),"PERMANENT_FAILURE"); self.assertRaises(TransportContractError,q.begin_attempt,eid); q.close()
    def test_429_honors_retry_after(self):
        with tempfile.TemporaryDirectory() as td, Server() as srv:
            BackendState.status=429; BackendState.headers={"Retry-After":"7"}; q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint=srv.url,payload={"x":1}); self.assertEqual(OtlpHttpJsonClient().send_once(q,eid,now=100.0,retry_policy=RetryPolicy(max_attempts=3,jitter_fraction=0)),"RETRYABLE"); self.assertEqual(q.get(eid)["next_attempt_at"],107.0); self.assertRaises(TransportContractError,q.begin_attempt,eid,now=106.9); q.close()
    def test_partial_success_is_not_ack(self):
        with tempfile.TemporaryDirectory() as td, Server() as srv:
            BackendState.body={"partialSuccess":{"rejectedSpans":"2","errorMessage":"quota"}}; q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint=srv.url,payload={"x":1}); self.assertEqual(OtlpHttpJsonClient().send_once(q,eid),"PARTIAL"); self.assertEqual(q.get(eid)["partial_rejected_spans"],2); q.close()
    def test_http_200_without_valid_json_is_protocol_error(self):
        with tempfile.TemporaryDirectory() as td:
            q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); q.begin_attempt(eid); self.assertEqual(q.mark_response(eid,http_status=200,response_body=b"",headers={"Content-Type":"application/json"}),"PROTOCOL_ERROR"); self.assertRaises(TransportContractError,q.begin_attempt,eid); q.close()
    def test_invalid_header_is_rejected_before_attempt_state_changes(self):
        with tempfile.TemporaryDirectory() as td, Server() as srv:
            q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint=srv.url,payload={"x":1}); self.assertRaises(TransportContractError,OtlpHttpJsonClient().send_once,q,eid,headers={"Authorization":"Bearer good\nInjected: bad"}); self.assertEqual(q.get(eid)["state"],"QUEUED"); self.assertEqual(q.get(eid)["attempt_count"],0); q.close()
    def test_network_failure_becomes_in_doubt_and_requires_reconciliation(self):
        with tempfile.TemporaryDirectory() as td:
            s=socket.socket(); s.bind(("127.0.0.1",0)); port=s.getsockname()[1]; s.close(); q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint=f"http://127.0.0.1:{port}/v1/traces",payload={"x":1}); self.assertEqual(OtlpHttpJsonClient(timeout=.2).send_once(q,eid),"IN_DOUBT"); self.assertRaises(TransportContractError,q.begin_attempt,eid); self.assertEqual(q.reconcile_in_doubt(eid,observed_in_backend=False,evidence_ref="probe:no-span"),"QUEUED"); q.close()
    def test_in_doubt_backend_presence_reconciles_without_forging_http_ack(self):
        with tempfile.TemporaryDirectory() as td:
            q=TransportQueue(Path(td)/"q.db"); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); q.begin_attempt(eid); q.mark_network_outcome_unknown(eid,"timeout"); self.assertEqual(q.reconcile_in_doubt(eid,observed_in_backend=True,evidence_ref="readback:trace-present"),"RECONCILED_PRESENT"); self.assertRaises(TransportContractError,q.begin_attempt,eid); q.close()
    def test_restart_recovers_sending_as_in_doubt(self):
        with tempfile.TemporaryDirectory() as td:
            db=Path(td)/"q.db"; q=TransportQueue(db); eid=q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); q.begin_attempt(eid); q.close(); q2=TransportQueue(db); self.assertEqual(q2.get(eid)["state"],"IN_DOUBT"); q2.close()
    def test_roundtrip_exact_match(self):
        expected=[span(),span("1111111111111111",parent=span()["span_id"],name="child",kind="TOOL")]; observed=[]
        for e in expected: observed.append({"trace_id":e["trace_id"],"span_id":e["span_id"],"parent_span_id":e["parent_span_id"],"name":e["name"],"status":e["status"],"attributes":{"amos.span.kind":e["kind"],"amos.subject":e["subject"],"amos.provenance.root":e["provenance_root"],"amos.environment":e["environment"],"amos.effect.state":e["effect_state"],"amos.capture.mode":e["capture_mode"],"amos.run.id":"r","amos.build.id":"b"}})
        self.assertEqual(RoundTripVerifier.verify(trace_id=expected[0]["trace_id"],run_id="r",build_id="b",expected_spans=expected,observed_spans=observed)["status"],"VERIFIED_ROUNDTRIP")
    def test_roundtrip_rejects_stale_build_contamination(self):
        e=span(); observed=[{"trace_id":e["trace_id"],"span_id":e["span_id"],"parent_span_id":None,"name":e["name"],"status":"OK","attributes":{"amos.span.kind":e["kind"],"amos.subject":e["subject"],"amos.provenance.root":e["provenance_root"],"amos.environment":e["environment"],"amos.effect.state":e["effect_state"],"amos.capture.mode":e["capture_mode"],"amos.run.id":"r","amos.build.id":"old-build"}}]; result=RoundTripVerifier.verify(trace_id=e["trace_id"],run_id="r",build_id="b",expected_spans=[e],observed_spans=observed); self.assertEqual(result["status"],"NOT_VERIFIED"); self.assertTrue(result["contamination"])
    def test_roundtrip_rejects_duplicate_span_ids(self):
        e=span(); obs={"trace_id":e["trace_id"],"span_id":e["span_id"],"parent_span_id":None,"name":e["name"],"status":"OK","attributes":{"amos.span.kind":e["kind"],"amos.subject":e["subject"],"amos.provenance.root":e["provenance_root"],"amos.environment":e["environment"],"amos.effect.state":e["effect_state"],"amos.capture.mode":e["capture_mode"],"amos.run.id":"r","amos.build.id":"b"}}; result=RoundTripVerifier.verify(trace_id=e["trace_id"],run_id="r",build_id="b",expected_spans=[e],observed_spans=[obs,dict(obs)]); self.assertEqual(result["status"],"NOT_VERIFIED"); self.assertEqual(result["duplicate_span_ids"],[e["span_id"]])
    def test_phoenix_normalizer_ignores_raw_content(self):
        norm=RoundTripVerifier.normalize_phoenix([{"name":"root","context":{"trace_id":"t","span_id":"s"},"parent_id":None,"status_code":"OK","attributes":{"amos.run.id":"r","input.value":"SECRET","amos.build.id":"b"}}]); self.assertEqual(norm[0]["attributes"],{"amos.run.id":"r","amos.build.id":"b"})
    def test_transport_ledger_tamper_detected(self):
        with tempfile.TemporaryDirectory() as td:
            q=TransportQueue(Path(td)/"q.db"); q.enqueue(trace_id="t",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); q.db.execute("UPDATE transport_ledger SET event_hash='bad' WHERE seq=1"); q.db.commit(); self.assertTrue(q.verify_integrity()); q.close()
    def test_queue_capacity_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            q=TransportQueue(Path(td)/"q.db",max_active=1); q.enqueue(trace_id="t1",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":1}); self.assertRaises(TransportContractError,q.enqueue,trace_id="t2",run_id="r",build_id="b",endpoint="http://localhost:1/v1/traces",payload={"x":2}); q.close()


if __name__=="__main__": unittest.main(verbosity=2)
