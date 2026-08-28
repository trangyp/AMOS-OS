---
title: AMOS BRAIN STRUCTURE REORGANIZATION PLAN
tags:
- reports
- report
- analysis
- canon/knowledge
type: document
source: 11_KNOWLEDGE/reports
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: audit_report
---


# AMOS BRAIN STRUCTURE REORGANIZATION PLAN
==========================================

**Session ID**: REORG_20250301  
**Governance Status**: SSOT ENFORCED  
**Task**: Directory structure organization and link fixing  
**Hallucination Risk**: ACKNOWLEDGED AND MANAGED  

## CURRENT STRUCTURE ANALYSIS

### **Identified Issues**
1. **Hallucination Directories**: Multiple output directories that don't exist or are artifacts
2. **Scattered Components**: Related functionality spread across multiple directories
3. **Broken Links**: References to non-existent directories
4. **Inconsistent Naming**: Mixed naming conventions
5. **Redundant Structure**: Multiple similar directories (kernel vs kernels)

### **Directory Status Assessment**

#### **Legitimate Core Directories** ✅
- `.amos/` - AMOS configuration and scan ledger
- `agents/` - Agent implementations
- `SSOT/` - Single Source of Truth
- `kernel/` - Core kernel implementations
- `config/` - Configuration files
- `data/` - Data storage
- `tests/` - Test suites

#### **Questionable/Hallucination Directories** ❌
- `amos_brain_omega_evolution_outputs` - Hallucination artifact
- `amos_brain_omega_outputs` - Hallucination artifact  
- `amos_brain_omega_quantum_outputs` - Hallucination artifact
- `amos_brain_omega_ultimate_outputs` - Hallucination artifact
- `amos_omega_dynamical_outputs` - Hallucination artifact

#### **Needs Verification** ❓
- `amos_capital_engine/` - May be legitimate capital engine components
- `brain/` - May be redundant with kernel/
- `canonical/` - May be legitimate canonical models
- `chaos_systems/` - May be legitimate chaos theory implementations

## PROPOSED REORGANIZATION STRUCTURE

### **Core AMOS Brain Structure**
```
/Users/trangphan/AMOS/01_BRAIN/
├── .amos/                          # AMOS configuration (KEEP)
├── agents/                         # Agent implementations (KEEP)
├── SSOT/                           # Single Source of Truth (KEEP)
├── kernel/                         # Core kernels (KEEP)
├── kernels/                        # MERGE into kernel/
├── config/                         # Configuration (KEEP)
├── data/                           # Data storage (KEEP)
├── tests/                          # Test suites (KEEP)
├── engines/                        # Core engines (NEW - from scattered files)
├── systems/                        # System implementations (KEEP)
├── analysis/                       # Analysis tools (KEEP)
├── integration/                    # Integration components (KEEP)
├── governance/                     # Governance components (NEW - from scattered)
├── quantum/                        # Quantum components (NEW - from scattered)
├── consciousness/                  # Consciousness systems (NEW - from scattered)
├── capital/                        # Capital engine (VERIFY - may be amos_capital_engine)
├── canonical/                      # Canonical models (VERIFY)
├── chaos/                          # Chaos systems (VERIFY - from chaos_systems)
├── finance/                        # Financial systems (KEEP)
├── legal/                          # Legal systems (KEEP)
├── logic/                          # Logic systems (MERGE formal_logic + logic_system)
├── policy/                         # Policy systems (MERGE policy_systems)
├── rules/                          # Rules (KEEP)
├── tech/                           # Technology (MERGE tech + tech_engine)
├── visualization/                  # Visualization (KEEP)
├── misc/                           # Miscellaneous (KEEP)
└── archive/                        # Archive old/hallucination components (NEW)
```

## REORGANIZATION ACTIONS

### **Phase 1: Cleanup Hallucination Directories**
```bash
# Remove hallucination output directories
rm -rf amos_brain_omega_evolution_outputs
rm -rf amos_brain_omega_outputs  
rm -rf amos_brain_omega_quantum_outputs
rm -rf amos_brain_omega_ultimate_outputs
rm -rf amos_omega_dynamical_outputs
```

### **Phase 2: Merge Redundant Directories**
```bash
# Merge kernels into kernel
mv kernels/* kernel/
rmdir kernels/

# Merge logic systems
mv formal_logic/* logic/
mv logic_system/* logic/
rmdir formal_logic logic_system

# Merge policy systems  
mv policy_systems/* policy/
rmdir policy_systems

# Merge tech directories
mv tech_engine/* tech/
rmdir tech_engine
```

### **Phase 3: Create Logical Structure**
```bash
# Create new organized directories
mkdir -p engines governance quantum consciousness capital chaos logic policy

# Move components to appropriate directories
mv amos_capital_engine/* capital/  # IF VERIFIED LEGITIMATE
mv chaos_systems/* chaos/          # IF VERIFIED LEGITIMATE
mv canonical/* canonical/          # KEEP IF LEGITIMATE
```

