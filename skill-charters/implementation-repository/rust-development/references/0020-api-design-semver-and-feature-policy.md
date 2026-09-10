# API design, semver, and feature policy

## Purpose

Make public Rust APIs predictable and
evolve them without surprising consumers.
Use this note when adding methods, changing
bounds, exposing types, or adjusting Cargo features.
The contract includes behavior, errors,
ownership, and supported configurations.

## Source posture

[API checklist](https://rust-lang.github.io/api-guidelines/checklist.html) collects Rust API recommendations.
[SemVer](https://doc.rust-lang.org/cargo/reference/semver.html) describes compatibility guidance.
[Features](https://doc.rust-lang.org/cargo/reference/features.html) documents feature behavior.
These are documented conventions and mechanisms;
a project may impose stricter support commitments.

## Practice

Name methods according to ownership and conversion behavior.
Use borrowed inputs when the callee does not need ownership.
Expose meaningful domain errors
where callers must branch on recovery.
Keep constructors explicit about validation and cost.
Document panics, errors, safety
requirements, and examples where relevant.
Avoid public fields when future invariant
changes require controlling construction.
Treat trait bounds, auto traits, and
lifetimes as part of the public contract.
Do not expose a dependency's concrete type
casually because consumers may depend on its version.

## Worked API change

Suppose a library currently returns
an owned String for a stored label.
Changing the return to &str may reduce
allocation but changes caller lifetime obligations.
Inspect consumers that retain the
result after dropping or mutating the owner.
Add a borrowed accessor while retaining
the owned API if compatibility requires it.
Document the borrowed accessor's
lifetime and the owned method's allocation.
Compile a small downstream consumer
demonstrating the supported usage.
Measure allocation reduction only
if it matters to the actual workload.
Do not describe the change as purely internal
because the representation looks equivalent.
Use deprecation and a migration
example when removing the older contract.

## Feature design

Treat Cargo features as additive configuration where possible.
Avoid mutually exclusive feature combinations
unless the package documents and checks them.
Remember that dependency feature
unification can enable features indirectly.
Use no-default-features checks to
expose accidental reliance on defaults.
Test each supported integration combination
rather than assuming all-features covers them.
Keep optional runtime behavior behind explicit
configuration when a feature only enables compilation.
Do not let a feature silently change
serialized meaning or authorization policy.
Explain whether a feature affects API surface,
dependencies, performance, or target support.

## Compatibility review

Removing or renaming a public item can break imports.
Adding a required trait method can break external implementations.
Changing Send or Sync behavior can break threaded consumers.
Tightening a lifetime bound can
invalidate previously accepted code.
Adding enum variants can break exhaustive
downstream matches unless extensibility was designed.
Changing defaults can alter runtime
behavior even when code still compiles.
Schema compatibility and Rust source
compatibility require separate review.
Minimum compiler changes should follow
the project's documented version policy.

## Validation

Compile representative downstream
consumers against the changed facade.
Exercise default, minimal, and supported feature combinations.
Run documentation tests for examples
showing ownership and failure behavior.
Test semantic compatibility using
stored fixtures or protocol examples.
Use a compatibility tool when available, but
review behavioral changes it cannot detect.
Inspect generated documentation for accidental public items.
Confirm the declared minimum compiler
with an actual check before advertising it.
Record unsupported combinations
explicitly rather than silently skipping them.

## Decision record

Describe the consumer problem and the resulting API behavior.
List the alternative that preserves
compatibility and why it was insufficient if rejected.
Include migration steps for changed
names, bounds, or representations.
Identify deprecation timing only when the project has decided it.
Keep user-visible error code changes in the release explanation.
Separate additive convenience APIs from required migrations.
Preserve the old contract in tests
when backward compatibility is promised.

## Limit

SemVer tooling does not establish
complete behavioral compatibility.
A green local build does not
prove downstream crates still compile.
Documented recommendations do not
automatically confer project approval.
