---
title: "AMOS-L AST Definition with Structural Kinds and Type Rules"
type: knowledge_specification
source: 11_KNOWLEDGE
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 11_KNOWLEDGE/11_KNOWLEDGE_MOC
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: knowledge_synthesis
tags:
  - amos-os
  - knowledge
  - reference
---
# AMOS-L AST Definition with Structural Kinds and Type Rules

## GOAL
Define the Abstract Syntax Tree structure for AMOS-L with formal structural kind system and type inference rules.

## FORMALIZATION

The AST is defined as a typed tree structure A = (N, E, K, Γ) where:
- N = set of AST nodes
- E = edges between nodes (parent-child relationships)
- K = structural kind system
- Γ = typing environment mapping identifiers to kinds

## CORE STRUCTURES

### Structural Kind Hierarchy
```
Kind ::= BaseKind | CompositeKind | FunctionKind

BaseKind ::= 
    | Structure      // Structural definitions
    | Node          // Node elements
    | Relation      // Relations between nodes
    | Graph         // Graph structures
    | Field         // Field objects
    | Wave          // Wave objects
    | Tensor        | Tensor objects
    | Operator      | Transformation operators
    | Rewrite       | Rewrite rules
    | Constraint    | Constraints
    | Invariant     | Invariants
    | Closure       | Closure objects
    | Model         | Compressed models
    | Equivalence   // Equivalence relations
    | Expr          // Mathematical expressions
    | Space         // Space definitions
    | Manifold      // Manifold structures
    | Category      // Category theory objects
    | Functor       // Functor objects
    | Type          // Type objects
    | Path          // Path objects

CompositeKind ::= 
    | Product(K1, K2)      // Product type
    | Sum(K1, K2)          // Sum type
    | List(K)              // List type
    | Set(K)               // Set type
    | Map(K1, K2)          // Map type

FunctionKind ::= 
    | Arrow(K1, K2)        // Function type K1 → K2
    | Transform(K)         // Transform over kind K
```

### AST Node Schema
```
ASTNode ::= 
    | ProgramNode(program)
    | StructDefNode(struct_def)
    | FieldDefNode(field_def)
    | WaveDefNode(wave_def)
    | TensorDefNode(tensor_def)
    | OperatorDefNode(operator_def)
    | RewriteDefNode(rewrite_def)
    | InvariantDefNode(invariant_def)
    | ModelDefNode(model_def)
    | EquivalenceDefNode(equivalence_def)
    | QuotientDefNode(quotient_def)
    | ExprNode(expr)
    | PatternNode(pattern)
    | ConstraintNode(constraint)
    | LawNode(law)
    | IdentifierNode(identifier)
    | NumberNode(number)
    | BinaryOpNode(op, left, right)
    | UnaryOpNode(op, operand)
    | FunctionCallNode(function, args)
    | DifferentialNode(op, expr, variable)
```

## OPERATORS

### Structural Node Definitions
```
ProgramNode ::= ProgramNode(statements: List[ASTNode], kind: Structure)
    kind_check: ∀s ∈ statements: Γ ⊢ s : Structure

StructDefNode ::= StructDefNode(name: IdentifierNode, body: StructBodyNode, kind: Structure)
    kind_check: Γ ⊢ body : Structure
    type_env: Γ[name] = Structure

StructBodyNode ::= StructBodyNode(members: List[StructMemberNode], kind: Structure)
    kind_check: ∀m ∈ members: Γ ⊢ m : (Node | Relation | Constraint)

StructMemberNode ::= 
    | NodeDeclNode(node: IdentifierNode, kind: Node)
    | RelationDeclNode(relation: IdentifierNode, source: IdentifierNode, target: IdentifierNode, kind: Relation)
    | ConstraintDeclNode(constraint: IdentifierNode, body: ConstraintNode, kind: Constraint)
```

### Mathematical Object Nodes
```
FieldDefNode ::= FieldDefNode(name: IdentifierNode, params: ParameterListNode, body: FieldBodyNode, kind: Field)
    kind_check: Γ ⊢ params : List(Type) ∧ Γ ⊢ body : Field

FieldBodyNode ::= FieldBodyNode(expressions: List[FieldExprNode], kind: Field)
    kind_check: ∀e ∈ expressions: Γ ⊢ e : Expr

FieldExprNode ::= FieldExprNode(lhs: IdentifierNode, rhs: ExprNode, kind: Expr)
    kind_check: Γ ⊢ lhs : Identifier ∧ Γ ⊢ rhs : Expr

WaveDefNode ::= WaveDefNode(name: IdentifierNode, params: ParameterListNode, body: WaveBodyNode, kind: Wave)
    kind_check: Γ ⊢ params : List(Type) ∧ Γ ⊢ body : Wave

TensorDefNode ::= TensorDefNode(name: IdentifierNode, params: ParameterListNode, body: TensorBodyNode, kind: Tensor)
    kind_check: Γ ⊢ params : List(Type) ∧ Γ ⊢ body : Tensor
```

