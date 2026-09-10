# Declarative macros and hygiene

## Purpose

Use macro_rules for local repetition where
functions or generics cannot express the syntax.
Apply this reference to repetitive tests, item
declarations, or compact construction helpers.
Keep expansion predictable enough that a consumer
can diagnose errors without learning hidden rules.

## Source posture

[Macros by example](https://doc.rust-lang.org/reference/macros-by-example.html) documents matching and hygiene.
[Edition guide](https://doc.rust-lang.org/edition-guide/) documents edition-sensitive changes.
The practical design advice below is a recommendation.
Check fragment behavior against the
edition in which the macro is defined.

## Practice

Write the repeated code first and
identify the smallest syntactic repetition.
Choose fragment specifiers deliberately
rather than using token trees for every input.
Use clear separators and accept a trailing
separator when it improves ordinary call-site use.
Document whether expressions are
evaluated once, repeatedly, or conditionally.
Avoid macros whose expansion unexpectedly
returns from or mutates the caller's scope.
Use dollar-crate paths for exported
helpers when referring to the defining crate.
Keep helper visibility compatible with downstream expansion.
Prefer a function when type checking and
ordinary arguments already solve the problem.

## Worked single evaluation

This example binds the expression once before inspecting its value.

```rust
macro_rules! require_nonempty {
    ($value:expr) => {{
        let value = $value;
        if value.is_empty() { Err("empty") } else { Ok(value) }
    }};
}
fn main() {
    let result = require_nonempty!(String::from("item"));
    assert_eq!(result.unwrap(), "item");
}
```

A real public API should explain
whether ownership is moved into the macro.
Do not assume borrowing because the call visually resembles a predicate.
Test an expression with an observable
counter if evaluation multiplicity matters.

## Matcher design

Place specific arms before broader arms
when matching order affects selection.
Avoid ambiguous repetition boundaries that
force callers into confusing token patterns.
Use nested repetitions only when the
input structure has a corresponding hierarchy.
Remember that captured fragments are not
always freely rematchable as raw tokens.
Test empty repetition, a single element, and multiple elements.
Handle trailing commas deliberately rather
than depending on accidental matcher behavior.
Use a final diagnostic arm only when it
produces a clearer error than the compiler.
Do not swallow malformed input into a broad
arm that generates unrelated downstream errors.

## Hygiene and exported use

Test local variables whose names resemble the macro's temporary bindings.
Test expansion in a module with no convenient prelude imports.
Use fully qualified paths when external
names would otherwise depend on the caller.
Check whether an exported helper remains reachable from a different crate.
Do not assume local and exported macros
have identical name-resolution conditions.
Preserve the caller's ability to use the result in a larger expression.
Use a block expression when temporary
bindings should remain scoped to the expansion.
Avoid exposing an implementation macro
merely because export made it convenient.

## Edition and evolution

Document the supported input grammar
as a public API if callers rely on it.
Compile fixtures in each supported edition when fragment matching differs.
Avoid changing an arm's accepted syntax in
a way that redirects an existing invocation.
Keep generated trait bounds visible in
documentation when they affect call-site types.
Separate semantic changes from formatting improvements in expansion.
Prefer a small stable macro surface
over a general-purpose embedded language.
If syntax complexity keeps growing, compare
a proc macro with ordinary data constructors.

## Validation

Compile accepted expression, item, or
pattern contexts relevant to the macro.
Include malformed input and an
unsupported form with a comprehensible diagnostic.
Test expression evaluation count and move behavior.
Exercise downstream use, renamed
imports, and adversarial local identifiers.
Check generated code for unnecessary clones or allocations.
Review whether error locations point to useful call-site information.
Record the macro-definition edition and compiler used for these checks.

## Limit

Declarative macros transform syntax and
do not grant stronger semantic guarantees.
Hygiene does not prove the generated algorithm correct.
A concise invocation can still hide cost,
ownership transfer, or effects unless those are documented.