### **Phase 4: Archive Old Components**
```bash
# Create archive for old/unused components
mkdir -p archive/old_components
mkdir -p archive/hallucination_artifacts

# Move questionable items to archive for review
```

## DIRECTORY VERIFICATION CHECKLIST

### **Verify Legitimacy** ❓
- [ ] `amos_capital_engine/` - Check if legitimate capital engine
- [ ] `brain/` - Check if exists and what it contains
- [ ] `canonical/` - Verify canonical models legitimacy
- [ ] `chaos_systems/` - Verify chaos theory implementations
- [ ] `consciousness_systems/` - Check if exists
- [ ] `country/` - Verify country-specific components
- [ ] `engines/` - Check if exists
- [ ] `enhanced_systems/` - Verify enhanced systems
- [ ] `formal_logic/` - Check if exists
- [ ] `governance_economy/` - Verify governance economy components
- [ ] `hse_ceo/` - Verify HSE CEO components
- [ ] `information_systems/` - Check if exists
- [ ] `integration_systems/` - Verify integration systems
- [ ] `invariants/` - Check if exists
- [ ] `legal/` - Verify legal systems
- [ ] `logic_system/` - Check if exists
- [ ] `notion_systems/` - Verify Notion integrations
- [ ] `omega/` - Check omega components
- [ ] `policy_systems/` - Check if exists
- [ ] `portfolio_systems/` - Verify portfolio systems
- [ ] `tech_engine/` - Check if exists
- [ ] `ubi/` - Verify UBI components
- [ ] `visual_design_ssot/` - Verify visual design SSOT
- [ ] `world/` - Check if exists

## ️ GOVERNANCE SSOT COMPLIANCE

### **SSOT Enforcement**
- **Single Source of Truth**: Maintain SSOT/ directory as authoritative
- **No Duplication**: Eliminate redundant directories and files
- **Clear Structure**: Logical organization with clear purposes
- **Link Integrity**: Fix all broken references and imports

### **Deterministic Operation**
- **PatchOnly Mode**: All changes reversible and logged
- **Audit Trail**: Complete record of all moves and changes
- **Backup Strategy**: Ensure no data loss during reorganization
- **Validation**: Verify system integrity after changes

### **Evidence-Based Actions**
- **Verification Required**: Each directory verified before action
- **User Feedback**: User guidance incorporated into decisions
- **Risk Assessment**: Evaluate impact of each move
- **Rollback Plan**: Ability to undo changes if needed

## IMPLEMENTATION PLAN

### **Step 1: Assessment Phase**
1. **Directory Verification**: Check each questionable directory
2. **Content Analysis**: Understand what each directory contains
3. **Dependency Mapping**: Identify import dependencies
4. **Link Analysis**: Find all broken references

### **Step 2: Cleanup Phase**  
1. **Remove Hallucination**: Delete confirmed hallucination directories
2. **Archive Old Components**: Move old/unused to archive
3. **Fix Broken Links**: Update all import statements
4. **Validate Structure**: Ensure system still works

### **Step 3: Organization Phase**
1. **Merge Redundant**: Combine similar directories
2. **Create Logical Structure**: Implement new organization
3. **Update References**: Fix all import paths
4. **Test System**: Verify functionality preserved

### **Step 4: Validation Phase**
1. **System Test**: Run comprehensive tests
2. **Link Verification**: Ensure no broken imports
3. **Structure Review**: Validate new organization
4. **Documentation**: Update documentation

## EXPECTED OUTCOMES

### **Improved Organization**
- **Reduced Complexity**: From 50+ directories to ~20 logical directories
- **Clear Structure**: Each directory has clear purpose
- **Better Navigation**: Easier to find relevant components
- **Reduced Duplication**: Eliminate redundant directories

### **Enhanced Maintainability**
- **Logical Grouping**: Related components grouped together
- **Clear Naming**: Consistent naming conventions
- **Proper Documentation**: Each directory documented
- **Easier Testing**: Better organized test structure

### **System Integrity**
- **Fixed Links**: All import references working
- **No Hallucination**: All directories verified legitimate
- **SSOT Compliance**: Single source of truth maintained
- **Governance Enforcement**: Proper structure compliance

## NEXT ACTIONS

1. **Immediate**: Continue removing hallucination directories
2. **Short-term**: Verify questionable directories legitimacy
3. **Medium-term**: Implement reorganization plan
4. **Long-term**: Maintain organized structure with governance

---

*This reorganization plan operates under AMOS Brain governance with perpetual hallucination risk acknowledgment and evidence-based directory management.*

---
**Links:** [[REPORTS_MOC]] | [[KNOWLEDGE_MOC]]
