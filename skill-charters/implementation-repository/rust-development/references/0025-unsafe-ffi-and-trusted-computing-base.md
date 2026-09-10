# Unsafe, FFI, and trusted computing base

## Purpose

Keep unsafe obligations explicit
and the public safe interface sound.
Use this note when raw pointers, foreign functions,
custom synchronization, or layout assumptions appear.
The result should identify every invariant
the compiler cannot check and who maintains it.

## Source posture

[Undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) lists important forbidden behavior.
[The Rustonomicon](https://doc.rust-lang.org/nomicon/) provides unsafe-programming context.
[Miri](https://github.com/rust-lang/miri) documents an interpreter for detecting classes of undefined behavior.
Read the specific unsafe API
documentation before relying on an invariant.

## Practice

Prefer a safe implementation when it
satisfies the measured requirement.
Keep unsafe blocks as small as
practical and explain the local safety argument.
Separate caller obligations on unsafe
functions from implementation obligations inside them.
Do not treat successful compilation
as evidence that unsafe code is sound.
Validate lengths, alignment, initialization,
lifetime, aliasing, and ownership as applicable.
Keep raw representations separate from validated safe types.
Minimize the dependencies and helper
functions included in the trusted boundary.
Document the safe facade's
behavior on malformed external input.

## Worked FFI buffer review

Suppose foreign code returns a pointer and length.
Determine who owns the allocation
and which function must release it.
Check whether null is allowed for an empty
buffer and what the called Rust API requires.
Establish that the pointer is aligned,
initialized, and valid for the complete length.
Check that the length does not
overflow address calculations.
Ensure no concurrent mutation violates
the reference type being constructed.
Tie the resulting borrow to an
owner that keeps the allocation alive.
Copy into owned Rust storage if a safe
lifetime cannot otherwise be represented.
Do not construct a slice merely
because the foreign call reported success.

## Layout and ABI

Use an explicitly appropriate
representation for types crossing the ABI.
Do not assume ordinary Rust
struct layout matches a C struct.
Verify enum and boolean validity
before interpreting arbitrary foreign bytes.
Keep allocation and deallocation
within compatible allocator ownership.
Specify calling convention and symbol naming.
Define panic and exception behavior across the boundary.
Avoid unwinding across an ABI that does not permit it.
Document target-specific size and alignment assumptions.
Treat packed fields carefully because
creating an unaligned reference can be invalid.

## Safe facade review

Check every public safe method for a
path violating an unsafe invariant.
Review Clone, Drop, Send, and Sync implementations together.
Ensure partially initialized values
cannot be dropped as fully initialized values.
Do not expose mutable access that
invalidates cached raw pointers.
Keep callback lifetimes and reentrancy assumptions explicit.
Handle foreign callbacks after shutdown
according to a defined ownership protocol.
Do not rely on Drop always running to preserve memory safety.
Document any intentional leak as a
resource decision rather than hiding it.

## Validation

Exercise the safe interface with
normal, empty, boundary, and malformed inputs.
Use Miri on supported paths to detect
relevant aliasing or initialization defects.
Use sanitizers or target-specific tools
where they cover behavior Miri cannot execute.
Test allocation failure or partial
initialization when the API can encounter it.
Check cross-language ownership with a minimal foreign caller.
Review safety arguments independently from the tests.
Record unsupported foreign calls or interpreter limitations.
Retain a focused regression case for every discovered defect.

## Maintenance

Keep an unsafe ledger naming location,
invariant, owner, tests, and removal condition.
Revisit the argument when surrounding safe code changes.
Review dependency upgrades that alter
layout, callbacks, or allocation behavior.
Avoid blanket unsafe impls whose bounds
are weaker than the inner type requires.
Explain why an optimization needs
unsafe and the measured benefit.
Prefer shrinking the unsafe
surface over adding broad suppression.
Keep safety comments factual and tied to the exact operation.

## Limit

Passing Miri or sanitizers does
not prove all executions sound.
A safe facade can be unsound if its
hidden invariant argument is wrong.
Unsafe correctness and application
authorization are separate obligations.
