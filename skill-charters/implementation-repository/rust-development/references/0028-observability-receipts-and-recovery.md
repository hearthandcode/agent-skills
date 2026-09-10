# Observability, receipts, and recovery

## Purpose

Make failures and interrupted work
reconstructible without leaking private data.
Use this note when adding logs, traces,
metrics, or durable operation receipts.
The output should explain what happened,
what remains unknown, and how recovery proceeds.

## Source posture

[Tracing](https://docs.rs/tracing/latest/tracing/) documents structured instrumentation.
[Instant](https://doc.rust-lang.org/std/time/struct.Instant.html) documents monotonic timing.
Local historical VALIDATION-RECEIPT.md
illustrates a bounded process report.
The recovery design below is a recommendation
that must align with the actual persistence contract.

## Practice

Assign stable request and attempt
identities before consequential work.
Use structured fields for machine
correlation rather than parsing prose messages.
Record state transitions at the component that owns them.
Keep observation timestamps
distinct from source-event timestamps.
Use monotonic elapsed timing for durations within one process.
Avoid logging raw payloads merely
because structured fields are convenient.
Bound message size and retention.
Separate an observed event from a claimed durable result.

## Worked uncertain outcome

Suppose a worker dispatches a command
and the connection drops before its reply.
Record the dispatch identity and the last confirmed state.
Mark completion unknown rather than
treating timeout as a proven failure.
Query the operation's durable status
if the protocol supports reconciliation.
Reuse the same identity when a safe
idempotent retry is explicitly supported.
Do not generate a fresh identity
that could duplicate the effect.
Record a late completion against the original attempt.
Expose the unresolved state to the
operator with a concrete recovery route.
Keep the diagnostic free of
credentials and full private request bodies.

## Trace design

Use spans for bounded operations with
meaningful parent-child relationships.
Record domain identifiers only
when their disclosure is appropriate.
Avoid high-cardinality metric
labels such as arbitrary request IDs.
Put detailed correlation in traces
while keeping metrics aggregatable.
Instrument queue wait separately from
service time when diagnosing latency.
Record error category and retry decision separately.
Avoid creating a success span
result before persistence commits.
Keep cancellation visible even when
no error is returned to the caller.

## Receipt design

Name the checked predicate, source
revision, command or operation, and observed result.
Record exit status rather than
inferring success from the last output line.
Distinguish skipped, unavailable, failed, and passed checks.
Keep historical results dated and
attached to their original source identity.
Do not let a receipt authorize the next effect automatically.
Store enough context to reproduce the claim
without copying private source material unnecessarily.
Include limitations that materially affect interpretation.
Use an append or revision model
when receipts form operational history.

## Recovery states

Define the last safe restart point before implementation.
Distinguish not-started, running, completed, failed,
cancelled, and indeterminate where behavior differs.
Check current durable state
before replaying work after restart.
Prevent stale completions from overwriting newer attempts.
Use transactional state changes or
compare-and-swap where concurrency requires them.
Treat cleanup failure as observable
state when it matters to subsequent work.
Keep rollback narrow and
preserve evidence of the failed attempt.
Do not promise exact recovery if
external effects lack reconciliation support.

## Validation

Test failure before dispatch, after
dispatch, and after commit but before reply.
Check that attempt IDs survive the adapter boundary.
Exercise late replies and duplicate completion messages.
Inspect logs with synthetic
secret-like values to verify redaction.
Test that metrics remain bounded under many distinct requests.
Reconstruct one failed attempt using only
its stored receipt and allowed diagnostics.
Verify historical results are not displayed as fresh checks.
Record recovery behavior that
depends on untested external services.

## Limit

Logs can be incomplete or lost and
are not automatically a durable ledger.
A receipt proves only its recorded
observation and trusted provenance.
Observability does not supply
authorization or exactly-once semantics.
