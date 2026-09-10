# Const generics, refinement, and type-level limits

## Purpose

Use compile-time constants where fixed
shape improves correctness or performance.
Use this note for buffers, dimensions,
bounded integers, and claims about refinement types.
Separate fixed-size representation from
value predicates that require runtime validation.

## Source posture

[Generic parameters](https://doc.rust-lang.org/reference/items/generics.html) documents const parameters.
[Constant evaluation](https://doc.rust-lang.org/reference/const_eval.html) documents const contexts.
The suggested modeling choices are recommendations
and must compile on the project's minimum toolchain.
Do not describe unstable generic-constant
expressions as a portable stable-Rust capability.

## Practice

Use a const parameter when callers
genuinely need distinct compile-time sizes.
Prefer slices when length varies at
runtime and no fixed-size API benefit exists.
Validate runtime lengths before
converting into a fixed-size representation.
Keep units explicit through newtypes; equal numeric
representation does not
imply interchangeable dimensions.
Use checked runtime predicates for ranges,
relationships, and externally supplied values.
Do not encode every configuration value in a type
because it increases API and compilation complexity.
Document whether zero-sized dimensions
are legal and what operations mean for them.
Separate storage capacity from the
current number of populated elements.

## Worked fixed shape

This example accepts only an array
with the selected compile-time size.

```rust
struct Frame<const N: usize> { bytes: [u8; N] }
impl<const N: usize> Frame<N> {
    fn new(bytes: [u8; N]) -> Self { Self { bytes } }
    fn len(&self) -> usize { self.bytes.len() }
}
fn main() {
    let frame = Frame::<4>::new([1, 2, 3, 4]);
    assert_eq!(frame.len(), 4);
}
```

The type records four bytes but says nothing
about checksum validity or their domain meaning.
An input slice of unknown length needs a
checked conversion before constructing this frame.
If the length comes from untrusted input, enforce
an allocation limit before materializing a buffer.

## Refinement decisions

A private positive-integer wrapper can
establish positivity through a checked constructor.
A compile-time dimension cannot
prove that a matrix is invertible.
A sorted-vector wrapper needs validation
and mutation methods preserving ordering.
A nonempty collection type needs a defined consuming
operation that cannot silently erase its invariant.
Keep predicates executable and named
so tests can target their boundaries.
Avoid claiming theorem-level refinement
from a comment or a phantom parameter alone.
If an external checker establishes a property, bind
its evidence to the exact value or source identity.
Reject stale evidence when
normalization changes the value being certified.

## Arithmetic and portability

Check integer conversion when
moving between protocol widths and usize.
Test maximum values before
multiplication used for allocation sizes.
Use checked multiplication for rows times
columns before allocating image or matrix storage.
Specify overflow behavior explicitly
instead of relying on profile-dependent checks.
Do not assume machine-word width is
identical across supported targets.
Review const evaluation failures
separately from runtime validation errors.
Avoid panicking public constructors
for invalid user-supplied lengths.
Keep large arrays off constrained
stacks when the allocation strategy matters.

## Validation

Compile at least two supported
sizes and a wrong-size negative example.
Test zero, one, maximum accepted length,
and one beyond the configured boundary.
Verify shape conversions do not truncate or pad silently.
Run arithmetic tests on relevant
target widths when portability is promised.
Benchmark specialization only if
it addresses a measured workload.
Check compile-time cost when many const
instantiations materially affect build time.
Document all predicates still checked at runtime.
Test mutating APIs after
construction, not just the initial constructor.

## Limit

Const generics provide parameterized
shape, not unrestricted dependent typing.
Fixed length does not establish
authentication, semantic
correctness, or current permission.
A stronger mathematical property needs a
stated proof mechanism and trusted assumptions.
