# Traits, generics, GATs, and associated types

## Purpose

Choose abstraction mechanisms from
actual substitution and borrowing needs.
Use this note before introducing traits,
GATs, blanket implementations, or trait objects.
An abstraction should reduce coupling while
preserving visible ownership and error behavior.

## Source posture

[Traits](https://doc.rust-lang.org/reference/items/traits.html) documents dyn compatibility.
[Associated items](https://doc.rust-lang.org/reference/items/associated-items.html) documents GAT bounds.
The API choices below are
recommendations, not universal requirements.
Compile proposed interfaces on the
declared minimum compiler with an actual consumer.

## Practice

Start concrete until a second implementation
or testing boundary justifies substitution.
Place bounds on the method that needs
them rather than the entire container.
Use associated types when each
implementation selects one related type.
Use generic trait parameters when distinct
parameterized implementations are meaningful.
Prefer static dispatch when
runtime heterogeneity is unnecessary.
Choose dyn dispatch when runtime
selection justifies indirection.
Document borrowing, mutation,
consumption, allocation, blocking, and I/O behavior.
Keep a domain port narrow enough that a
fake implements only relevant operations.

## Worked lending interface

The output type below depends on the lifetime of the borrow.

```rust
trait View {
    type Item<'a> where Self: 'a;
    fn view<'a>(&'a self) -> Self::Item<'a>;
}
struct Text(String);
impl View for Text {
    type Item<'a> = &'a str where Self: 'a;
    fn view<'a>(&'a self) -> Self::Item<'a> {
        &self.0
    }
}
fn main() {
    let text = Text("bounded".into());
    assert_eq!(text.view(), "bounded");
}
```

A GAT describes a family of associated types;
it does not provide unrestricted dependent types.
A plain borrowed return is simpler if every
implementation exposes exactly the same view type.

## Dynamic and async interfaces

Check dyn compatibility before
promising heterogeneous trait-object storage.
Do not assume generic methods or
generic associated types work through dyn.
Separate Self: Sized construction
methods from dynamically dispatched operations.
For async ports, decide whether callers
require a Send future and express that in the API.
Native async trait syntax alone does not settle
dynamic-dispatch or future-bound requirements.
If boxing futures, document allocation and lifetime costs.
Use the repository's established async style
unless a concrete limitation requires another.
Verify cancellation behavior of the
implementation rather than assuming the trait implies it.

## Coherence and evolution

Inspect blanket implementations for
overlap before adding broad new ones.
Use a local wrapper when orphan
rules prevent a foreign integration.
Seal a trait when external implementations
would break invariants, not merely from habit.
Adding required methods can break downstream
implementations even when local callers compile.
Default methods preserve some source
compatibility while still changing behavior.
Avoid exposing private implementation
details through associated public types.
Treat Send, Sync, and lifetime
bounds as compatibility commitments.
Keep abstraction names tied to consumer
operations rather than implementation technology.

## Validation

Compile two meaningful implementations
and a consumer using only the port surface.
Include a negative lifetime or
unsupported trait-object example.
Check whether a fake reproduces the
error semantics needed by the domain.
Inspect public docs for ownership and
cost information missing from signatures.
Measure dispatch or code-size costs only
when the application has a relevant budget.
Test minimum compiler and supported feature configurations.
Review each parameter against a concrete consumer need.
Avoid claiming object safety from one
monomorphized example that never constructs dyn.

## Limit

Informal trait laws remain
obligations for implementers and tests.
Successful compilation cannot establish
remote-service or transaction correctness.
Attach formal guarantees to their
separately defined checker and trust assumptions.
