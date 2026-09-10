# Concurrency, async, cancellation, and backpressure

## Purpose

Make ownership and progress explicit
when several operations can overlap.
Use this reference for async tasks, shared
state, channels, cancellation, and shutdown.
The design should define who owns each task
and what happens when work cannot complete.

## Source posture

[Tokio select](https://tokio.rs/tokio/tutorial/select) explains branch cancellation behavior.
[Send](https://doc.rust-lang.org/std/marker/trait.Send.html) documents transfer between threads.
[Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html) documents shared ownership.
Runtime-specific behavior must be checked
against the project's locked runtime version.

## Practice

Identify the owner that starts,
observes, and finishes every spawned task.
Bound queues and state the policy for
overload: wait, reject, shed, or coalesce.
Keep blocking I/O and expensive CPU work away from
executor threads unless the runtime provides an appropriate path.
Do not hold a lock across await without a
deliberate reason and compatible lock semantics.
Use message passing when it clarifies
ownership better than shared mutation.
Keep critical sections small and avoid
calling unknown user code while holding a lock.
Treat timeout as a local waiting
outcome, not proof that remote work stopped.
Define shutdown ordering before
adding detached background activity.

## Worked cancellable import

Suppose an import reads chunks,
validates them, and writes a transaction.
Cancellation before the transaction
begins can return without durable changes.
Cancellation during a write needs an
explicit rollback or completion policy.
If commit may already have happened,
report an unknown outcome until reconciled.
Keep the attempt ID so a late
completion can be matched to the request.
Bound the number of buffered chunks to prevent producer overload.
Check cancellation between bounded
units of work rather than only at the end.
Test a slow consumer and a closed channel.
Do not restart the import automatically unless
duplicate effects are prevented by the contract.

## Shared-state decisions

Arc shares ownership but does not make an
arbitrary inner value safe for concurrent mutation.
Use synchronization suited to the
access pattern and measured contention.
A read-write lock is not automatically faster than a mutex.
Keep atomic ordering arguments close to the invariant they protect.
Prefer a mutex over an ad hoc atomic
protocol when it is simpler and adequate.
Review poisoning behavior rather than
blindly unwrapping lock acquisition.
Avoid retaining a guard through a
callback that can reenter the same component.
Document whether clones observe a snapshot or live shared state.

## Cancellation safety

Inspect each awaited operation for
what happens if its future is dropped.
A select loop can repeatedly cancel losing branches.
Preserve partial read or write progress
where dropping would lose framing state.
Separate cancellation request from
confirmation that the task has stopped.
Join or otherwise observe completion
before releasing resources the task uses.
Do not assume dropping a task handle
cancels the task for every runtime API.
Test cancellation at different points,
including after an external dispatch.
Document operations that
intentionally finish despite caller cancellation.

## Backpressure and shutdown

Choose queue capacity from memory and latency budgets.
Expose overload as a defined result
instead of allowing unbounded growth.
Stop accepting new work before draining existing work.
Give graceful shutdown a deadline
and define the forced-stop outcome.
Flush essential state through explicit fallible operations.
Keep logging from blocking indefinitely during shutdown.
Report tasks that did not terminate
rather than silently abandoning them.
Preserve recovery metadata for
effects whose completion is uncertain.

## Validation

Use deterministic synchronization in tests
rather than arbitrary sleeps where possible.
Test producer overload, consumer exit, task
panic, cancellation, and deadline expiration.
Exercise duplicate and late replies.
Use Loom for small synchronization
algorithms when schedule exploration adds value.
Measure queue depth and latency under a representative workload.
Check that all started tasks have
an observation or supervision route.
Run platform-specific behavior where promised.
Record what shutdown and restart behavior remains untested.

## Limit

Memory safety does not guarantee deadlock
freedom, fairness, or exactly-once effects.
A cancelled future may leave external work running.
Async syntax alone does not make
blocking work concurrent or bounded.
