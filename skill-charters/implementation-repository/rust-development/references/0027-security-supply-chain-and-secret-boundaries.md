# Security, supply chain, and secret boundaries

## Purpose

Reduce exposure at dependency,
input, build, and diagnostic boundaries.
Use this note when adding crates,
processing untrusted data, or handling credentials.
The aim is a concrete threat-informed
check set rather than a generic security claim.

## Source posture

[Cargo build scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html) documents host-side build execution.
[RustSec](https://rustsec.org/) provides advisory information.
[Cargo registry authentication](https://doc.rust-lang.org/cargo/reference/registry-authentication.html) documents credential handling.
Recommendations here require adaptation to
the application's actual trust boundaries.

## Practice

Identify the untrusted producer
and the resource it can influence.
Validate input size before expensive parsing or allocation.
Keep authorization checks at
the component owning the effect.
Do not treat a dependency name or
popularity as a security review.
Inspect newly introduced build
scripts and procedural macros.
Review transitive dependency
changes as well as the direct crate.
Keep secrets out of debug formatting,
fixtures, command output, and receipts.
Prefer narrowly scoped credentials and
interfaces where the deployment supports them.

## Worked dependency admission

Suppose a parser crate would replace a small local parser.
Identify the syntax and
diagnostic requirements it must satisfy.
Review its license, maintenance state,
supported compiler, and dependency graph.
Inspect build-time execution and optional features.
Check current advisories against the exact resolved version.
Run representative accepted and malformed inputs.
Compare resource limits and error
behavior with the existing implementation.
Record why the dependency is
worth its maintenance and trust cost.
Do not install unrelated tooling
merely because an advisory scan mentions it.

## Input threat model

List attacker-controlled bytes, paths,
identifiers, counts, and nested structures.
Check integer overflow before allocation or indexing.
Reject path traversal according to
the actual filesystem access model.
Do not assume canonicalizing a
path removes races or symlink attacks.
Use capability-oriented handles or
directory-relative operations
when the threat model warrants them.
Escape untrusted text at rendering boundaries.
Avoid invoking a shell with
untrusted interpolated arguments.
Keep parser failure distinct from authorization denial.

## Credential handling

Retrieve credentials only through the
authorized application's intended mechanism.
Do not print environment dumps
when diagnosing configuration.
Use synthetic secret-like values to test redaction.
Review derived Debug on structures
that can contain tokens or private bodies.
Keep error chains from exposing request headers.
Avoid placing secrets in process arguments visible
to other local processes where safer input exists.
Document rotation and revocation
behavior for the actual credential provider.
Treat possession of a token as insufficient
evidence that every target action is authorized.

## Build and reproducibility

Pin resolution with the lockfile
when reproducing an application build.
A lockfile identifies versions but does
not prove those versions are trustworthy.
Review source changes in vendored or patched dependencies.
Keep build outputs separate from
source-only governance artifacts.
Use a restricted environment for
unfamiliar build dependencies when practical.
Record network access required by build
scripts instead of hiding it in setup.
Do not claim hermeticity unless the
build's ambient inputs were actually controlled.
Check license and target
restrictions before distributing a binary.

## Validation

Run targeted malformed-input tests with bounded resources.
Inspect logs using synthetic private values.
Check current advisories with
the actual dependency resolution.
Test denied actions through the
real boundary rather than only the UI.
Review filesystem and shell
arguments for attacker-controlled components.
Record findings, accepted risks, and untested surfaces.
Do not describe a clean advisory
scan as a complete security audit.
Use a specific reproduction for each actionable defect.

## Limit

Memory safety does not eliminate injection,
authorization, denial-of-service, or supply-chain risks.
A security checklist establishes only the checks performed.
Do not infer permission to retrieve or
expose real credentials from a debugging task.
