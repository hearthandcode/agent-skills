# Crate, module, and workspace architecture

## Purpose

Organize Rust code so ownership and
dependency direction remain inspectable.
Use this reference when extracting modules,
creating crates, or changing workspace configuration.
The architecture should support independent
testing without multiplying interfaces unnecessarily.

## Source posture

[Workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html) documents shared Cargo configuration.
[Visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html) documents public and restricted items.
The decomposition advice below is an engineering recommendation.
Inspect actual consumers and compile
costs before introducing new crate boundaries.

## Practice

Keep pure domain logic
independent of UI and transport frameworks.
Use a public module facade to expose the supported contract.
Keep implementation modules private
unless consumers need their structure.
Create a crate when ownership, reuse,
dependency isolation, or build behavior justifies it.
Avoid a catch-all common crate that
accumulates unrelated responsibilities.
Keep dependency direction acyclic and understandable.
Centralize workspace configuration where Cargo
supports it, with member opt-in where required.
Document package selection so checks do
not accidentally omit the changed member.

## Worked decomposition

Suppose a desktop package contains parsing,
domain validation, storage, and UI command code.
First extract pure validation into
a private module with unit tests.
Expose only the validated type and
the operation the command adapter needs.
If another consumer needs the same
domain API, consider a dedicated domain crate.
Keep storage traits narrow and implemented by an outer adapter.
Do not make the domain crate depend on desktop framework types.
Use a composition root to wire
concrete adapters to domain operations.
Test the domain without opening a window or database.
Measure whether extraction improves actual
ownership and testing before splitting further.

## Public surface

Re-export intentional public types from a small facade.
Avoid leaking a dependency's type unless
the compatibility commitment is acceptable.
Keep internal error details behind stable boundary errors.
Use pub(crate) when sharing inside the
crate rather than exposing an external API.
Document invariants on the public
type, not only beside an internal helper.
Keep examples compilable through
the facade consumers actually use.
Review feature-gated exports
under every supported configuration.
Do not assume a module rename is
harmless if callers import its public path.

## Cargo configuration

Read workspace members, default-members,
resolver, dependency inheritance, and package metadata.
Check whether a virtual workspace
needs an explicit resolver choice.
Distinguish a workspace dependency
declaration from a member actually inheriting it.
Keep features and default-feature
behavior explicit for optional integrations.
Inspect cargo tree when a small change
unexpectedly pulls a large dependency family.
Avoid embedding machine-specific
absolute paths into portable manifests.
Check build scripts and proc macros as host-side dependencies.
Keep generated targets outside
source-only governance repositories.

## Validation

Run checks for the affected package
and its real downstream consumers.
Build supported minimal and default feature configurations.
Test documentation through the public facade.
Use a dependency graph inspection to verify
domain code does not import outer adapters.
Check no_std or target constraints
only when the package promises them.
Inspect packaging contents if the
crate is intended for distribution.
Test the minimum compiler declared by the package.
Record the exact workspace and feature selection in the receipt.

## Evolution and tradeoffs

A module boundary is cheaper to revise than a public crate API.
A crate boundary can improve dependency
isolation but adds release and configuration work.
Avoid interfaces whose only
implementation is an unnecessary pass-through wrapper.
Keep cross-cutting tracing and errors deliberate
rather than inherited accidentally from frameworks.
Move code without behavior changes when
isolating architecture from a semantic fix.
Preserve existing consumers until the
replacement API has a migration path.
Use an architecture decision only when
the tradeoff needs durable explanation.

## Limit

A tidy dependency graph does not
prove runtime isolation or security.
Workspace membership does not
establish that every member was tested.
Architecture claims should cite the
actual dependency and consumer evidence.
