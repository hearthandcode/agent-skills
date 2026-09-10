# Ownership, borrowing, lifetimes, and drop

## Purpose

Choose ownership around the lifetime
of the data and the operation using it.
Use this note when borrow errors, reference counting,
interior mutability, or cleanup complicate a design.
The desired outcome is a clear owner, a bounded
borrow, and an explicit resource-release path.

## Source posture

[Ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html) introduces moves and ownership.
[Destructors](https://doc.rust-lang.org/reference/destructors.html) documents drop scopes.
[Arc](https://doc.rust-lang.org/std/sync/struct.Arc.html) documents shared ownership.
[Pin](https://doc.rust-lang.org/std/pin/index.html) defines address-stability contracts.
The design procedures here are recommendations
to test against the actual resource lifecycle.

## Practice

Identify the component responsible for creating,
retaining, and releasing each allocation or resource.
Borrow for a short inspection and move when
responsibility transfers to a longer-lived owner.
Prefer slices and str views when a
callee only reads contiguous data.
Use owned values across detached lifetime
boundaries unless a scoped API proves borrowing is valid.
Do not add static lifetimes to silence a borrow
error; investigate the required lifetime relationship.
Use clone when a real independent owned
copy is intended and its cost is acceptable.
Use Arc for shared ownership, remembering that it
does not make arbitrary inner mutation thread-safe.
Break reference-count cycles with an
ownership redesign or suitable weak references.

## Worked borrow boundary

A returned view must remain tied to the owner's lifetime.

```rust
fn first_line(text: &str) -> &str {
    text.lines().next().unwrap_or("")
}
fn main() {
    let document = String::from("alpha\nbeta");
    let line = first_line(&document);
    assert_eq!(line, "alpha");
}
```

Returning a slice into a locally created String
would be invalid because that owner is dropped.
If the caller must retain the line after releasing
the document, return an owned String deliberately.
Avoid keeping a tiny slice alive through a huge
retained buffer when copying would reduce memory pressure.

## Borrow-error diagnosis

Read which borrow conflicts, where it
starts, and where its last use occurs.
Shorten the borrow by extracting an
owned key or a small immutable result.
Split unrelated fields or operations when one
broad mutable borrow prevents independent access.
Do not replace every borrow with RefCell
merely to defer a design problem until runtime.
Use an index or stable identifier when
self-references would otherwise
complicate movable structures.
Check iterator lifetime retention
before mutating a collection being traversed.
Separate lookup from mutation when holding a
reference across insertion would invalidate assumptions.
Explain any remaining clone as snapshot,
ownership transfer, caching, or boundary conversion.

## Resources and destruction

Use RAII guards for ordinary cleanup while
documenting that abrupt process termination can bypass it.
Provide explicit fallible close or commit
operations when failure must be reported.
Keep Drop implementations short and avoid
relying on them for essential remote effects.
Define behavior when a mutex is poisoned instead of
silently assuming the protected invariant survives.
Ensure a failed constructor
releases resources already acquired.
Order fields or explicit shutdown carefully when
one resource depends on another during cleanup.
For async resources, offer an awaited shutdown path
because Drop cannot perform ordinary async waiting.
Treat mem::forget and reference cycles as reasons not
to base memory safety on guaranteed destructor execution.

## Validation

Test ownership transfer through the public
caller rather than an artificial helper alone.
Exercise early returns, parse failures,
cancellation, and explicit close errors.
Use counters or recording fakes to
check balanced acquisition and release.
Check that long-lived caches do not retain
unexpectedly large owners through small views.
Use Miri when supported to examine
unsafe aliasing or lifetime-sensitive code.
Review lock lifetimes around
await points and blocking operations.
Test weak-reference upgrade
failure as a normal lifecycle case.
Compile lifetime examples without relaxing
them to static or adding unnecessary allocation.

## Limit

Borrow checking prevents specific invalid reference
patterns in safe Rust, not logical resource leaks.
Pinning is an address-stability contract and does
not automatically solve self-referential design.
A memory-safe shutdown can still lose
application data unless
persistence semantics are explicit.
