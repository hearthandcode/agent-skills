# Haskell, Lean, Idris orientation and non-equivalence

## Purpose

Transfer useful design ideas without
claiming the languages have identical guarantees.
Use this reference when discussing algebraic data,
totality, proofs, effects, or dependent types in Rust.
The engineering objective is to choose an
appropriate mechanism for a named obligation.

## Source posture

[Lean reference](https://lean-lang.org/doc/reference/latest/Introduction/) introduces Lean's language and proving environment.
[Rust traits](https://doc.rust-lang.org/reference/items/traits.html) defines Rust trait capabilities.
[Haskell report](https://www.haskell.org/onlinereport/haskell2010/) is a language source, not a Rust extension.
[Idris documentation](https://docs.idris-lang.org/en/latest/) describes Idris concepts.
The comparison below is design orientation;
validate any concrete cross-language bridge independently.

## Practice

Write the property in plain language
before selecting a type or proof mechanism.
Separate structural well-formedness, arithmetic
truth, termination, effects, and authorization.
Use ordinary Rust enums for closed alternatives without
importing another language's terminology unnecessarily.
Use traits for behavioral interfaces while
remembering that laws may remain unverified.
Treat a Rust Result return as explicit
failure handling rather than proof of totality.
Treat an iterator pipeline as an implementation whose
allocation and evaluation behavior still needs inspection.
Document evaluation strategy
assumptions when adapting a lazy-language design.
Keep formal proof artifacts connected to the
implementation they are intended to describe.

## Comparison by obligation

For “identifier classes cannot mix,” a Rust
newtype is a straightforward representation.
For “only checked values expose this method,” a
private checked type or typestate may suffice.
For “every input terminates,” ordinary Rust type
checking does not establish the requested property.
For “this arithmetic theorem follows,” use a
proof system with named definitions and assumptions.
For “this remote command is allowed now,” use
an authenticated runtime authorization decision.
For “effects cannot occur in this projection,”
restrict its dependencies and test the execution boundary.
For “this function satisfies a monoid
law,” test the law or provide a separate proof.
Choose the cheapest mechanism that actually covers
the obligation rather than the most elaborate notation.

## Worked proof boundary

Suppose a queue capacity calculation
must never exceed an allocation budget.
Implement checked arithmetic and
boundary tests in Rust for the runtime inputs.
A Lean theorem could separately establish an
arithmetic implication under explicit assumptions.
The theorem does not prove that the Rust
parser supplies values satisfying those assumptions.
Bind the source revision, translated definitions,
theorem identity, and verifier version in the evidence record.
Test the adapter with an altered source digest and an omitted assumption.
Reject a successful-looking certificate if the
verifier or source binding cannot be established.
Keep the runtime budget check even when
proof coverage excludes part of the input path.

## Translation hazards

Do not identify similarly named type classes and
traits without comparing coherence and dispatch behavior.
Do not equate Rust lifetimes with
dependent proofs about arbitrary runtime values.
Do not equate lack of a mutable variable
with absence of I/O or hidden shared state.
Do not assume compiler-generated code inherits
properties of a mathematical specification automatically.
Describe every normalization and representational loss in a translation.
Keep equality of serialized text
separate from equality in a formal theory.
Treat axioms, admitted holes, and trusted
plugins as part of the proof's assumptions.
Avoid describing a proof assistant result as
evidence about human intention or accepted terminology.

## Review procedure

Ask which concrete failure the stronger technique prevents.
Identify the checker, its input
language, its output, and the trusted boundary.
Distinguish a proof term from a report saying a check succeeded.
Check whether theorem names resolve in the pinned environment.
Inspect whether the bridge verifies
evidence or merely trusts a declared result.
Prefer a small end-to-end case over a
broad list of formal-language features.
Document the behavior when a proof tool is unavailable or times out.
Keep ordinary development available for tasks
that do not require the stronger obligation.

## Validation

Use positive and negative bridge fixtures,
including stale source and mismatched predicate.
Reproduce the exact verifier invocation when claiming a checked theorem.
Compile the Rust consumer independently from validating its certificate.
Preserve both outputs so a reviewer
can see where each guarantee originates.
Include one counterexample showing what the proof does not cover.
Do not turn the comparison itself into a claim of semantic equivalence.

## Limit

This reference proposes careful
technique selection, not a Rust theorem prover.
Formal acceptance, application correctness,
and human approval remain different judgments.
Do not advertise a bridge as implemented until its
actual verifier and consumer have been exercised.
