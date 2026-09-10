# Typestate, capabilities, and proof witnesses

## Purpose

Restrict operations when a small, stable
sequence of states makes illegal calls likely.
Use this reference for builder completion,
validated construction, or ownership-consuming transitions.
Prefer runtime state when persistence or dynamic
dispatch would make a typestate API cumbersome.

## Source posture

[PhantomData](https://doc.rust-lang.org/std/marker/struct.PhantomData.html) documents marker semantics.
[Visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html) defines construction boundaries.
Typestate is an engineering pattern built from
ordinary Rust, not a separate language guarantee.
The meaning of a witness depends on private
constructors and the checks they actually execute.

## Practice

Name the exact illegal operation before adding a state parameter.
Keep constructors for privileged states private to
the component performing the corresponding check.
Consume the earlier state when transition semantics invalidate it.
Avoid Clone on a consumable capability
unless duplication is explicitly valid.
Do not derive Deserialize for privileged
state in a way that bypasses validation.
Keep a runtime representation for storing
and reloading state with version checks.
Distinguish “checked structurally” from
“authorized now” when external permissions can change.
Make failure recovery explicit when a
consumed value cannot simply be reconstructed.

## Worked typestate

The checked state exposes output only after a nonempty-input check.

```rust
use std::marker::PhantomData;
struct Draft;
struct Checked;
struct Item<S> { text: String, state: PhantomData<S> }
impl Item<Draft> {
    fn new(text: String) -> Self {
        Self { text, state: PhantomData }
    }
    fn check(self) -> Result<Item<Checked>, Self> {
        if self.text.is_empty() { return Err(self); }
        Ok(Item { text: self.text, state: PhantomData })
    }
}
impl Item<Checked> {
    fn text(&self) -> &str { &self.text }
}
fn main() {
    let item = Item::<Draft>::new("candidate".into());
    let checked = item.check().ok().unwrap();
    assert_eq!(checked.text(), "candidate");
}
```

The example proves only that this
constructor rejected empty strings.
It does not establish human review, source
authenticity, or permission for an external action.

## Capability lifetime

Bind a capability to subject,
operation, target, and relevant revision.
If revocation is possible, recheck current
permission immediately before the consequential operation.
Represent expiration explicitly instead of
assuming a type parameter captures wall-clock time.
Do not serialize an in-memory
witness as an automatically trusted token.
If a token crosses a process boundary, define
authentication, replay policy, and audience checks.
Avoid storing secret-bearing
capabilities in debug output or general receipts.
Keep authorization failures
distinguishable from structural validation failures.

## Design alternatives

A runtime enum is simpler when callers need
homogeneous collections of different states.
A checked newtype is sufficient when
there is only one construction invariant.
A builder can encode required fields
without modeling an entire workflow lifecycle.
A transition table often reveals more
than multiplying phantom state parameters.
Do not duplicate independent review and
execution dimensions into dozens of artificial states.
Choose typestate where unavailable
methods improve actual consumer ergonomics.
Document which state transitions remain runtime checks and why.

## Validation

Compile an accepted sequence and a
downstream compile-fail call on the wrong state.
Test constructor bypass attempts through
public fields and conversion implementations.
Exercise failure paths and confirm the
original value remains recoverable where promised.
Check whether serialization can
manufacture a checked or privileged state.
Test revoked and stale
capabilities against the execution component.
Review Clone, Copy, Send, and Sync
behavior against capability semantics.
Use tests to prove the named check rather
than merely instantiate the marker types.

## Limit

A marker carries only the guarantees
established by its trusted constructors.
Process restart, concurrent revocation, and
remote effects require runtime coordination.
Typestate cannot turn a candidate
artifact into an approved decision.
