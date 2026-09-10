# Game, desktop, harness, and general application patterns

## Purpose

Keep domain rules testable across
event loops and application adapters.
Use this note when Rust logic serves a
game, desktop shell, CLI, or agent harness.
The architecture should let the same rule be
exercised headlessly without reproducing the entire UI.

## Source posture

[Standard threads](https://doc.rust-lang.org/std/thread/) documents thread behavior.
[Channels](https://doc.rust-lang.org/std/sync/mpsc/) documents one standard message-passing option.
Framework APIs must be checked against
the application's actual locked versions.
The patterns below are recommendations, not a
requirement to adopt a
specific engine or desktop framework.

## Practice

Keep rendering and input
translation outside pure domain transitions.
Represent user actions as
explicit commands with validated data.
Let the domain return outcomes
that adapters render or persist.
Keep clocks, randomness, and external
I/O injectable where determinism matters.
Do not call the event loop
recursively to hide a long-running operation.
Bound work performed on UI or simulation threads.
Separate persistent identity from
temporary widget or entity handles.
Define cancellation when a view closes or a session ends.

## Worked headless transition

Suppose a desktop and CLI both edit a project record.
Each adapter parses its input
into the same domain command.
The domain validates the expected
revision and returns a change or conflict.
The storage adapter commits the
accepted change transactionally.
The desktop displays the result and
the CLI selects a documented exit status.
A headless test exercises the
domain with a recording storage boundary.
Adapter tests check input mapping and error presentation.
Neither adapter implements
its own divergent revision rule.
A shared data type alone is insufficient
if the adapters still duplicate semantics.

## Game and simulation choices

Separate simulation time from
wall-clock time when replay matters.
Use a seeded random source for
reproducible simulation tests.
Record external inputs needed to replay a session.
Keep rendering interpolation separate
from authoritative simulation state.
Do not assume deterministic behavior across platforms
without testing relevant numeric and scheduling choices.
Treat asset loading failures as defined outcomes.
Avoid storing raw engine handles in durable domain records.
Measure frame-time budgets
around the actual work performed.

## Desktop and CLI choices

Keep long-running work off the UI thread
through the framework's supported mechanism.
Report progress with stable operation identity.
Do not equate closing a progress
dialog with confirmed task cancellation.
Use explicit file-access and command boundaries.
Keep CLI output modes separate for
human text and machine-readable records.
Use exit codes consistently for expected failure classes.
Test without a graphical display
when the core behavior allows it.
Exercise real platform integration
before claiming native feature support.

## Harness choices

Represent attempt identity and lifecycle explicitly.
Keep task input distinct from
permission to perform an external action.
Validate worker output before
accepting it into domain state.
Define timeout, cancellation,
retry, and unknown-result handling.
Record durable progress before
releasing ownership when recovery requires it.
Do not infer completion from a process exit alone.
Keep a presentation record unable to
masquerade as an execution request.
Use bounded messages and queues to
prevent uncontrolled accumulation.

## Validation

Test pure transitions with deterministic inputs.
Test each adapter's accepted and rejected mapping.
Exercise shutdown while work is in progress.
Test missing resources and malformed worker replies.
Check that stale UI state
cannot overwrite newer durable state.
Run platform-specific tests only
for supported claimed behavior.
Measure event-loop responsiveness
under a representative workload.
Record which layers were tested headlessly and
which were exercised in the actual application.

## Limit

Headless success does not establish UI
accessibility or native platform behavior.
Shared types do not guarantee shared semantics.
An event-driven architecture still needs
explicit ownership, persistence, and recovery contracts.