### Expression Nodes
```
ExprNode ::= 
    | IdentifierNode(value: String, kind: Expr)
    | NumberNode(value: Float, kind: Expr)
    | BinaryOpNode(op: BinaryOperator, left: ExprNode, right: ExprNode, kind: Expr)
    | UnaryOpNode(op: UnaryOperator, operand: ExprNode, kind: Expr)
    | FunctionCallNode(function: IdentifierNode, args: List[ExprNode], kind: Expr)
    | DifferentialNode(op: DifferentialOperator, expr: ExprNode, variable: IdentifierNode, kind: Expr)

BinaryOperator ::= '+' | '-' | '*' | '/' | '^' | '.' | '×' | '÷' | '∧' | '∨' | '→' | '↔'
UnaryOperator ::= '-' | '∇' | '∂' | '∫' | '∑' | '∏'
DifferentialOperator ::= 'd' | '∂' | '∇'

FunctionCallNode ::= FunctionCallNode(function: IdentifierNode, args: List[ExprNode], kind: Expr)
    kind_check: Γ ⊢ function : Arrow(List(Expr), Expr) ∧ ∀a ∈ args: Γ ⊢ a : Expr
```

### Transformation Nodes
```
OperatorDefNode ::= OperatorDefNode(name: IdentifierNode, signature: OperatorSignatureNode, body: OperatorBodyNode, kind: Operator)
    kind_check: Γ ⊢ signature : Arrow(List(Type), List(Type)) ∧ Γ ⊢ body : Expr

OperatorSignatureNode ::= OperatorSignatureNode(params: ParameterListNode, returns: ParameterListNode, kind: Arrow(List(Type), List(Type)))

RewriteDefNode ::= RewriteDefNode(name: IdentifierNode, pattern: PatternNode, replacement: PatternNode, condition: Option[ConditionNode], kind: Rewrite)
    kind_check: Γ ⊢ pattern : Expr ∧ Γ ⊢ replacement : Expr ∧ (condition = None ∨ Γ ⊢ condition : Expr)

PatternNode ::= 
    | ExprPatternNode(expr: ExprNode, kind: Expr)
    | StructPatternNode(name: IdentifierNode, args: List[PatternNode], kind: Structure)

ConditionNode ::= ConditionNode(expr: ExprNode, kind: Expr)
    kind_check: Γ ⊢ expr : Expr
```

### Invariant and Model Nodes
```
InvariantDefNode ::= InvariantDefNode(name: IdentifierNode, transforms: List[IdentifierNode], spec: InvariantSpecNode, kind: Invariant)
    kind_check: ∀t ∈ transforms: Γ[t] = Operator ∧ Γ ⊢ spec : Expr

InvariantSpecNode ::= 
    | MathInvariantNode(expr: ExprNode, kind: Expr)
    | FindInvariantNode(target: IdentifierNode, structure: IdentifierNode, kind: Invariant)

ModelDefNode ::= ModelDefNode(name: IdentifierNode, criterion: ModelCriterionNode, constraints: List[ConstraintNode], kind: Model)
    kind_check: Γ ⊢ criterion : Expr ∧ ∀c ∈ constraints: Γ ⊢ c : Constraint

ModelCriterionNode ::= ModelCriterionNode(expr: ExprNode, kind: Expr)
    kind_check: Γ ⊢ expr : Expr
```

### Equivalence and Quotient Nodes
```
EquivalenceDefNode ::= EquivalenceDefNode(name: IdentifierNode, left: IdentifierNode, right: IdentifierNode, condition: ConditionNode, kind: Equivalence)
    kind_check: Γ ⊢ left : Expr ∧ Γ ⊢ right : Expr ∧ Γ ⊢ condition : Expr

QuotientDefNode ::= QuotientDefNode(name: IdentifierNode, structure: IdentifierNode, equivalence: IdentifierNode, kind: Quotient)
    kind_check: Γ ⊢ structure : Structure ∧ Γ ⊢ equivalence : Equivalence
```

## TYPE RULES

### Typing Environment
```
Γ ::= ∅ | Γ, x:K

Environment extends: Γ' = Γ ∪ {x:K} if x ∉ dom(Γ)
Environment lookup: Γ(x) = K if x:K ∈ Γ
```

