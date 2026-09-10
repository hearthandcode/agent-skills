# Error taxonomy and diagnostics

## Purpose

Make failures actionable for both callers and people.
Use this note when introducing errors, translating
adapter failures, or designing machine-readable diagnostics.
The error contract should preserve cause and
recovery meaning without exposing sensitive data.

## Source posture

[Error](https://doc.rust-lang.org/std/error/trait.Error.html) documents standard error chaining.
[Result](https://doc.rust-lang.org/std/result/) documents recoverable result handling.
The taxonomy below is a design recommendation;
retain the application's established error vocabulary.
Do not convert a domain rejection into a panic
merely because the successful path is simpler.

## Practice

Use typed variants when callers need
to choose different recovery actions.
Keep stable public codes independent of human-readable wording.
Preserve the underlying source error where
useful without leaking it directly across a boundary.
Distinguish malformed input, unsupported version, missing
data, conflict, unavailable dependency, and unknown outcome.
Attach context where the operation meaning is known.
Avoid repeatedly wrapping errors
with identical generic messages.
Use Option for ordinary absence only when
absence is not itself a reportable failure.
Keep retryability tied to operation
semantics, not merely an HTTP or I/O category.

## Worked conflict diagnostic

Suppose an update expects revision 4
but storage currently contains revision 5.
Return a conflict containing the expected and
observed revision where disclosure is permitted.
Give the public adapter a stable conflict code.
Explain that the caller should
reload before attempting a new decision.
Do not automatically retry with revision 5 because
that would change the user's intended precondition.
Keep the original request identity in the trace.
Test that the adapter preserves conflict rather
than translating every failure to internal error.
Ensure logs do not include the full protected record.
A conflict is an expected concurrency
outcome, not necessarily an implementation defect.

## Error implementation

Implement Display for a concise message and
Error for causal chaining when appropriate.
Use a derivation library only if it is already
suitable for the package's dependency policy.
Keep domain errors free of transport-specific
status codes where multiple adapters consume them.
At the boundary, map each
relevant domain category deliberately.
Avoid exposing debug formatting as a stable external protocol.
Document whether errors own strings,
retain references, or capture costly backtraces.
Preserve non-UTF-8 path information internally
when relevant rather than corrupting it for display.
Bound diagnostic payload size
when input can control its content.

## Panic policy

Reserve panic for violated internal
assumptions where the project permits it.
Use Result for malformed external
input and expected resource failure.
Do not catch panics as a universal
substitute for a correct error API.
Define behavior at FFI and process
boundaries where unwinding has special constraints.
Avoid unwrap in production input paths unless
the preceding invariant is local and convincing.
An expect message should explain the invariant
rather than merely restate the failed operation.
Review destructors for panics during cleanup.
Keep test-only assertions clearly
separated from user-input handling.

## Retry and cancellation

Classify timeout separately from a
proven failure of the external operation.
A lost response can leave completion
unknown even when the client receives an error.
Retry only when idempotency or non-dispatch is established.
Represent cancellation as an
outcome with its own state consequences.
Preserve enough attempt identity to reconcile late replies.
Do not hide partial progress
behind a generic cancelled message.
Give users a concrete recovery route
when automatic retry would be unsafe.

## Validation

Test every externally meaningful error mapping.
Assert codes and structured fields rather than
brittle full prose where wording is not contractual.
Exercise source chaining with a
representative underlying error.
Test redaction using synthetic sensitive-looking values.
Check malformed Unicode, long paths,
and oversized messages where applicable.
Verify that failure leaves the documented
state unchanged or records partial progress.
Include a successful path to guard against overbroad rejection.
Review documentation examples for actual recovery behavior.

## Limit

A detailed diagnostic does not
prove its interpretation is correct.
A retryable label cannot guarantee
that a repeated external effect is safe.
Error handling must be checked together
with the operation's state and side effects.
