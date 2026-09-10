# Algebraic data types and pattern matching

## Purpose

Expose legal combinations and make
state transitions readable in ordinary Rust.
Use this note when booleans, optional
fields, and status strings conceal invalid states.
The model should make required payloads
available only where they are meaningful.

## Source posture

[Enums](https://doc.rust-lang.org/reference/items/enumerations.html) defines variant structure.
[Match](https://doc.rust-lang.org/reference/expressions/match-expr.html) defines matching behavior.
The transition design below is a
recommendation to test against the domain contract.
Exhaustiveness checks variant coverage,
not the business correctness of each branch.

## Practice

Replace status plus optional payloads with
variants containing the appropriate data.
Name states after observable domain
meaning rather than widget appearance.
Keep failure details in a failure variant
instead of beside a stale success result.
Distinguish queued, running, and
unknown outcome when recovery differs.
Match explicitly on internal closed enums
so new variants expose affected consumers.
Use wildcard fallbacks deliberately when
handling extensible external protocols.
Borrow while inspecting and consume only
when ownership transfer is intentional.
Keep classification pure so rejected
transitions do not hide side effects.

## Worked transition

The receipt exists only after the running state completes.

```rust
#[derive(Debug, PartialEq, Eq)]
enum Job {
    Queued,
    Running { attempt: u64 },
    Finished { receipt: String },
}
fn complete(job: Job, receipt: String) -> Result<Job, Job> {
    match job {
        Job::Running { .. } => Ok(Job::Finished { receipt }),
        other => Err(other),
    }
}
fn main() {
    assert!(complete(Job::Queued, "r1".into()).is_err());
    let job = Job::Running { attempt: 7 };
    assert!(matches!(complete(job, "r2".into()), Ok(Job::Finished { .. })));
}
```

Returning the original state makes rejection
recoverable without fabricating replacement data.
A durable implementation also checks
attempt identity to reject stale completions.

## Representation decisions

Use structs for facts that coexist and enums for alternatives.
A boolean is adequate for one independent
binary property, but weak for a lifecycle.
Avoid a giant Cartesian-product enum for
dimensions that can be checked independently.
Draft a transition table before
deciding which combinations belong in types.
Keep stable wire tags separate from internal naming changes.
Consider non-exhaustive public enums when
downstream matches should tolerate future variants.
Use runtime state when values must be
stored, loaded, or selected dynamically.
Use typestate only when restricting
method availability improves the real API.

## Pattern review

Inspect moves and borrows before
adding clone to satisfy a match.
Use guards for value predicates and
provide a path for values failing each guard.
Watch identifier shadowing because a pattern
may bind a name rather than compare its value.
Use matches! for a boolean question
when discarding the payload is intentional.
Use let-else when an early rejection leaves
one clear case for the remaining function.
Extract a small transition function
when nested matches obscure the rule.
Preserve distinctions consumers use to
choose retry, refusal, or manual recovery.
Avoid converting every rejected
transition into an uninformative generic error.

## Validation

Exercise every relevant source-state and event combination.
Test repeated completion, completion
before start, and stale-attempt completion.
Assert that rejection preserves the previous durable state.
Test stored variant decoding independently
because old values outlive executable versions.
Include unknown tags and absent
discriminators for extensible protocols.
Compile a downstream matching
example when changing public enums.
Check the error mapping in the adapter
that exposes the transition to callers.
Make success tests assert the returned
payload, not merely an Ok discriminant.

## Limit

Exhaustive matching does not establish
liveness, fairness, authorization, or durability.
A state change becomes durable through its storage transaction.
A success-shaped decoded value still needs
provenance validation before trusted use.
