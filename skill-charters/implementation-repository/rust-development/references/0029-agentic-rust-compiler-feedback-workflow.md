# Agentic Rust compiler feedback workflow

## Purpose

Use compiler diagnostics to improve a bounded
implementation without erasing its intended contract.
Apply this note when an agent writes Rust,
fixes compiler errors, or resumes a failed check.
The loop should converge on the requested behavior
with attributable edits and reproducible evidence.

## Source posture

[Compiler diagnostics](https://doc.rust-lang.org/rustc/json.html) documents structured compiler output.
[Cargo check](https://doc.rust-lang.org/cargo/commands/cargo-check.html) documents compilation checking.
[Clippy](https://doc.rust-lang.org/clippy/) documents linting.
This workflow is an engineering
recommendation and does not expand the user's task.

## Practice

Read the current source and error before modifying code.
Run the narrow relevant command
with the intended package and features.
Start with the first causal error rather than
treating every downstream error independently.
Explain the ownership, bound, or
interface mismatch in concrete terms.
Change the model or caller deliberately rather
than adding clone, static, or unsafe automatically.
Keep edits small enough that the
next compiler result is interpretable.
Preserve unrelated changes in a shared checkout.
Record the command and actual exit status.

## Worked borrow repair

Suppose a map lookup returns a
reference that remains live across an insertion.
Read where the reference is last used.
If only an identifier is needed, copy or
clone that small identifier before mutation.
If the algorithm needs the original value,
consider removing it or splitting the operation.
Do not clone the entire map merely to obtain a green build.
Add a regression test covering the
behavior that caused the overlapping access.
Re-run the narrow compiler check and test.
Inspect whether the repair
changes allocation or update ordering.
Explain the chosen ownership tradeoff in the return.

## Diagnostic triage

A missing dependency feature requires
checking the manifest and intended support matrix.
A trait-bound error requires
identifying which caller actually needs the bound.
A type mismatch at a wire boundary may
indicate missing validation rather than a cast.
A lifetime error may reveal an
owned-versus-borrowed API mismatch.
A missing method may indicate the wrong crate
version rather than an absent feature to implement.
A linker failure belongs to a
different stage from Rust type checking.
A test panic requires reading the
failed assertion and reproduction input.
A lint is evidence to evaluate, not
permission to change unrelated behavior.

## Tool discipline

Use cargo check for rapid type
feedback but run tests for behavior.
Use formatting checks to separate
mechanical layout from semantic failures.
Do not suppress warnings broadly
to conceal newly introduced issues.
Apply lint suggestions only after
checking their semantic consequence.
Avoid running stale binaries after compilation failed.
Check that a test filter matched the intended case.
Keep compiler version and feature
selection visible across repeated attempts.
Stop repeating an identical command when
no source or environment condition changed.

## Agent decision quality

Do not invent APIs from memory when
local dependency documentation is available.
Inspect one real caller before
designing a replacement interface.
Use a minimal example to
isolate a difficult language question.
Preserve expected failures that protect a contract.
Do not weaken tests simply because the
implementation does not satisfy them.
Distinguish a justified test correction
from changing the acceptance criterion.
Keep generated comments focused on invariants and decisions.
Ask a specific semantic question when source
evidence cannot settle the required behavior.

## Validation and return

Run the smallest behavior test
after the compiler accepts the change.
Then run repository-required checks
proportionate to the changed boundary.
Report focused success separately
from unrelated baseline failures.
Include unresolved warnings that affect confidence.
Record unrun platform or feature checks.
Review the final diff for accidental scope expansion.
Return the concrete behavior change and remaining limitations.
Keep terminal history as evidence,
not as the user's primary explanation.

## Limit

Compiler acceptance does not prove
the user's requirement was satisfied.
Lint cleanliness does not establish
performance, security, or semantic approval.
A feedback loop succeeds only when its
tests and source contract remain meaningful.
