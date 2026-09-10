# Rust engineering orientation

## Purpose

Turn a Rust request into an observable
behavior change with an identified consumer.
Use this note before editing, after
interruption, or when a checkout contradicts a handoff.
The output is a bounded implementation plan
whose checks can expose a wrong assumption.

## Source posture

[Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html) documents package selection.
[Minimum compiler](https://doc.rust-lang.org/cargo/reference/rust-version.html) documents rust-version.
The workflow here is a recommendation; the
actual repository contract determines acceptance.
Record compiler, edition, target, enabled
features, and lockfile before compatibility claims.

## Practice

Locate the workspace root and affected package;
directory proximity does not prove membership.
Read its public entrypoint, nearest charter,
tests, manifest, and one representative caller.
Inspect the working tree so another author's
changes remain distinguishable from this task.
Translate “support import” into “reject
duplicate identifiers
without modifying stored records.”
Write accepted input, rejected input, resulting
state, and public error before choosing abstractions.
Separate the domain rule from the desktop,
file, network, or command adapter carrying it.
Determine whether the request
authorizes diagnosis, implementation, or review.
Reuse existing types until a concrete requirement
demonstrates that they cannot express the contract.

## Baseline procedure

Run the smallest existing test that
reaches the behavior and record the exit status.
Check the executed test count; a filter
matching zero cases establishes no behavioral baseline.
Classify baseline failures before
repairing files unrelated to the requested change.
Use locked resolution for
reproduction and inspect any lockfile change.
Offline failure may identify a cache
gap rather than an implementation defect.
Keep scratch builds outside the Hub when its
charter excludes generated build directories.
Read unfamiliar build scripts
because compilation can execute host code.
Cross-compilation and execution on the
target establish different observations.

## Worked import task

Suppose a command imports records but
currently accepts duplicate identifiers.
Define uniqueness after the documented
normalization, including case and whitespace policy.
Preserve raw input for diagnostics while
constructing validated values separately.
Test identical identifiers and
identifiers colliding only after normalization.
Test an unrelated invalid field to ensure
duplicate detection does not mask parsing failures.
Use a recording storage fake to
show rejection causes zero writes.
Include a valid two-record example
to guard against rejecting everything.
Check whether the command adapter
preserves the domain diagnostic code.
If storage writes multiple records, identify the
transaction boundary and partial-write behavior.
Make the test independent of a live
service so a failure localizes to this contract.

## Decisions and tradeoffs

A local pure function is adequate for one
validation rule; a trait needs a substitution seam.
A private module is usually cheaper than a
new crate without a dependency-direction reason.
Explain dependency changes separately because
they alter reproducibility and supply-chain exposure.
Keep in-memory predicates
synchronous even when their callers use async.
Document reversible assumptions near the
implementation and complete independent work.
Resolve ambiguity before a transformation
changes the meaning of persisted records.
Keep product semantics distinct from compiler
complaints; fixing one does not decide the other.
Choose a test layer from the failure
mechanism rather than a universal checklist.

## Validation and handoff

Record package, features, command, exit
code, executed tests, and relevant warnings.
Explain which invariant each test
exercises instead of listing incidental assertions.
Name untested platforms and
external services explicitly.
Return a minimal reproduction when an
environment or compiler issue blocks implementation.
Tie the next action to the remaining
uncertainty, such as a consumer fixture.
Preserve the previous source
identity for reproduction of the comparison.
Do not describe an older receipt as current
evidence without rerunning its relevant check.
A useful handoff lets the next developer
continue without reconstructing terminal history.

## Limit

This workflow establishes bounded
engineering evidence, not product or release approval.
A passing baseline covers only the
observed configuration and tested inputs.
The current task's authorization governs
which writes and external actions are permitted.
