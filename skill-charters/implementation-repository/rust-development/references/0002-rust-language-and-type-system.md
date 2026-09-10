# Rust language and type system

## Purpose

Choose types that expose constraints
without overstating compiler guarantees.
Use this note for identifiers, checked
values, conversions, and public function signatures.
Separate representable states, admissible
runtime values, and external authorization.

## Source posture

[The Rust Reference](https://doc.rust-lang.org/reference/) documents stable language semantics.
[TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html) documents fallible conversion.
Modeling choices below are
recommendations rather than language requirements.
Compile version-sensitive techniques with
the package's minimum supported compiler.

## Practice

Use newtypes for identifiers that share
storage representation but are not interchangeable.
Keep invariant-bearing fields private and
validate construction through an explicit API.
Use fallible conversion when some inputs are
invalid and infallible conversion only for total mappings.
Choose enums for alternatives and
structs for simultaneously meaningful fields.
Use Option only when absence has one
meaning; distinct failure reasons deserve variants.
Select integer widths from protocol and
storage contracts, not the host architecture.
Use checked arithmetic when overflow is a recoverable boundary case.
Keep wire types separate when
validation requires contextual information.

## Worked checked value

This standalone example rejects zero
before constructing the domain value.

```rust
#[derive(Debug, PartialEq, Eq)]
struct Count(u32);
impl TryFrom<u32> for Count {
    type Error = &'static str;
    fn try_from(raw: u32) -> Result<Self, Self::Error> {
        if raw == 0 { Err("positive count required") }
        else { Ok(Self(raw)) }
    }
}
fn main() {
    assert!(Count::try_from(0).is_err());
    assert_eq!(Count::try_from(3), Ok(Count(3)));
}
```

Privacy constrains external callers; the
defining module still carries the invariant obligation.
Derived deserialization needs a checked conversion
path if ordinary decoding would bypass construction.
Test the actual wire-to-domain admission
path as well as direct constructor calls.

## Type relationships

A type alias changes naming but does
not create a distinct nominal type.
A generic parameter selects a member of a family of implementations.
An associated type records a related
type selected by an implementation.
A trait bound exposes operations without proving
the informal laws those operations should satisfy.
Lifetimes constrain references without
extending the lifetime of their underlying allocation.
An owned String and a borrowed str slice
assign allocation responsibility differently.
A normalizing conversion can lose spelling or
formatting, so document its round-trip behavior.
Avoid Deref on a domain wrapper if it exposes
operations that undermine the wrapper's contract.

## Boundary failures

Test zero, largest accepted value, oversized
textual input, and invalid sign as applicable.
Check whether normalization changes
identity lookup or digest computation.
Replace lossy numeric casts at boundaries
with checked conversion and explicit errors.
Define NaN, infinity, and signed-zero policy
before using floats in identity or ordering.
Do not default missing fields to zero
when missing and zero mean different things.
Keep equality and hashing
consistent when implementing them manually.
List alternative construction routes through
FFI, migration, persistence, and test helpers.
Inspect public mutation methods for ways to
violate a constructor-established invariant.

## Validation

Compile valid construction and run boundary-value assertions.
Use a downstream module or crate to test
that private construction is unavailable.
Ensure a compile-fail example fails for
the intended reason, not a missing import.
Check deserialization rejection separately from Rust type checking.
Use property tests where interacting numeric or
normalization cases exceed a small example set.
Exercise mutation after
construction to confirm invariant preservation.
Document any unsafe escape hatch as
part of the trusted implementation.
Record target-width assumptions when
converting between usize and protocol integers.

## Limit

A checked count does not establish
current inventory or permission to consume it.
Time-sensitive facts can expire after
construction and require checks at the effect boundary.
State the dynamic checks that remain
outside the Rust type-level contract.
