# Procedural macro architecture

## Purpose

Use procedural macros for repeated syntax
transformations with a concrete consumer.
Apply this note before designing derives,
attributes, or function-like DSL macros.
The macro should improve a recurring task while
preserving understandable generated Rust and diagnostics.

## Source posture

[Procedural macros](https://doc.rust-lang.org/reference/procedural-macros.html) documents the compiler interface.
[Syn](https://docs.rs/syn/latest/syn/) and [Quote](https://docs.rs/quote/latest/quote/) document common implementation libraries.
Dependency versions must follow the
consuming workspace and declared compiler support.
The architecture below is a recommendation, not a
requirement that every project adopt these libraries.

## Practice

Demonstrate the repeated
handwritten Rust before proposing a macro.
Keep parsing, semantic validation, and token
emission separate enough to test independently.
Use a normal library crate for reusable logic when
the proc-macro crate restrictions require separation.
Preserve source spans through parsing
so errors point to the user's input.
Return deliberate compile errors for unsupported
syntax rather than panicking with an internal message.
Generate explicit paths and test dependency renaming.
Avoid implicit filesystem,
environment, or network dependencies in expansion.
Treat procedural macros as host-executed
build dependencies with supply-chain exposure.

## Worked transformation design

Suppose a derive creates a stable
diagnostic-code accessor for an enum.
Specify how each variant declares its code
and whether duplicate codes are rejected.
Parse only the supported attribute
grammar and retain the span of each declaration.
Validate missing attributes, duplicate codes,
malformed literals, and unsupported item kinds.
Emit the same ordinary Rust
implementation a reviewer could write manually.
Test a valid enum with payload-bearing
variants and a generic enum if generics are supported.
Test the downstream call without importing
implementation helper names accidentally.
Document how generated paths resolve
when the runtime support crate has an alias.
Do not silently assign codes from variant order
because reordering would change the external contract.

## Hygiene and visibility

Generated names can collide with user code;
choose scoped helpers and test adversarial names.
Do not assume procedural macros
inherit declarative-macro hygiene behavior.
Keep emitted implementation details
private unless the public contract requires them.
Respect the user's generics, where clauses,
and existing attributes when transforming items.
Avoid consuming unrelated
attributes during an attribute-macro rewrite.
Check whether emitted types leak a dependency into the public API.
Test re-exports and use from a
sibling module as well as the crate root.
Keep diagnostics readable when multiple
errors can be reported in one invocation.

## Testing layers

Unit-test the parser on accepted and rejected syntax forms.
Test validation on parsed structures
without invoking the compiler where possible.
Compile downstream examples to exercise
expansion, name resolution, and type checking together.
Use compile-fail fixtures for the
intended diagnostic class and source location.
Avoid asserting entire compiler wording when
toolchain differences would create irrelevant churn.
Inspect expansion when a type error points into generated code.
Test the minimum supported compiler and relevant editions.
Use a renamed dependency fixture when
emitted paths depend on the runtime crate.

## Maintenance choices

Version syntax deliberately because users
may persist macro invocations across releases.
Offer ordinary Rust escape hatches when
generated behavior cannot express a special case.
Keep proc-macro dependencies small
because they affect every downstream compile.
Measure expansion size when generated
implementations multiply compile time.
Prefer a function or declarative macro for simpler repetition.
Document unsupported forms explicitly instead
of pretending the parser covers all Rust syntax.
Keep semantic checks independent of
string formatting so diagnostics remain stable.

## Validation and return

Report parser cases, downstream
compile cases, negative cases, and toolchain.
Show one representative expansion with its original source.
State which checks occur during
parsing and which are left to rustc.
Record any environment inputs needed for reproducible expansion.
Explain whether the macro generates
executable effects or only data definitions.

## Limit

A procedural macro emits Rust and
cannot extend rustc's underlying type theory.
A successful expansion does not prove external
domain semantics or theorem-level properties.
Stronger guarantees require a separate
trusted checker whose result is actually verified.
