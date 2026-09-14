"""Bounded ULK ALU-07 classical finite-dimensional numerical reference checker.

Origin architect / steward: Trang Phan.
Extracted as a bounded executable projection from the current `_00_AMOS_CANON` unified_brain.py source.
This artifact does not promote Canon or grant effect authority.
"""
from __future__ import annotations
from typing import Any, Dict

SOURCE_DRIVE_FILE_ID = '1oDrxdqfF-1HFxwDbW5ooSfsfYfJm05iQ'
SOURCE_REVISION_ID = '0B_FlOTCuYcaFdVpKNEFLOTNHcFM3Q01GVGx4TmpVTTBHVytrPQ'
SOURCE_FILE_SHA256 = 'c04cbe63b3a8d3b67095c17bcfb1c471ccb9841d78412aa086f44fcb35b14d8e'
SOURCE_METHOD_AST_SHA256 = '754402e1a342f4eee7d4bf6c19c155a0ff6257cab82bcaf1f1e3bedbcec98410'


class ALU07ReferenceChecker:
    @staticmethod
    def _alu07_complex_scalar(value: Any, name: str) -> complex:
        """Parse JSON-safe real/complex scalar for bounded ALU-07 math."""
        if isinstance(value, bool):
            raise ValueError(f'{name} must be numeric, not boolean')
        if isinstance(value, (int, float, complex)):
            return complex(value)
        if isinstance(value, (list, tuple)) and len(value) == 2:
            return complex(float(value[0]), float(value[1]))
        if isinstance(value, dict) and {'real', 'imag'}.issubset(value):
            return complex(float(value['real']), float(value['imag']))
        raise ValueError(f'{name} must be numeric or [real, imag]')

    @classmethod
    def _alu07_matrix(cls, value: Any, name: str):
        import numpy as np
        if not isinstance(value, list) or not value or not all(isinstance(row, list) and row for row in value):
            raise ValueError(f'{name} must be a non-empty nested list')
        width = len(value[0])
        if any(len(row) != width for row in value):
            raise ValueError(f'{name} rows must have equal length')
        return np.array([[cls._alu07_complex_scalar(cell, f'{name}[{i},{j}]') for j, cell in enumerate(row)] for i, row in enumerate(value)], dtype=complex)

    @staticmethod
    def _alu07_matrix_payload(matrix, *, max_cells: int = 64) -> Dict[str, Any]:
        import numpy as np
        rows, cols = matrix.shape
        out = {'shape': [int(rows), int(cols)], 'truncated': bool(rows * cols > max_cells)}
        if rows * cols <= max_cells:
            if float(np.max(np.abs(matrix.imag))) < 1e-12:
                out['data'] = [[float(np.real(x)) for x in row] for row in matrix]
            else:
                out['data'] = [[[float(np.real(x)), float(np.imag(x))] for x in row] for row in matrix]
        return out

    @staticmethod
    def _alu07_real(x: Any, tol: float = 1e-9) -> float:
        import numpy as np
        z = complex(x)
        if abs(z.imag) > tol:
            raise ValueError('expected real scalar within tolerance')
        return float(np.real(z))

    @staticmethod
    def _alu07_adjoint(matrix):
        return matrix.conj().T

    @classmethod
    def _alu07_check_square(cls, matrix, name: str) -> int:
        if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
            raise ValueError(f'{name} must be a square matrix')
        return int(matrix.shape[0])

    @classmethod
    def _alu07_check_dim(cls, matrix, name: str, max_dim: int) -> int:
        n = cls._alu07_check_square(matrix, name)
        if n > max_dim:
            raise ValueError(f'{name} dimension {n} exceeds bounded max_dim {max_dim}')
        return n

    @classmethod
    def _alu07_check_hermitian(cls, matrix, name: str, tol: float) -> None:
        import numpy as np
        if not np.allclose(matrix, cls._alu07_adjoint(matrix), atol=tol):
            raise ValueError(f'{name} must be Hermitian within tolerance')

    @classmethod
    def _alu07_check_psd(cls, matrix, name: str, tol: float) -> None:
        import numpy as np
        vals = np.linalg.eigvalsh((matrix + cls._alu07_adjoint(matrix)) / 2)
        if float(vals.min()) < -tol:
            raise ValueError(f'{name} must be positive semidefinite within tolerance')

    @classmethod
    def _alu07_check_density(cls, rho, name: str, tol: float, max_dim: int) -> int:
        import numpy as np
        n = cls._alu07_check_dim(rho, name, max_dim)
        cls._alu07_check_hermitian(rho, name, tol)
        tr = np.trace(rho)
        if abs(tr - 1.0) > tol:
            raise ValueError(f'{name} trace must equal 1 within tolerance')
        cls._alu07_check_psd(rho, name, tol)
        return n

    @classmethod
    def _alu07_check_projector(cls, p, name: str, tol: float, max_dim: int) -> int:
        import numpy as np
        n = cls._alu07_check_dim(p, name, max_dim)
        cls._alu07_check_hermitian(p, name, tol)
        if not np.allclose(p @ p, p, atol=tol):
            raise ValueError(f'{name} must be idempotent projector within tolerance')
        return n

    @classmethod
    def _alu07_kraus_list(cls, value: Any, name: str):
        if not isinstance(value, list) or not value:
            raise ValueError(f'{name} must be a non-empty list of matrices')
        return [cls._alu07_matrix(item, f'{name}[{idx}]') for idx, item in enumerate(value)]

    @classmethod
    def _alu07_check_same_square(cls, matrices, name: str, tol: float, max_dim: int) -> int:
        n = None
        for idx, m in enumerate(matrices):
            dim = cls._alu07_check_dim(m, f'{name}[{idx}]', max_dim)
            if n is None:
                n = dim
            elif dim != n:
                raise ValueError(f'{name} matrices must have the same square dimension')
        return int(n)

    @classmethod
    def _alu07_check_kraus_tp(cls, kraus, name: str, tol: float, max_dim: int) -> int:
        import numpy as np
        n = cls._alu07_check_same_square(kraus, name, tol, max_dim)
        total = sum(cls._alu07_adjoint(k) @ k for k in kraus)
        if not np.allclose(total, np.eye(n), atol=tol):
            raise ValueError(f'{name} must satisfy sum K^dagger K = I within tolerance')
        return n

    @classmethod
    def _alu07_vn_entropy(cls, rho, base: float, tol: float) -> float:
        import math
        import numpy as np
        cls._alu07_check_hermitian(rho, 'rho', tol)
        vals = np.linalg.eigvalsh((rho + cls._alu07_adjoint(rho)) / 2)
        vals = np.clip(vals.real, 0.0, None)
        vals = vals[vals > tol]
        if len(vals) == 0:
            return 0.0
        return float(-sum(float(v) * math.log(float(v), base) for v in vals))

    @classmethod
    def _alu07_matrix_log_psd(cls, matrix, tol: float):
        import numpy as np
        cls._alu07_check_hermitian(matrix, 'matrix', tol)
        vals, vecs = np.linalg.eigh((matrix + cls._alu07_adjoint(matrix)) / 2)
        if float(vals.min()) < -tol:
            raise ValueError('matrix log requires PSD input')
        log_vals = [0.0 if v <= tol else float(np.log(v)) for v in vals.real]
        return vecs @ np.diag(log_vals) @ cls._alu07_adjoint(vecs)

    @classmethod
    def _alu07_partial_trace_bipartite(cls, rho, dims, trace_out: int):
        import numpy as np
        d_a, d_b = int(dims[0]), int(dims[1])
        if rho.shape != (d_a * d_b, d_a * d_b):
            raise ValueError('rho shape does not match bipartite dims')
        reshaped = rho.reshape(d_a, d_b, d_a, d_b)
        if trace_out == 1:
            return np.trace(reshaped, axis1=1, axis2=3)
        if trace_out == 0:
            return np.trace(reshaped, axis1=0, axis2=2)
        raise ValueError('trace_out must be 0 or 1')

    @classmethod
    def _alu07_partial_transpose_bipartite(cls, rho, dims, target: int):
        d_a, d_b = int(dims[0]), int(dims[1])
        if rho.shape != (d_a * d_b, d_a * d_b):
            raise ValueError('rho shape does not match bipartite dims')
        reshaped = rho.reshape(d_a, d_b, d_a, d_b)
        if target == 0:
            return reshaped.transpose(2, 1, 0, 3).reshape(d_a * d_b, d_a * d_b)
        if target == 1:
            return reshaped.transpose(0, 3, 2, 1).reshape(d_a * d_b, d_a * d_b)
        raise ValueError('target must be 0 or 1')

    @classmethod
    def _alu07_success(cls, operator: str, profile: str, payload: Dict[str, Any], *, tol: float, max_dim: int) -> Dict[str, Any]:
        out = {
            'success': True,
            'status': 'PASS_BOUNDED_ALU07_REFERENCE_CHECKER',
            'operator': operator,
            'candidate_profile': profile,
            'operator_executable': True,
            'runtime_callable_bound': True,
            'finite_dimensional_checker_bound': True,
            'implementation_status': 'BOUNDED_CLASSICAL_FINITE_DIMENSIONAL_REFERENCE_CHECKER',
            'hardware_backend': 'NONE_CLASSICAL_NUMERIC',
            'quantum_advantage': 'NOT_ESTABLISHED',
            'physical_quantum_state': False,
            'tolerance': tol,
            'max_dim': max_dim,
            'epistemic_class': 'EXECUTED_NUMERICAL_RESULT',
            'conclusion_class': 'BOUNDED_EXECUTABLE_EVIDENCE',
            'authority_granted': False,
            'effect_authorized': False,
            'method': 'ulk_alu07_operator_gate',
            'boundary': 'BOUNDED_NUMERICAL_REFERENCE_CHECKER != QUANTUM_HARDWARE; BOUNDED_OPERATOR_PASS != UNIVERSAL_ULK_ALU07_COMPLETION',
        }
        out.update(payload)
        return out

    def ulk_alu07_operator_gate(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Bounded classical finite-dimensional checker for selected ULK ALU-07 operators."""
        import numpy as np
        from scipy.linalg import expm
        candidate_profiles = {
            'QCHANNEL': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QPOVM': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QENTROPY': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QRELENT': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QMUTUALINFO': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QHAMILTONIAN': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V2',
            'QINSTRUMENT': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QAPPLYINSTRUMENT': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QCHANNELCOMPOSE': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QTRACEDIST': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QFIDELITY': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QPARTIALTRANSPOSE': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QNEGATIVITY': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'QLINDBLAD': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V3',
            'PROJECTOR_COMPLEMENT': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
            'PROJECTOR_MEET': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
            'PROJECTOR_JOIN': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
            'BORN_PROBABILITY': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
            'LUDERS_UPDATE': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
            'PARTIAL_TRACE': 'ULK_ALU07_QUANTUM_LOGIC_EXECUTABLE_PROFILE_V1',
        }

        def fail(status: str, reason: str, *, operator: str = None, detail: str = None) -> Dict[str, Any]:
            out = {
                'success': False,
                'status': status,
                'reason': reason,
                'capability_bound': True,
                'operator_executable': False,
                'runtime_callable_bound': False,
                'finite_dimensional_checker_bound': False,
                'hardware_backend': 'NOT_ESTABLISHED',
                'quantum_advantage': 'NOT_ESTABLISHED',
                'physical_quantum_state': False,
                'epistemic_class': 'UNKNOWN/GAP',
                'authority_granted': False,
                'effect_authorized': False,
                'method': 'ulk_alu07_operator_gate',
            }
            if operator is not None:
                out['operator'] = operator
            if detail is not None:
                out['detail'] = detail
            return out

        if not isinstance(params, dict):
            return fail('ILL_TYPED', 'params must be a dict')
        raw_operator = params.get('operator') or params.get('op')
        if not isinstance(raw_operator, str) or not raw_operator.strip():
            return fail('HOLD_UNKNOWN', 'missing_operator_identity')
        operator = raw_operator.strip().upper()
        if operator not in candidate_profiles:
            return fail('REJECT_UNKNOWN_OPERATOR', 'operator_not_defined_in_bound_candidate_profiles', operator=operator)
        tol = float(params.get('tolerance', params.get('tol', 1e-8)))
        if tol <= 0 or tol > 1e-2:
            return fail('ILL_TYPED', 'tolerance must be in (0, 1e-2]', operator=operator)
        max_dim = int(params.get('max_dim', 8))
        if max_dim < 1 or max_dim > 16:
            return fail('ILL_TYPED', 'max_dim must be between 1 and 16', operator=operator)
        profile = candidate_profiles[operator]

        try:
            I = None
            if operator in {'QCHANNEL', 'QPOVM', 'QENTROPY', 'QRELENT', 'QMUTUALINFO', 'QHAMILTONIAN', 'QAPPLYINSTRUMENT', 'QTRACEDIST', 'QFIDELITY', 'QPARTIALTRANSPOSE', 'QNEGATIVITY', 'QLINDBLAD', 'BORN_PROBABILITY', 'LUDERS_UPDATE', 'PARTIAL_TRACE'}:
                rho = self._alu07_matrix(params.get('rho'), 'rho')
                n = self._alu07_check_density(rho, 'rho', tol, max_dim)
                I = np.eye(n)

            if operator == 'QCHANNEL':
                kraus = self._alu07_kraus_list(params.get('kraus') or params.get('K'), 'kraus')
                kdim = self._alu07_check_kraus_tp(kraus, 'kraus', tol, max_dim)
                if kdim != n:
                    raise ValueError('kraus dimension must match rho')
                out_rho = sum(k @ rho @ self._alu07_adjoint(k) for k in kraus)
                self._alu07_check_density(out_rho, 'channel_output', tol * 10, max_dim)
                return self._alu07_success(operator, profile, {'trace_preserving': True, 'output_density_valid': True, 'output': self._alu07_matrix_payload(out_rho)}, tol=tol, max_dim=max_dim)

            if operator == 'QPOVM':
                effects = self._alu07_kraus_list(params.get('effects') or params.get('E'), 'effects')
                edim = self._alu07_check_same_square(effects, 'effects', tol, max_dim)
                if edim != n:
                    raise ValueError('effect dimension must match rho')
                for idx, e in enumerate(effects):
                    self._alu07_check_hermitian(e, f'effects[{idx}]', tol)
                    self._alu07_check_psd(e, f'effects[{idx}]', tol)
                if not np.allclose(sum(effects), I, atol=tol):
                    raise ValueError('POVM effects must sum to identity')
                probs = [self._alu07_real(np.trace(rho @ e), tol * 10) for e in effects]
                return self._alu07_success(operator, profile, {'probabilities': probs, 'probability_sum': float(sum(probs)), 'povm_valid': abs(sum(probs) - 1.0) <= tol * 10}, tol=tol, max_dim=max_dim)

            if operator == 'QENTROPY':
                base = float(params.get('base', 2.0))
                return self._alu07_success(operator, profile, {'entropy': self._alu07_vn_entropy(rho, base, tol), 'base': base}, tol=tol, max_dim=max_dim)

            if operator == 'QRELENT':
                sigma = self._alu07_matrix(params.get('sigma'), 'sigma')
                self._alu07_check_density(sigma, 'sigma', tol, max_dim)
                vals, vecs = np.linalg.eigh((sigma + self._alu07_adjoint(sigma)) / 2)
                null_projector = vecs[:, vals.real <= tol] @ self._alu07_adjoint(vecs[:, vals.real <= tol]) if any(vals.real <= tol) else np.zeros_like(sigma)
                null_mass = self._alu07_real(np.trace(null_projector @ rho), tol * 10)
                if null_mass > tol:
                    rel = float('inf')
                else:
                    log_rho = self._alu07_matrix_log_psd(rho, tol)
                    log_sigma = self._alu07_matrix_log_psd(sigma, tol)
                    rel = self._alu07_real(np.trace(rho @ (log_rho - log_sigma)), tol * 100)
                return self._alu07_success(operator, profile, {'relative_entropy_nats': rel}, tol=tol, max_dim=max_dim)

            if operator == 'QMUTUALINFO':
                dims = params.get('dims')
                if not (isinstance(dims, list) and len(dims) == 2):
                    raise ValueError('dims must be [dA, dB]')
                rho_a = self._alu07_partial_trace_bipartite(rho, dims, trace_out=1)
                rho_b = self._alu07_partial_trace_bipartite(rho, dims, trace_out=0)
                base = float(params.get('base', 2.0))
                mi = self._alu07_vn_entropy(rho_a, base, tol) + self._alu07_vn_entropy(rho_b, base, tol) - self._alu07_vn_entropy(rho, base, tol)
                return self._alu07_success(operator, profile, {'mutual_information': float(mi), 'base': base}, tol=tol, max_dim=max_dim)

            if operator == 'QHAMILTONIAN':
                H = self._alu07_matrix(params.get('H') or params.get('hamiltonian'), 'H')
                self._alu07_check_dim(H, 'H', max_dim)
                if H.shape != rho.shape:
                    raise ValueError('H dimension must match rho')
                self._alu07_check_hermitian(H, 'H', tol)
                t = float(params.get('t', 0.0))
                U = expm(-1j * H * t)
                out_rho = U @ rho @ self._alu07_adjoint(U)
                self._alu07_check_density(out_rho, 'rho_t', tol * 100, max_dim)
                return self._alu07_success(operator, profile, {'unitary_valid': bool(np.allclose(self._alu07_adjoint(U) @ U, I, atol=tol * 100)), 't': t, 'output': self._alu07_matrix_payload(out_rho)}, tol=tol, max_dim=max_dim)

            if operator == 'QINSTRUMENT':
                instrument = params.get('instrument') or params.get('kraus_by_outcome')
                if not isinstance(instrument, list) or not instrument:
                    raise ValueError('instrument must be a non-empty list of outcome Kraus lists')
                all_k = []
                for idx, outcome in enumerate(instrument):
                    ks = self._alu07_kraus_list(outcome, f'instrument[{idx}]')
                    all_k.extend(ks)
                dim = self._alu07_check_kraus_tp(all_k, 'instrument', tol, max_dim)
                return self._alu07_success(operator, profile, {'instrument_complete': True, 'dimension': dim, 'outcome_count': len(instrument), 'kraus_count': len(all_k)}, tol=tol, max_dim=max_dim)

            if operator == 'QAPPLYINSTRUMENT':
                instrument = params.get('instrument') or params.get('kraus_by_outcome')
                if not isinstance(instrument, list) or not instrument:
                    raise ValueError('instrument must be a non-empty list of outcome Kraus lists')
                outcome_states = []
                probs = []
                all_k = []
                for idx, outcome in enumerate(instrument):
                    ks = self._alu07_kraus_list(outcome, f'instrument[{idx}]')
                    all_k.extend(ks)
                    unnorm = sum(k @ rho @ self._alu07_adjoint(k) for k in ks)
                    p_i = max(0.0, self._alu07_real(np.trace(unnorm), tol * 100))
                    probs.append(p_i)
                    outcome_states.append(unnorm / p_i if p_i > tol else None)
                self._alu07_check_kraus_tp(all_k, 'instrument', tol, max_dim)
                selected = params.get('outcome')
                payload = {'probabilities': probs, 'probability_sum': float(sum(probs))}
                if selected is not None:
                    idx = int(selected)
                    if idx < 0 or idx >= len(outcome_states):
                        raise ValueError('outcome index out of range')
                    if outcome_states[idx] is None:
                        payload['selected_outcome_state'] = None
                        payload['selected_outcome_status'] = 'ZERO_PROBABILITY'
                    else:
                        self._alu07_check_density(outcome_states[idx], 'selected_outcome_state', tol * 100, max_dim)
                        payload['selected_outcome_state'] = self._alu07_matrix_payload(outcome_states[idx])
                return self._alu07_success(operator, profile, payload, tol=tol, max_dim=max_dim)

            if operator == 'QCHANNELCOMPOSE':
                k1 = self._alu07_kraus_list(params.get('kraus1') or params.get('E1'), 'kraus1')
                k2 = self._alu07_kraus_list(params.get('kraus2') or params.get('E2'), 'kraus2')
                n1 = self._alu07_check_kraus_tp(k1, 'kraus1', tol, max_dim)
                n2 = self._alu07_check_kraus_tp(k2, 'kraus2', tol, max_dim)
                if n1 != n2:
                    raise ValueError('channel dimensions must match')
                composed = [a @ b for a in k1 for b in k2]
                self._alu07_check_kraus_tp(composed, 'composed', tol * 100, max_dim)
                return self._alu07_success(operator, profile, {'composition_order': 'E1_after_E2', 'kraus_count': len(composed), 'trace_preserving': True}, tol=tol, max_dim=max_dim)

            if operator == 'QTRACEDIST':
                sigma = self._alu07_matrix(params.get('sigma'), 'sigma')
                self._alu07_check_density(sigma, 'sigma', tol, max_dim)
                vals = np.linalg.svd(rho - sigma, compute_uv=False)
                dist = 0.5 * float(np.sum(vals))
                return self._alu07_success(operator, profile, {'trace_distance': dist, 'within_unit_interval': bool(-tol <= dist <= 1.0 + tol)}, tol=tol, max_dim=max_dim)

            if operator == 'QFIDELITY':
                sigma = self._alu07_matrix(params.get('sigma'), 'sigma')
                self._alu07_check_density(sigma, 'sigma', tol, max_dim)

                def sqrt_psd(m):
                    vals, vecs = np.linalg.eigh((m + self._alu07_adjoint(m)) / 2)
                    if float(vals.min()) < -tol:
                        raise ValueError('fidelity requires PSD inputs')
                    vals = np.clip(vals.real, 0.0, None)
                    return vecs @ np.diag(np.sqrt(vals)) @ self._alu07_adjoint(vecs)

                sr = sqrt_psd(rho)
                inner = sr @ sigma @ sr
                f = float(np.real(np.trace(sqrt_psd(inner)))) ** 2
                f = max(0.0, min(1.0, f))
                return self._alu07_success(operator, profile, {'fidelity_squared_uhlmann': f, 'within_unit_interval': True}, tol=tol, max_dim=max_dim)

            if operator == 'QPARTIALTRANSPOSE':
                dims = params.get('dims')
                target = int(params.get('target', 1))
                if not (isinstance(dims, list) and len(dims) == 2):
                    raise ValueError('dims must be [dA, dB]')
                pt = self._alu07_partial_transpose_bipartite(rho, dims, target)
                return self._alu07_success(operator, profile, {'target': target, 'output': self._alu07_matrix_payload(pt)}, tol=tol, max_dim=max_dim)

            if operator == 'QNEGATIVITY':
                dims = params.get('dims')
                target = int(params.get('target', 1))
                if not (isinstance(dims, list) and len(dims) == 2):
                    raise ValueError('dims must be [dA, dB]')
                pt = self._alu07_partial_transpose_bipartite(rho, dims, target)
                eig = np.linalg.eigvalsh((pt + self._alu07_adjoint(pt)) / 2)
                negativity = float(sum(abs(v) for v in eig.real if v < -tol))
                return self._alu07_success(operator, profile, {'negativity': negativity, 'entanglement_witness_for_selected_bipartite_state': bool(negativity > tol)}, tol=tol, max_dim=max_dim)

            if operator == 'QLINDBLAD':
                H = self._alu07_matrix(params.get('H') or params.get('hamiltonian'), 'H')
                self._alu07_check_dim(H, 'H', max_dim)
                if H.shape != rho.shape:
                    raise ValueError('H dimension must match rho')
                self._alu07_check_hermitian(H, 'H', tol)
                Ls = self._alu07_kraus_list(params.get('L') or params.get('lindblad_ops') or [], 'lindblad_ops') if params.get('L') or params.get('lindblad_ops') else []
                drho = -1j * (H @ rho - rho @ H)
                for L in Ls:
                    if L.shape != rho.shape:
                        raise ValueError('each Lindblad operator dimension must match rho')
                    LdL = self._alu07_adjoint(L) @ L
                    drho = drho + L @ rho @ self._alu07_adjoint(L) - 0.5 * (LdL @ rho + rho @ LdL)
                return self._alu07_success(operator, profile, {'generator_only': True, 'lindblad_operator_count': len(Ls), 'drho_dt': self._alu07_matrix_payload(drho)}, tol=tol, max_dim=max_dim)

            if operator in {'PROJECTOR_COMPLEMENT', 'PROJECTOR_MEET', 'PROJECTOR_JOIN', 'BORN_PROBABILITY', 'LUDERS_UPDATE'}:
                P = self._alu07_matrix(params.get('P') or params.get('projector'), 'P')
                pdim = self._alu07_check_projector(P, 'P', tol, max_dim)
                if operator == 'PROJECTOR_COMPLEMENT':
                    comp = np.eye(pdim) - P
                    self._alu07_check_projector(comp, 'I_minus_P', tol * 10, max_dim)
                    return self._alu07_success(operator, profile, {'output': self._alu07_matrix_payload(comp)}, tol=tol, max_dim=max_dim)
                if operator in {'PROJECTOR_MEET', 'PROJECTOR_JOIN'}:
                    Q = self._alu07_matrix(params.get('Q') or params.get('projector_b'), 'Q')
                    qdim = self._alu07_check_projector(Q, 'Q', tol, max_dim)
                    if qdim != pdim:
                        raise ValueError('projectors must have same dimension')
                    if not np.allclose(P @ Q, Q @ P, atol=tol):
                        return fail('HOLD_UNSUPPORTED_NONCOMMUTING_PROJECTORS', 'meet/join implemented only for commuting projectors', operator=operator)
                    outp = P @ Q if operator == 'PROJECTOR_MEET' else P + Q - P @ Q
                    self._alu07_check_projector(outp, 'projector_output', tol * 100, max_dim)
                    return self._alu07_success(operator, profile, {'commuting_projectors': True, 'output': self._alu07_matrix_payload(outp)}, tol=tol, max_dim=max_dim)
                if pdim != n:
                    raise ValueError('projector dimension must match rho')
                prob = self._alu07_real(np.trace(rho @ P), tol * 10)
                if operator == 'BORN_PROBABILITY':
                    return self._alu07_success(operator, profile, {'probability': prob, 'within_unit_interval': bool(-tol <= prob <= 1.0 + tol)}, tol=tol, max_dim=max_dim)
                if prob <= tol:
                    return fail('HOLD_ZERO_PROBABILITY_EVENT', 'Luders update undefined for zero-probability event', operator=operator)
                out_rho = P @ rho @ P / prob
                self._alu07_check_density(out_rho, 'luders_output', tol * 100, max_dim)
                return self._alu07_success(operator, profile, {'probability': prob, 'output': self._alu07_matrix_payload(out_rho)}, tol=tol, max_dim=max_dim)

            if operator == 'PARTIAL_TRACE':
                dims = params.get('dims')
                trace_out = int(params.get('trace_out', params.get('target', 1)))
                if not (isinstance(dims, list) and len(dims) == 2):
                    raise ValueError('dims must be [dA, dB]')
                out_rho = self._alu07_partial_trace_bipartite(rho, dims, trace_out)
                self._alu07_check_density(out_rho, 'partial_trace_output', tol * 100, max_dim)
                return self._alu07_success(operator, profile, {'trace_out': trace_out, 'output': self._alu07_matrix_payload(out_rho)}, tol=tol, max_dim=max_dim)

            return fail('HOLD_UNKNOWN', 'operator dispatch missing', operator=operator)
        except Exception as exc:
            return fail('REJECT_OR_REPAIR', 'bounded_ALU07_validation_failed', operator=operator, detail=str(exc))

    def process_quantum_request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        gate = self.ulk_alu07_operator_gate(params)
        gate['method'] = 'process_quantum_request'
        gate['delegated_gate'] = 'ulk_alu07_operator_gate'
        return gate