### Base Typing Rules
```
T-IDENT: 
    Γ ⊢ x : K if x:K ∈ Γ

T-NUMBER:
    Γ ⊢ n : Expr

T-STRUCT:
    Γ ⊢ structure name { ... } : Structure

T-FIELD:
    Γ ⊢ field name(params) { ... } : Field

T-WAVE:
    Γ ⊢ wave name(params) { ... } : Wave

T-TENSOR:
    Γ ⊢ tensor name(params) { ... } : Tensor

T-OPERATOR:
    Γ ⊢ operator name : Operator

T-REWRITE:
    Γ ⊢ rewrite name : Rewrite

T-INVARIANT:
    Γ ⊢ invariant name : Invariant

T-MODEL:
    Γ ⊢ model name : Model
```

### Expression Typing Rules
```
T-BINARY:
    Γ ⊢ e1 : Expr
    Γ ⊢ e2 : Expr
    ───────────────────────
    Γ ⊢ e1 op e2 : Expr

T-UNARY:
    Γ ⊢ e : Expr
    ───────────────────────
    Γ ⊢ op(e) : Expr

T-FUNCTION:
    Γ ⊢ f : Arrow(List(Expr), Expr)
    Γ ⊢ args : List(Expr)
    ───────────────────────────────────────
    Γ ⊢ f(args) : Expr

T-DIFFERENTIAL:
    Γ ⊢ e : Expr
    Γ ⊢ x : Expr
    ───────────────────────────────
    Γ ⊢ ∂(e, x) : Expr
```

### Composition Typing Rules
```
T-COMPOSE-STRUCTURE:
    Γ ⊢ s1 : Structure
    Γ ⊢ s2 : Structure
    ───────────────────────────────
    Γ ⊢ s1 ~ s2 : Equivalence

T-QUOTIENT:
    Γ ⊢ s : Structure
    Γ ⊢ equiv : Equivalence
    ───────────────────────────────
    Γ ⊢ s / equiv : Quotient

T-REWRITE:
    Γ ⊢ pattern : Expr
    Γ ⊢ replacement : Expr
    ───────────────────────────────────────
    Γ ⊢ pattern -> replacement : Rewrite

T-CLOSURE:
    Γ ⊢ e : Structure
    ───────────────────────────────
    Γ ⊢ close(e) : Closure

T-COMPRESSION:
    Γ ⊢ e : Structure
    ───────────────────────────────
    Γ ⊢ compress(e) : Model

T-INVARIANT:
    Γ ⊢ e : Expr
    Γ ⊢ transforms : [Operator]
    ───────────────────────────────────────────────
    Γ ⊢ invariant(e, transforms) : Invariant
```

### Function Typing Rules
```
T-ARROW:
    Γ ⊢ e1 : K1
    Γ ⊢ e2 : K2
    ───────────────────────
    Γ ⊢ (e1 -> e2) : Arrow(K1, K2)

T-PRODUCT:
    Γ ⊢ e1 : K1
    Γ ⊢ e2 : K2
    ───────────────────────
    Γ ⊢ (e1, e2) : Product(K1, K2)

T-LIST:
    Γ ⊢ e : K
    ───────────────────────
    Γ ⊢ [e] : List(K)

T-SET:
    Γ ⊢ e : K
    ───────────────────────
    Γ ⊢ {e} : Set(K)
```

## IR LOWERING

### AST to IR Mapping
```
lower_structure: StructDefNode → IRStruct
lower_field: FieldDefNode → IRField
lower_wave: WaveDefNode → IRWave
lower_tensor: TensorDefNode → IRTensor
lower_operator: OperatorDefNode → IROperator
lower_rewrite: RewriteDefNode → IRRewrite
lower_invariant: InvariantDefNode → IRInvariant
lower_model: ModelDefNode → IRModel
lower_expr: ExprNode → IRExpr
```

### Lowering Functions
```
lower_structure(node: StructDefNode): IRStruct =
    IRStruct(
        id = node.name.value,
        nodes = [n.name.value for n in node.body.members if isinstance(n, NodeDeclNode)],
        relations = [(r.relation.value, r.source.value, r.target.value) for r in node.body.members if isinstance(r, RelationDeclNode)],
        constraints = [lower_constraint(c) for c in node.body.members if isinstance(c, ConstraintDeclNode)]
    )

lower_expr(node: ExprNode): IRExpr =
    match node:
        case IdentifierNode(value, _) => IREVar(value)
        case NumberNode(value, _) => IREConst(value)
        case BinaryOpNode(op, left, right, _) => IREBinaryOp(op, lower_expr(left), lower_expr(right))
        case UnaryOpNode(op, operand, _) => IREUnaryOp(op, lower_expr(operand))
        case FunctionCallNode(function, args, _) => IRECall(function.value, [lower_expr(arg) for arg in args])
        case DifferentialNode(op, expr, variable, _) => IREDifferential(op, lower_expr(expr), variable.value)

lower_rewrite(node: RewriteDefNode): IRRewrite =
    IRRewrite(
        id = node.name.value,
        pattern = lower_pattern(node.pattern),
        replacement = lower_pattern(node.replacement),
        condition = lower_condition(node.condition) if node.condition else None
    )
```

