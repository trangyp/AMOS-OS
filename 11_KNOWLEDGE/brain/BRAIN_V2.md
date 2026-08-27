---
tags: [brain]
---
"""LEGACY: AMOSBrainV2 wrapper.

Canonical brain behaviour now flows through the OMEGA brain kernel
(``amos_system.kernels.omega_brain``) and ``AmosRuntime``. This module is
retained for historical reference and migration only.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional

from .cognition import Cognition
from .memory import MemoryStore
from .motor_cortex import MotorCortex
from .perception import Perception


class AMOSBrainV2:
    """High-level brain wrapper that ties together legacy subsystems.

      A) MotorCortex  -> actions
      B) Perception   -> world/sector mapping
      C) Cognition    -> frameworks, laws, planning
      D) MemoryStore  -> episodic/semantic/procedural traces
    """

    def __init__(self, repo_root: Optional[Path] = None, dry_run: bool = True) -> None:
        self.repo_root = repo_root or Path(__file__).resolve().parents[2]
        self.dry_run = dry_run

        self.motor = MotorCortex(dry_run=dry_run)
        self.perception = Perception(self.repo_root)
        self.cognition = Cognition(self.repo_root)
        self.memory = MemoryStore(self.repo_root)

    def run_once(self, task: Dict[str, Any]) -> Dict[str, Any]:
        world = self.perception.world_state()
        plan = self.cognition.reason(task)

        allow_execution = bool(task.get("allow_execution")) and not self.dry_run

        engine_name = task.get("engine") or "AMOS_META_ENGINE"
        payload = {
            "task": task,
            "plan": plan,
            "world_snapshot": {
                "has_reports": bool(world.get("reports")),
                "log_count": len(world.get("logs", [])),
                "data_file_count": len(world.get("data_files", [])),
            },
        }

        motor_result = self.motor.run_engine(
            engine_name=engine_name,
            payload=payload,
            allow_execution=allow_execution,
        )

        self.memory.save(
            kind="episodic",
            payload={
                "task": task,
                "plan": plan,
                "motor_result": motor_result,
            },
            task=task,
        )

        return {
            "task": task,
            "plan": plan,
            "motor_result": motor_result,
            "world_snapshot": payload["world_snapshot"],
            "dry_run": self.dry_run,
        }


def smoketest() -> Dict[str, Any]:
    brain = AMOSBrainV2(dry_run=True)
    task: Dict[str, Any] = {
        "type": "diagnostic",
        "description": "AMOSBrainV2 smoketest",
        "priority": "normal",
        "domains": ["meta", "system_health"],
        "allow_execution": False,
    }
    return brain.run_once(task)


if __name__ == "__main__":
    out = smoketest()
    print(json.dumps(out, indent=2, ensure_ascii=False))

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
