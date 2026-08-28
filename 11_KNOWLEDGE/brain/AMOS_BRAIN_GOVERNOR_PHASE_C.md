---
title: AMOS BRAIN GOVERNOR PHASE C
tags: [brain, cognitive, neural, canon/knowledge]
type: document
source: 11_KNOWLEDGE/brain
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: cognitive_architecture
---


# amos_brain_governor_phase_c

```python
#!/usr/bin/env python3
"""
AMOS Brain Omega Ultimate Git Safety + Performance + Coherence Governor
Phase C: Import Guard + Duplicate Kernel/Core Detector - Enhanced with Strongest AMOS Brain
"""

import ast
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any
from dataclasses import dataclass
from datetime import datetime
import logging
from collections import defaultdict

# Import strongest AMOS Brain Omega Ultimate
sys.path.insert(0, str(Path(__file__).parent / "01_BRAIN"))
try:
    from amos_brain_omega_ultimate_2025 import AMOSBrainOmegaUltimate
except ImportError:
    logging.warning("Could not import AMOS Brain Omega Ultimate - using fallback")
    AMOSBrainOmegaUltimate = None

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class ImportViolation:
    """Import rule violation"""
    file_path: str
    line: int
    import_module: str
    import_name: str
    violation_type: str
    severity: str
    description: str

@dataclass
class DuplicateKernel:
    """Duplicate kernel detection"""
    kernel_name: str
    files: List[str]
    confidence: float
    similarity_score: float

@dataclass
class DuplicateCore:
    """Duplicate core detection"""
    core_name: str
    files: List[str]
    confidence: float
    similarity_score: float

class ImportGuard:
    """Import Guard with AMOS Brain enhancement - enforces canonical kernel/core usage"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        # AMOS Brain integration
        self.amos_brain = None
        if AMOSBrainOmegaUltimate:
            try:
                self.amos_brain = AMOSBrainOmegaUltimate(repo_root)
                logger.info("🧠 ImportGuard enhanced with AMOS Brain Omega Ultimate")
            except Exception as e:
                logger.warning(f"Could not initialize AMOS Brain for ImportGuard: {e}")
        
        # Canonical kernel/core definitions
        self.canonical_kernels = {
            'governance': ['01_BRAIN/amos_brain_main.py', '01_BRAIN/amos_brain_omega_ultimate_2025.py'],
            'incentive': ['04_BLOOD/circulation/incentive_flow.py'],
            'enforcement': ['03_IMMUNE/03_IMMUNE_module.py'],
            'information': ['02_SENSES/brain_main.py'],
            'recourse': ['11_LEGAL_BRAIN/main.py'],
            'audit': ['03_IMMUNE/audit/'],
            'evolution': ['07_METABOLISM/adaptive_optimization_max_power.py'],
            'drift': ['08_WORLD_MODEL/civilizational_dynamics/'],
            'collapse': ['12_QUANTUM_LAYER/12_QUANTUM_LAYER_module.py'],
            'output_scan': ['14_INTERFACES/14_INTERFACES_module.py'],
            'logging': ['amos_brain_governor.py']
        }
        
        self.canonical_cores = {
            'tensor_field': ['01_BRAIN/amos_brain_omega_ultimate_2025.py'],
            'agent_model': ['01_BRAIN/amos_brain_omega_ultimate_2025.py'],
            'risk_scoring': ['amos_brain_governor.py'],
            'structural_invariants': ['01_BRAIN/amos_brain_omega_ultimate_2025.py'],
            'exploitation_modeling': ['01_BRAIN/amos_brain_omega_ultimate_2025.py']
        }
        
        # Import rules
        self.import_rules = {
            'forbidden_modules': [
                'os.system', 'subprocess.call', 'eval', 'exec',
                'pickle.loads', 'marshal.loads', '__import__'
            ],
            'restricted_apis': [
                'open(', 'write(', 'mkdir(', 'rmdir(', 'unlink(',
                'subprocess.', 'os.system', 'os.popen'
            ],
            'required_kernels': ['governance', 'information', 'logging'],
            'allowed_external': [
                'logging', 'json', 'pathlib', 'datetime', 'hashlib',
                'typing', 'dataclasses', 'collections', 'time', 'ast'
            ]
        }
        
        logger.info(f"🛡️ ImportGuard initialized - Session: {self.session_id}")
    
    def check_import_violations(self, file_path: Path) -> List[ImportViolation]:
        """Check file for import violations"""
        violations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        violation = self._check_import_node(alias.name, file_path, node.lineno)
                        if violation:
                            violations.append(violation)
                
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        full_import = f"{module}.{alias.name}" if module else alias.name
                        violation = self._check_import_node(full_import, file_path, node.lineno)
                        if violation:
                            violations.append(violation)
        
        except Exception as e:
            logger.warning(f"Could not check imports in {file_path}: {e}")
        
        return violations
    
    def _check_import_node(self, import_name: str, file_path: Path, line: int) -> Optional[ImportViolation]:
        """Check individual import for violations"""
        import_name_lower = import_name.lower()
        
        # Check forbidden modules
        for forbidden in self.import_rules['forbidden_modules']:
            if forbidden in import_name_lower:
                return ImportViolation(
                    file_path=str(file_path),
                    line=line,
                    import_module=import_name,
                    import_name=import_name,
                    violation_type="FORBIDDEN_MODULE",
                    severity="CRITICAL",
                    description=f"Import of forbidden module: {import_name}"
                )
        
        # Check for non-canonical kernel imports
        for kernel_type, canonical_files in self.canonical_kernels.items():
            if kernel_type in import_name_lower:
                rel_path = str(file_path.relative_to(self.repo_root))
                if not any(cf in rel_path for cf in canonical_files):
                    return ImportViolation(
                        file_path=str(file_path),
                        line=line,
                        import_module=import_name,
                        import_name=import_name,
                        violation_type="NON_CANONICAL_KERNEL",
                        severity="HIGH",
                        description=f"Non-canonical kernel import: {import_name}. Use: {canonical_files}"
                    )
        
        return None
    
    def check_write_api_usage(self, file_path: Path) -> List[ImportViolation]:
        """Check for unrestricted write API usage"""
        violations = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines, 1):
                line_lower = line.lower()
                
                for restricted in self.import_rules['restricted_apis']:
                    if restricted in line_lower and not line.strip().startswith('#'):
                        violations.append(ImportViolation(
                            file_path=str(file_path),
                            line=i,
                            import_module="WRITE_API",
                            import_name=restricted,
                            violation_type="UNRESTRICTED_WRITE_API",
                            severity="HIGH",
                            description=f"Unrestricted write API usage: {restricted}"
                        ))
        
        except Exception as e:
            logger.warning(f"Could not check write APIs in {file_path}: {e}")
        
        return violations

class DuplicateDetector:
    """Duplicate Kernel/Core Detector with AMOS Brain enhancement"""
    
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        # AMOS Brain integration
        self.amos_brain = None
        if AMOSBrainOmegaUltimate:
            try:
                self.amos_brain = AMOSBrainOmegaUltimate(repo_root)
                logger.info("🧠 DuplicateDetector enhanced with AMOS Brain Omega Ultimate")
            except Exception as e:
                logger.warning(f"Could not initialize AMOS Brain for DuplicateDetector: {e}")
        
        # Kernel/Core patterns
        self.kernel_patterns = {
            'governance': ['govern', 'policy', 'rule', 'compliance'],
            'incentive': ['incentive', 'reward', 'motivation'],
            'enforcement': ['enforce', 'audit', 'monitor'],
            'information': ['info', 'data', 'knowledge'],
            'recourse': ['recourse', 'appeal', 'remedy'],
            'audit': ['audit', 'check', 'verify'],
            'evolution': ['evol', 'adapt', 'learn'],
            'drift': ['drift', 'deviation', 'change'],
            'collapse': ['collaps', 'risk', 'fragile'],
            'output_scan': ['scan', 'output', 'result'],
            'logging': ['log', 'trace', 'audit']
        }
        
        self.core_patterns = {
            'tensor_field': ['tensor', 'field', 'multi_scale'],
            'agent_model': ['agent', 'actor', 'entity'],
            'risk_scoring': ['risk', 'score', 'assess'],
            'structural_invariants': ['invariant', 'structure', 'stable'],
            'exploitation_modeling': ['exploit', 'ambiguity', 'asymmetry']
        }
        
        logger.info(f"🔍 DuplicateDetector initialized - Session: {self.session_id}")
    
    def extract_symbols(self, file_path: Path) -> Dict[str, Any]:
        """Extract symbols from file for similarity analysis"""
        symbols = {
            'classes': [],
            'functions': [],
            'variables': [],
            'imports': [],
            'content_hash': ''
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            symbols['content_hash'] = hashlib.sha256(content.encode()).hexdigest()
            
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    symbols['classes'].append(node.name)
                elif isinstance(node, ast.FunctionDef):
                    symbols['functions'].append(node.name)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        symbols['imports'].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        symbols['imports'].append(f"{module}.{alias.name}")
        
        except Exception as e:
            logger.warning(f"Could not extract symbols from {file_path}: {e}")
        
        return symbols
    
    def compute_similarity(self, symbols1: Dict[str, Any], symbols2: Dict[str, Any]) -> float:
        """Compute similarity between two symbol sets"""
        similarity = 0.0
        
        # Class name similarity
        classes1 = set(symbols1.get('classes', []))
        classes2 = set(symbols2.get('classes', []))
        if classes1 or classes2:
            class_similarity = len(classes1 & classes2) / len(classes1 | classes2)
            similarity += class_similarity * 0.3
        
        # Function name similarity
        functions1 = set(symbols1.get('functions', []))
        functions2 = set(symbols2.get('functions', []))
        if functions1 or functions2:
            func_similarity = len(functions1 & functions2) / len(functions1 | functions2)
            similarity += func_similarity * 0.3
        
        # Import similarity
        imports1 = set(symbols1.get('imports', []))
        imports2 = set(symbols2.get('imports', []))
        if imports1 or imports2:
            import_similarity = len(imports1 & imports2) / len(imports1 | imports2)
            similarity += import_similarity * 0.2
        
        # Content hash similarity (exact match)
        if symbols1.get('content_hash') == symbols2.get('content_hash'):
            similarity += 0.2
        
        return min(similarity, 1.0)
    
    def detect_duplicate_kernels(self) -> List[DuplicateKernel]:
        """Detect duplicate kernels across repository"""
        duplicates = []
        python_files = list(self.repo_root.rglob("*.py"))
        
        # Group files by kernel type
        kernel_groups = defaultdict(list)
        for py_file in python_files:
            if py_file.name.startswith('.') or py_file.suffix == '.pyc':
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                for kernel_type, patterns in self.kernel_patterns.items():
                    if any(pattern in content for pattern in patterns):
                        kernel_groups[kernel_type].append(py_file)
            except Exception as e:
                logger.warning(f"Could not analyze {py_file}: {e}")
        
        # Find duplicates within each kernel type
        for kernel_type, files in kernel_groups.items():
            if len(files) > 1:
                symbols_map = {}
                for file_path in files:
                    symbols_map[file_path] = self.extract_symbols(file_path)
                
                # Compare all pairs
                for i, file1 in enumerate(files):
                    for file2 in files[i+1:]:
                        similarity = self.compute_similarity(
                            symbols_map[file1], 
                            symbols_map[file2]
                        )
                        
                        if similarity > 0.7:  # High similarity threshold
                            duplicates.append(DuplicateKernel(
                                kernel_name=kernel_type,
                                files=[str(file1), str(file2)],
                                confidence=similarity,
                                similarity_score=similarity
                            ))
        
        return duplicates
    
    def detect_duplicate_cores(self) -> List[DuplicateCore]:
        """Detect duplicate cores across repository"""
        duplicates = []
        python_files = list(self.repo_root.rglob("*.py"))
        
        # Group files by core type
        core_groups = defaultdict(list)
        for py_file in python_files:
            if py_file.name.startswith('.') or py_file.suffix == '.pyc':
                continue
            
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                
                for core_type, patterns in self.core_patterns.items():
                    if any(pattern in content for pattern in patterns):
                        core_groups[core_type].append(py_file)
            except Exception as e:
                logger.warning(f"Could not analyze {py_file}: {e}")
        
        # Find duplicates within each core type
        for core_type, files in core_groups.items():
            if len(files) > 1:
                symbols_map = {}
                for file_path in files:
                    symbols_map[file_path] = self.extract_symbols(file_path)
                
                # Compare all pairs
                for i, file1 in enumerate(files):
                    for file2 in files[i+1:]:
                        similarity = self.compute_similarity(
                            symbols_map[file1], 
                            symbols_map[file2]
                        )
                        
                        if similarity > 0.7:  # High similarity threshold
                            duplicates.append(DuplicateCore(
                                core_name=core_type,
                                files=[str(file1), str(file2)],
                                confidence=similarity,
                                similarity_score=similarity
                            ))
        
        return duplicates

class AMOSBrainGovernorPhaseC:
    """AMOS Brain Governor Phase C: Import Guard + Duplicate Detector"""
    
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root).resolve()
        self.session_id = hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
        
        # Initialize components
        self.import_guard = ImportGuard(self.repo_root)
        self.duplicate_detector = DuplicateDetector(self.repo_root)
        
        # AMOS Brain integration
        self.amos_brain = None
        if AMOSBrainOmegaUltimate:
            try:
                self.amos_brain = AMOSBrainOmegaUltimate(self.repo_root)
                logger.info(f"🧠 AMOS Brain Omega Ultimate ACTIVATED - Session: {self.session_id}")
            except Exception as e:
                logger.warning(f"Could not initialize AMOS Brain Omega Ultimate: {e}")
        
        logger.info(f"🛡️ AMOS Brain Governor Phase C initialized - Session: {self.session_id}")
    
    def run_import_guard(self) -> Dict[str, Any]:
        """Run import guard checks"""
        logger.info("🛡️ Running Import Guard checks...")
        start_time = time.time()
        
        all_violations = []
        python_files = list(self.repo_root.rglob("*.py"))
        
        for py_file in python_files:
            if py_file.name.startswith('.') or py_file.suffix == '.pyc':
                continue
            
            # Check import violations
            import_violations = self.import_guard.check_import_violations(py_file)
            all_violations.extend(import_violations)
            
            # Check write API violations
            write_violations = self.import_guard.check_write_api_usage(py_file)
            all_violations.extend(write_violations)
        
        # Categorize violations
        violations_by_type = defaultdict(list)
        violations_by_severity = defaultdict(list)
        
        for violation in all_violations:
            violations_by_type[violation.violation_type].append(violation)
            violations_by_severity[violation.severity].append(violation)
        
        scan_time = time.time() - start_time
        
        result = {
            'session_id': self.session_id,
            'scan_time': scan_time,
            'total_violations': len(all_violations),
            'files_checked': len(python_files),
            'violations_by_type': dict(violations_by_type),
            'violations_by_severity': dict(violations_by_severity),
            'critical_violations': len(violations_by_severity['CRITICAL']),
            'high_violations': len(violations_by_severity['HIGH']),
            'amos_brain_active': self.amos_brain is not None
        }
        
        logger.info(f"🛡️ Import Guard complete: {len(all_violations)} violations in {scan_time:.2f}s")
        return result
    
    def run_duplicate_detection(self) -> Dict[str, Any]:
        """Run duplicate kernel/core detection"""
        logger.info("🔍 Running Duplicate Detection...")
        start_time = time.time()
        
        # Detect duplicate kernels
        duplicate_kernels = self.duplicate_detector.detect_duplicate_kernels()
        
        # Detect duplicate cores
        duplicate_cores = self.duplicate_detector.detect_duplicate_cores()
        
        scan_time = time.time() - start_time
        
        result = {
            'session_id': self.session_id,
            'scan_time': scan_time,
            'duplicate_kernels': [
                {
                    'kernel_name': dk.kernel_name,
                    'files': dk.files,
                    'confidence': dk.confidence,
                    'similarity_score': dk.similarity_score
                }
                for dk in duplicate_kernels
            ],
            'duplicate_cores': [
                {
                    'core_name': dc.core_name,
                    'files': dc.files,
                    'confidence': dc.confidence,
                    'similarity_score': dc.similarity_score
                }
                for dc in duplicate_cores
            ],
            'total_duplicate_kernels': len(duplicate_kernels),
            'total_duplicate_cores': len(duplicate_cores),
            'amos_brain_active': self.amos_brain is not None
        }
        
        logger.info(f"🔍 Duplicate Detection complete: {len(duplicate_kernels)} kernels, {len(duplicate_cores)} cores in {scan_time:.2f}s")
        return result
    
    def run_phase_c_complete(self) -> Dict[str, Any]:
        """Run complete Phase C analysis"""
        logger.info("🚀 Starting Phase C: Import Guard + Duplicate Detection...")
        
        import_results = self.run_import_guard()
        duplicate_results = self.run_duplicate_detection()
        
        combined_results = {
            'phase': 'C',
            'session_id': self.session_id,
            'timestamp': datetime.now().isoformat(),
            'import_guard_results': import_results,
            'duplicate_detection_results': duplicate_results,
            'amos_brain_active': self.amos_brain is not None,
            'overall_risk_score': self._compute_overall_risk(import_results, duplicate_results)
        }
        
        logger.info(f"🚀 Phase C complete - Overall Risk Score: {combined_results['overall_risk_score']:.3f}")
        return combined_results
    
    def _compute_overall_risk(self, import_results: Dict[str, Any], duplicate_results: Dict[str, Any]) -> float:
        """Compute overall risk score for Phase C"""
        import_risk = (
            import_results['critical_violations'] * 0.4 +
            import_results['high_violations'] * 0.2 +
            import_results['total_violations'] * 0.1
        )
        
        duplicate_risk = (
            duplicate_results['total_duplicate_kernels'] * 0.15 +
            duplicate_results['total_duplicate_cores'] * 0.15
        )
        
        return min(import_risk + duplicate_risk, 1.0)

def main():
    """Main entrypoint"""
    if len(sys.argv) < 2:
        print("Usage: python amos_brain_governor_phase_c.py <repo_root> [command]")
        print("Commands: import-guard, duplicate-detection, phase-c-complete")
        sys.exit(1)
    
    repo_root = sys.argv[1]
    command = sys.argv[2] if len(sys.argv) > 2 else "phase-c-complete"
    
    governor = AMOSBrainGovernorPhaseC(repo_root)
    
    if command == "import-guard":
        result = governor.run_import_guard()
        print(f"IMPORT_GUARD: {result['total_violations']} violations, {result['scan_time']:.2f}s")
    
    elif command == "duplicate-detection":
        result = governor.run_duplicate_detection()
        print(f"DUPLICATE_DETECTION: {result['total_duplicate_kernels']} kernels, {result['total_duplicate_cores']} cores, {result['scan_time']:.2f}s")
    
    elif command == "phase-c-complete":
        result = governor.run_phase_c_complete()
        print(f"PHASE_C_COMPLETE: Risk Score {result['overall_risk_score']:.3f}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()


```

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[BRAIN_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
