# Testing, property, fuzz, and model checking

## Purpose

Choose tests from the failure
mechanism and the claim being made.
Use this reference when a change
needs evidence beyond compilation.
The test set should expose plausible defects
without duplicating implementation details.

## Source posture

[Cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) documents test selection.
[Rustdoc tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) documents executable examples.
[Proptest](https://proptest-rs.github.io/proptest/) documents generated testing.
[Loom](https://docs.rs/loom/latest/loom/) documents concurrency exploration.
Each tool's result is bounded by its
configuration and modeled behavior.

## Practice

State the invariant before selecting unit,
integration, property, fuzz, or model tests.
Use unit tests for pure decisions
with clear input-output behavior.
Use integration tests for
producer-consumer contracts and persistence boundaries.
Use compile-fail tests for APIs that
intentionally prohibit an operation.
Use property tests when many
combinations share a meaningful invariant.
Use fuzzing for parser robustness or
other large malformed-input spaces.
Use concurrency model exploration when
interleavings are the failure mechanism.
Avoid tests that only reproduce the
implementation's current wording or branch structure.

## Worked admission tests

Suppose a parser admits a bounded list of unique identifiers.
Test empty input if it is legal, one
identifier, and a representative multi-item list.
Test duplicate values, malformed
encoding, and one input beyond the size limit.
Add a property that admitted outputs
contain no duplicate normalized identifiers.
Build the expected uniqueness check
independently enough to avoid copying the same bug.
Fuzz bytes through the real decoder, not
only through already-valid Rust values.
Assert rejected input performs no storage writes.
Record the seed and minimized failing
case when generated testing finds a defect.
Keep the regression fixture even after the random campaign ends.

## Property quality

A round-trip property is useful but can pass
when encoder and decoder share the same defect.
Add independent known examples or an alternative oracle.
State preconditions so the generator does
not spend most runs on irrelevant cases.
Include boundary-biased
generation for limits and special values.
Keep shrinking enabled when it
produces actionable counterexamples.
Avoid overly broad assumptions that
discard almost every generated input.
Do not claim exhaustive coverage from a finite generated run.
Record the case count and configuration
when they materially affect confidence.

## Compile and documentation tests

Ensure a compile-fail fixture
fails for the intended restriction.
Use a positive companion case to show the API is usable.
Test from a downstream crate when
privacy or exported paths matter.
Keep examples executable through the public facade.
Do not mark a broken example
ignored merely to obtain a passing report.
If an example requires a network or
platform, document that requirement explicitly.
Check that test filters execute a
nonzero number of intended cases.
Separate compilation of tests from execution of tests.

## Concurrency and fuzz limits

A Loom model covers modeled
operations and bounded explored schedules.
Use the instrumented synchronization types required by the model.
A fuzz campaign without a crash
is not proof of parser correctness.
Record duration, corpus, sanitizer or
interpreter mode, and stopping condition.
Keep resource limits so malicious cases
cannot consume unbounded memory or time.
Avoid live external effects from fuzz targets.
Test cancellation and restart separately
when the model excludes process failure.
Retain minimized cases in a stable regression corpus.

## Return evidence

Report the property, test layer, command, toolchain, and outcome.
Name untested platforms, feature
combinations, and external services.
Explain whether expected failures
were observed for the correct reason.
Distinguish passing focused tests
from repository-wide gate failures.
Keep flaky tests visible instead
of silently rerunning until green.
Use a deterministic reproduction to
diagnose nondeterministic failures where possible.
Stop expanding the test suite once
relevant uncertainty is resolved.

## Limit

Coverage percentages do not establish semantic completeness.
Model checks, fuzzing, and property tests each
leave explicit parts of the system unmodeled.
Human acceptance remains separate from automated evidence.