## EXECUTION SEMANTICS

### AST Evaluation
```
eval_ast(node: ASTNode, Γ: TypingEnv): Value =
    match node:
        case ProgramNode(statements, _) => 
            for stmt in statements: eval_ast(stmt, Γ)
            return Unit
            
        case StructDefNode(name, body, _) =>
            Γ[name.value] = Structure
            return eval_struct(body, Γ)
            
        case ExprNode(expr, kind) =>
            return eval_expr(expr, Γ)
            
        case RewriteDefNode(name, pattern, replacement, condition, _) =>
            rewrite = create_rewrite(pattern, replacement, condition, Γ)
            Γ[name.value] = rewrite
            return rewrite
```

### Expression Evaluation
```
eval_expr(expr: ExprNode, Γ: TypingEnv): ExprValue =
    match expr:
        case IdentifierNode(value, _) => Γ.lookup(value)
        case NumberNode(value, _) => NumberValue(value)
        case BinaryOpNode(op, left, right, _) => 
            lval = eval_expr(left, Γ)
            rval = eval_expr(right, Γ)
            return apply_binary_op(op, lval, rval)
        case UnaryOpNode(op, operand, _) =>
            val = eval_expr(operand, Γ)
            return apply_unary_op(op, val)
        case FunctionCallNode(function, args, _) =>
            func = Γ.lookup(function.value)
            arg_vals = [eval_expr(arg, Γ) for arg in args]
            return apply_function(func, arg_vals)
```

## CORRECTNESS CONDITIONS

### Type Safety
For all AST nodes n and typing environment Γ:
If Γ ⊢ n : K and eval_ast(n, Γ) = v, then v has kind K.

### Determinism
For any AST node n and typing environment Γ:
If Γ ⊢ n : K and eval_ast(n, Γ) is defined, then eval_ast(n, Γ) yields a unique result.

### Preservation
If Γ ⊢ n : K and n → n' is a valid transformation, then Γ ⊢ n' : K.

### Progress
If Γ ⊢ n : K and n is well-typed, then either n is a value or there exists n' such that n → n'.

## FAILURE MODES

### Type Errors
- Kind mismatch: Expected K1 but got K2
- Unbound identifier: x not in Γ
- Invalid function application: f not of Arrow type

### Structural Errors
- Circular dependencies in structure definitions
- Invalid relation endpoints
- Constraint violations

### Runtime Errors
- Division by zero in expression evaluation
- Undefined function calls
- Non-terminating rewrite sequences

## IMPLEMENTATION PLAN

### Phase 1: Core AST Classes
1. Implement base AST node classes
2. Create structural kind hierarchy
3. Build typing environment
4. Implement type checker

### Phase 2: Expression System
1. Define expression node hierarchy
2. Implement expression evaluator
3. Create operator system
4. Add differential operators

### Phase 3: Transformation System
1. Implement rewrite rule AST nodes
2. Build pattern matching system
3. Create transformation engine
4. Add condition evaluation

### Phase 4: Lowering System
1. Define IR node schema
2. Implement AST to IR lowering
3. Create IR validation
4. Add IR serialization

## TEST CASES

### Structure Definition
```
structure MindWorld {
    node agent
    node body
    node environment
    relation senses(agent, environment)
    relation embodied(agent, body)
}
```

### Field Definition
```
field E(x,t) {
    E = vector_field(x,t)
}
```

### Rewrite Rule
```
rewrite Perception {
    senses(agent, environment) -> model(agent, environment)
}
```

### Invariant Definition
```
invariant StructureInvariant over {T1, T2, T3} {
    find preserved_structure in system
}
```

### Model Definition
```
model CompressedModel {
    argmin(L(model) + L(data|model)) subject to {
        constraint1,
        constraint2
    }
}
```

## NEXT DEPENDENCIES

1. Kernel IR schema implementation
2. Deterministic operational semantics
3. Rewrite engine with confluence checking
4. Closure solver implementation
5. Invariant mining algorithm
6. Compression engine with MDL
7. Continuous mathematics operators
8. Agent self-extension protocol
9. Reference interpreter
10. Comprehensive validation suite
