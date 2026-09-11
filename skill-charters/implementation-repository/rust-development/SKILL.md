---
name: rust-development
description: Implement, diagnose, review, and validate Rust changes using explicit ownership, checked boundaries, documented APIs, and reproducible compiler and test evidence.
metadata:
  revision: depth-enrichment-2026-09-09
  status: candidate
  verified: false
---

# Rust Development

## 01. Purpose, use, and evidence
R(§01-01) [proof-element from section 01, sentence-level atomic element]
R(§01-02) [proof-element from section 01, sentence-level atomic element]
R(§01-03) [proof-element from section 01, sentence-level atomic element]

Use this skill for Rust implementation,
diagnosis, review, migration, and test work.
Start from the requested behavior and
the repository's actual public contract.
Apply documented Rust semantics to implementation
decisions and test the remaining runtime obligations.
Treat this package as a review-required engineering candidate.
The examples and procedures recommend practices;
they do not claim blanket approval by the Rust project.
The source links identify language guarantees,
library contracts, and project-maintained guidance.
Framework-specific mappings to external governance systems are proposed
integration guidance with their own source owners; those references are
available in the canonical source but are not part of this public-safe projection.
Keep these categories explicit whenever a
stronger guarantee would change a decision.
A successful check supports the named predicate on
the tested source, toolchain, features, and target.
It does not establish complete
correctness across untested configurations.
Use the user's existing
authorization for the requested local work.
Do not transform a documentation or diagnosis
request into an unrelated implementation project.
When asked to implement, carry the change
through relevant checks and a concrete handoff.
When asked to review, report evidence-backed
findings without silently repairing unrelated code.
When asked to diagnose, identify the cause and
reproduction before proposing the smallest correction.
Read only references relevant to the task after this entrypoint.
Each reference contains deeper decisions,
examples, failure cases, validation, and limits.
The reference filenames are stable routes within this package.

## 02. Source and toolchain orientation
R(§02-01) [proof-element from section 02, sentence-level atomic element]
R(§02-02) [proof-element from section 02, sentence-level atomic element]
R(§02-03) [proof-element from section 02, sentence-level atomic element]

Read the nearest charter, Cargo.toml,
lockfile, affected facade, tests, and one real caller.
Resolve which directory is the workspace
and which package owns the changed code.
Record the compiler version, edition, target,
feature set, and minimum supported compiler.
Do not assume the latest online documentation
describes the compiler selected by the repository.
Use version-specific documentation or a minimal
compile experiment for uncertain language behavior.
Inspect rust-toolchain configuration
before invoking a different toolchain.
A rust-version declaration is a support
commitment to verify, not proof that verification occurred.
Check build scripts and procedural macros
before compiling unfamiliar dependencies.
Compilation may execute host code even
when the final application never runs.
Keep temporary experiments and
build output outside a source-only Hub.
Use locked dependency resolution to
reproduce an application configuration.
Treat an offline cache miss as an
environment limitation rather than a Rust defect.
Inspect the working tree before
editing and preserve other authors' changes.
Read the direct source when an old
handoff disagrees with the current checkout.
Record the base identity used for comparison
in a durable receipt when the task needs one.
Use the smallest source set that settles the decision.
Do not inspect unrelated private material or
credentials as part of routine orientation.
Route deeper practice through reference
0001 and the Cargo documentation linked there.

## 03. Translate the request into an engineering contract
R(§03-01) [proof-element from section 03, sentence-level atomic element]
R(§03-02) [proof-element from section 03, sentence-level atomic element]
R(§03-03) [proof-element from section 03, sentence-level atomic element]

Write the observable behavior in terms
of input, state, operation, and result.
Replace vague goals such as “robust import”
with explicit accepted and rejected cases.
Identify the consumer that needs the changed behavior.
Name the public API or transport
boundary through which the consumer reaches it.
State which state may change and
what must remain unchanged on rejection.
Separate structural validation from
domain interpretation and current permission.
Identify the failure category the caller needs to distinguish.
Specify relevant limits before designing
allocation, recursion, or queue behavior.
Use a small transition table when state and
event combinations are the main uncertainty.
Choose a representative valid
example and a meaningful negative example.
Keep test oracles independent of the
implementation where a shared bug is plausible.
Document reversible assumptions
and proceed with independent work.
Resolve missing product semantics
before changing persisted meaning.
Do not create abstractions until
their consumer and invariant are clear.
Select a template only if its fields
improve this task's reproducibility.
A short task may need only a
clear test and a concise explanation.
A migration or external-effect
boundary needs explicit recovery semantics.
Use reference 0001 for decomposition and 0032 for completion.

## 04. Type selection and checked construction
R(§04-01) [proof-element from section 04, sentence-level atomic element]
R(§04-02) [proof-element from section 04, sentence-level atomic element]
R(§04-03) [proof-element from section 04, sentence-level atomic element]

Use structs for simultaneously
meaningful facts and enums for alternatives.
Use distinct newtypes when accidentally
interchanging identifiers would be a defect.
A type alias does not prevent
substitution between identical underlying types.
Keep invariant-bearing fields
private and check all constructor paths.
Use TryFrom or another fallible
constructor when some raw values are invalid.
Reserve From for conversions whose
contract is genuinely infallible.
Keep untrusted DTOs separate from validated domain values.
Do not let derived deserialization bypass a checked constructor.
Use Option when absence has one meaning
and an enum when absence causes differ.
Select numeric widths from the domain
and protocol rather than the host machine.
Use checked conversions at width and sign boundaries.
Define float treatment for NaN, infinity, and
signed zero if those values enter ordering or identity.
Check equality and hashing together
when implementing either manually.
Do not derive Default if its value violates
the domain invariant or hides missing input.
Review mutation methods for
preservation of constructor-established guarantees.
A value checked once may still require
current-state validation before an effect.
Keep external authorization outside a purely
structural marker unless the type's lifecycle truly enforces it.
Use references 0002, 0003, and 0026
for construction and admission details.

## 05. Ownership decisions before borrow fixes
R(§05-01) [proof-element from section 05, sentence-level atomic element]
R(§05-02) [proof-element from section 05, sentence-level atomic element]
R(§05-03) [proof-element from section 05, sentence-level atomic element]

Identify the owner responsible for
retaining and releasing each resource.
Borrow when an operation only
inspects data for a bounded duration.
Move when responsibility transfers to another component.
Clone when an independent owned copy
is intended and its cost is acceptable.
Do not use clone as an unexplained
default response to compiler diagnostics.
Read the start and last use of a conflicting borrow.
Shorten the borrow, extract a small
owned key, or separate lookup from mutation.
Avoid retaining a tiny view through a huge
owner when copying would reduce memory pressure.
Use slices and str for borrowed contiguous views.
Use owned buffers when values must outlive the original input.
Do not add static lifetimes to hide an invalid ownership model.
Use stable identifiers instead of
self-references when that keeps movable structures simple.
Arc provides shared ownership and does
not make arbitrary inner mutation safe.
Use synchronization only where mutation is actually shared.
Break reference-count cycles
through a deliberate ownership design.
Keep RefCell borrow failures visible as
runtime behavior if interior mutability is chosen.
Review resource release on early error,
cancellation, and partial construction.
Use reference 0005 for lifetime and destruction procedures.

## 06. State modeling and transitions
R(§06-01) [proof-element from section 06, sentence-level atomic element]
R(§06-02) [proof-element from section 06, sentence-level atomic element]
R(§06-03) [proof-element from section 06, sentence-level atomic element]

Represent different payload
requirements with explicit enum variants.
Keep queued, running, failed, completed, and
unknown outcomes distinct when recovery differs.
Avoid a status string plus optional
fields that permits contradictory combinations.
Match explicitly on internal closed
enums to expose new variants at call sites.
Use wildcard fallbacks only where
extensibility and fallback behavior are deliberate.
Keep pure transition classification
separate from persistence and dispatch.
Return the original state on rejection
when the API promises recoverability.
Check expected revision and attempt
identity before applying asynchronous completion.
Do not accept stale success merely
because its payload has a valid shape.
Use runtime state for persistence and heterogeneous collections.
Use typestate when unavailable
operations materially improve the public API.
Keep constructors for privileged
states private to the validating component.
Do not derive Clone for a consumable
capability without a clear duplication policy.
Treat revocation and expiration as runtime
obligations when they can change externally.
Test both accepted transitions and
forbidden source-state/event combinations.
Confirm rejected transitions leave durable state unchanged.
Persist the transition through the actual
transaction before reporting durable success.
Use references 0003 and 0006 for the detailed design.

## 07. Traits and abstraction selection
R(§07-01) [proof-element from section 07, sentence-level atomic element]
R(§07-02) [proof-element from section 07, sentence-level atomic element]
R(§07-03) [proof-element from section 07, sentence-level atomic element]

Start with a concrete implementation unless
a substitution need is already established.
Introduce a trait for a real port, second
implementation, or useful test boundary.
Keep methods narrow enough that a fake
represents the actual domain dependency.
Use associated types for an
implementation-selected related type.
Use generic parameters where multiple
parameterized implementations are meaningful.
Place bounds on the method that needs
them rather than every use of a container.
Choose static dispatch when concrete types are known.
Choose dyn dispatch for runtime
heterogeneity after checking dyn compatibility.
Do not assume generic methods, GATs, or async
trait syntax are automatically usable through dyn.
Specify future Send requirements where callers need them.
Document ownership, allocation, blocking,
and cancellation behavior beyond the signature.
Check blanket implementations for
overlap and downstream compatibility.
Use local wrappers for foreign
integrations constrained by orphan rules.
Seal traits when external
implementation would undermine a required invariant.
Avoid sealing merely to enforce an aesthetic preference.
Compile a real consumer and a second
implementation before declaring the abstraction useful.
Keep trait laws stated in prose
distinguishable from compiler-enforced bounds.
Use reference 0004 for GAT and dynamic-interface examples.

## 08. Fixed shape and stronger guarantees
R(§08-01) [proof-element from section 08, sentence-level atomic element]
R(§08-02) [proof-element from section 08, sentence-level atomic element]
R(§08-03) [proof-element from section 08, sentence-level atomic element]

Use const generics when
compile-time shape matters to the consumer.
Prefer a slice when a runtime length is sufficient.
Validate untrusted lengths before
allocating or constructing fixed-size values.
Check multiplication and
conversion used to compute buffer sizes.
Do not rely on target-dependent usize
width for a stable wire representation.
A fixed-size array says nothing about
checksum validity or domain meaning.
A phantom parameter does not establish a
predicate unless construction actually checks it.
A sorted wrapper needs mutation methods that preserve ordering.
A nonempty wrapper needs a defined policy
for consuming or removing its last item.
Use executable runtime predicates for
value relationships outside the static model.
Compile uncertain const
expressions on the supported stable compiler.
Do not advertise unstable
features as universally available Rust.
Separate arithmetic proof, termination proof,
structural validation, and current authorization.
A formal theorem needs its
definitions, assumptions, and checker identity.
A Rust Result return is explicit error
handling rather than a totality proof.
Keep proof-tool adoption proportionate to a named obligation.
Use references 0007, 0008, and
0013 for stronger-technique decisions.


## 09. Public API design
R(§09-01) [proof-element from section 09, sentence-level atomic element]
R(§09-02) [proof-element from section 09, sentence-level atomic element]
R(§09-03) [proof-element from section 09, sentence-level atomic element]

Make ownership and cost visible in
method names, signatures, and documentation.
Expose only the surface consumers
need through a deliberate facade.
Keep internal types and dependencies private
unless exposing them is an intentional commitment.
Document expected errors and panic
conditions for public operations.
Include a short example that uses the actual exported path.
Treat lifetime, Send, Sync, and trait
bounds as compatibility commitments.
A borrowed return may reduce allocation while
imposing new lifetime constraints on callers.
Consider adding a borrowed accessor
instead of replacing a compatible owned API.
Use deprecation and a migration example
when removing an established contract.
Do not expose debug formatting as a stable external format.
Keep error variants useful for caller recovery
without leaking transport details into pure domain code.
Review non-exhaustive enums when future variants are expected.
Check downstream implementations
before adding required trait methods.
Keep API compatibility separate
from stored-format compatibility.
Compile a representative downstream crate
when changing exports or generic bounds.
Measure performance claims rather than
using “zero cost” as a substitute for evidence.
Use reference 0020 and the Rust
API Guidelines for focused review.

## 10. Crate and workspace boundaries
R(§10-01) [proof-element from section 10, sentence-level atomic element]
R(§10-02) [proof-element from section 10, sentence-level atomic element]
R(§10-03) [proof-element from section 10, sentence-level atomic element]

Keep domain validation
independent of UI and transport frameworks.
Use private modules before creating a crate
when ownership does not require separate packaging.
Create a crate for justified reuse,
dependency isolation, ownership, or build behavior.
Avoid a common crate that becomes a
dependency sink for unrelated concerns.
Keep dependency direction acyclic and explicit.
Use a composition root to connect
concrete adapters to domain ports.
Read workspace members and
default-members before selecting a check command.
Inspect resolver and inherited dependencies
rather than assuming every member uses root settings.
Review cargo tree when an apparently
small change pulls a large dependency family.
Keep optional integration dependencies
behind documented features where appropriate.
Treat features as additive configuration where practical.
Test supported minimal configurations
instead of relying only on all-features.
Do not assume one all-features build covers
mutually exclusive or target-specific behavior.
Keep machine-specific paths out of portable manifests.
Check packaging contents when distribution is part of the task.
Separate source-only governance
artifacts from generated build output.
Use references 0019 and 0020 for
architecture and feature policy.

## 11. Error design and diagnostic mapping
R(§11-01) [proof-element from section 11, sentence-level atomic element]
R(§11-02) [proof-element from section 11, sentence-level atomic element]
R(§11-03) [proof-element from section 11, sentence-level atomic element]

Classify errors according to caller recovery decisions.
Distinguish malformed input, unsupported version, missing
data, conflict, unavailable dependency, and unknown outcome.
Keep stable codes separate from human-readable explanation.
Attach operation context at the
layer that understands its meaning.
Preserve causal source errors internally where useful.
Map errors deliberately at each transport boundary.
Do not expose full debug output or
request bodies to external consumers.
Use bounded messages when input controls diagnostic text.
Avoid broad defaults that turn
malformed input into plausible successful data.
Reserve panic for internal invariant
violations under the project's policy.
Use Result for expected input and resource failures.
An expect message should explain why
the operation cannot fail at that point.
Review panic behavior in destructors and foreign boundaries.
Do not classify every timeout as safe to retry.
A conflict can require reloading and a
new decision rather than automatic replay.
Test codes and structured fields when prose
wording is not part of the compatibility contract.
Use reference 0021 for implementation and recovery details.

## 12. Serialization admission
R(§12-01) [proof-element from section 12, sentence-level atomic element]
R(§12-02) [proof-element from section 12, sentence-level atomic element]
R(§12-03) [proof-element from section 12, sentence-level atomic element]

Decode into a raw DTO before
constructing a trusted domain value.
Validate nested fields and array items
as carefully as the top-level object.
A closed outer object can still
contain unconstrained nested values.
Choose unknown-field behavior from the actual boundary contract.
Use strict rejection for executable control data
when silent misspellings could change behavior.
Use explicit extension mechanisms where
descriptive records require forward compatibility.
Do not combine Serde deny_unknown_fields
with unsupported flattening arrangements.
Keep absent, null, empty, and default
distinct when they carry different meaning.
Use version tags before interpreting a stored or wire value.
Prefer unambiguous enum tags for important input boundaries.
Test untagged enum overlap before relying on variant selection.
Do not let a derived deserializer
manufacture a checked or privileged type.
Route admission through fallible conversion.
Test schema and Rust acceptance
on the same representative cases.
Ordinary JSON output is not a canonical byte contract by itself.
Name the canonicalization algorithm
if digests depend on serialization.
Use reference 0026 for detailed
admission and migration procedures.

## 13. Persistence and migration
R(§13-01) [proof-element from section 13, sentence-level atomic element]
R(§13-02) [proof-element from section 13, sentence-level atomic element]
R(§13-03) [proof-element from section 13, sentence-level atomic element]

Identify the transaction that owns the durable change.
Check expected revision when concurrent updates can race.
Keep schema version and data meaning explicit.
Do not reinterpret an old numeric field
after changing units without a migration.
Use checked arithmetic during conversion.
Preserve a recoverable previous
representation before destructive replacement.
Verify the backup is readable
before claiming rollback readiness.
Define whether migration is repeatable,
idempotent, or rejected after completion.
Test interruption before conversion, before commit,
and after commit where the storage model permits it.
Separate stored success from a
successful response that was never committed.
Keep rejected historical records
available for diagnosis within privacy limits.
Do not replace malformed data with
defaults merely to finish the migration.
Test old-reader and new-reader
compatibility directions independently.
Document when rollback cannot reverse external effects.
Keep source and adapter revisions attached to converted records.
Use references 0026 and 0028 for recovery and evidence.
Return the migration's actual
tested range of historical versions.

## 14. Async and task ownership
R(§14-01) [proof-element from section 14, sentence-level atomic element]
R(§14-02) [proof-element from section 14, sentence-level atomic element]
R(§14-03) [proof-element from section 14, sentence-level atomic element]

Name the component that starts,
observes, and completes each task.
Avoid detached activity without a recovery or supervision owner.
Bound queue size and define overload behavior.
Keep blocking work away from executor
threads through the runtime's supported mechanism.
Do not hold a lock across await
without a deliberate, reviewed reason.
Inspect each awaited operation's cancellation behavior.
Dropping a future can leave partial progress or external work.
A select loop may repeatedly cancel losing branches.
Preserve framing and partial I/O state
where cancellation would otherwise lose it.
Distinguish cancellation request
from confirmed task termination.
Observe task completion before
releasing resources the task still uses.
Do not assume dropping a handle cancels its task.
Use explicit graceful shutdown with
a deadline and a forced-stop outcome.
Stop accepting work before draining outstanding operations.
Keep cancellation and unknown completion visible to the caller.
Use reference 0023 and the
actual locked runtime's documentation.
Test overload, task failure, late reply, and shutdown races.

## 15. Concurrency and shared state
R(§15-01) [proof-element from section 15, sentence-level atomic element]
R(§15-02) [proof-element from section 15, sentence-level atomic element]
R(§15-03) [proof-element from section 15, sentence-level atomic element]

Choose shared mutation only when ownership cannot remain local.
Arc shares ownership but requires
appropriate inner synchronization for mutation.
A mutex is often clearer than an ad hoc atomic protocol.
Use read-write locks only when the
workload and contention justify them.
Keep critical sections short.
Do not call unknown or reentrant code
while holding a lock without a clear contract.
Define behavior after poisoning rather
than blindly assuming invariants survived.
Keep atomic-ordering arguments
beside the invariant they protect.
Use compare-and-swap or transactions
where stale state would overwrite newer state.
Test stale attempt completions and duplicate event delivery.
Do not infer exactly-once behavior from a single process mutex.
Consider Loom for small synchronization
algorithms with meaningful schedule exploration.
Use the instrumentation required by the model.
Separate modeled schedules from process crash
or remote-service behavior excluded by the test.
Keep task and resource ownership visible during shutdown.
Measure contention before
introducing more complex synchronization.
Use references 0023 and 0028 for lifecycle and recovery.

## 16. Performance decisions
R(§16-01) [proof-element from section 16, sentence-level atomic element]
R(§16-02) [proof-element from section 16, sentence-level atomic element]
R(§16-03) [proof-element from section 16, sentence-level atomic element]

Begin with a user-visible budget
rather than an optimization technique.
Measure latency, throughput, allocation, memory,
startup, or binary size according to the actual problem.
Profile representative workloads before changing hot-path code.
Keep compiler, target, profile,
features, and dependencies comparable.
Separate CPU work from blocking I/O and queue wait.
Avoid comparing debug and release results
as if they measured the same configuration.
Prevent benchmark elimination while preserving realistic inputs.
Include setup only when it belongs to the user-visible budget.
Test valid and rejected inputs when both occur in practice.
Compare distributions and absolute
values rather than one favorable run.
Check memory and tail-latency
regressions when average throughput improves.
Do not trade soundness for an unmeasured speed claim.
Review retained owners when
replacing owned values with borrowed slices.
Bound reservations derived from untrusted lengths.
Keep raw measurements and reproducible commands available.
Use reference 0024 for benchmark design and interpretation.
Run semantic tests around every optimized path.


## 17. Unsafe and FFI review
R(§17-01) [proof-element from section 17, sentence-level atomic element]
R(§17-02) [proof-element from section 17, sentence-level atomic element]
R(§17-03) [proof-element from section 17, sentence-level atomic element]

Prefer safe code when it satisfies the measured requirement.
Name every invariant the compiler cannot verify.
Keep unsafe blocks small and justify the exact operation.
Separate caller obligations of unsafe functions
from obligations inside their implementations.
Review validity, alignment,
initialization, aliasing, ownership, and lifetime.
Do not construct references from foreign
pointers solely because a foreign call returned success.
Check pointer-length arithmetic
and complete allocation validity.
Keep allocator ownership and release functions compatible.
Define ABI, layout, target assumptions, and unwind behavior.
Do not rely on ordinary Rust layout
matching a foreign representation.
Review Clone, Drop, Send, and Sync together for wrapper types.
Ensure safe public methods cannot
invalidate hidden raw-pointer assumptions.
Do not rely on destructors always running for memory safety.
Use Miri or sanitizers where
supported, recording excluded paths.
Treat a passing tool run as bounded
evidence rather than proof of soundness.
Keep an unsafe ledger with location,
invariant, tests, and removal condition.
Use reference 0025 before modifying the trusted boundary.

## 18. Procedural macros
R(§18-01) [proof-element from section 18, sentence-level atomic element]
R(§18-02) [proof-element from section 18, sentence-level atomic element]
R(§18-03) [proof-element from section 18, sentence-level atomic element]

Demonstrate the repeated
handwritten Rust before introducing a macro.
Prefer ordinary functions or
declarative macros for simpler cases.
Define the accepted syntax and supported item kinds.
Separate parsing, semantic checking, and token emission.
Retain spans so failures point to user input.
Return intentional compile
diagnostics instead of internal panics.
Preserve generics, where clauses, and unrelated attributes.
Use explicit generated paths and test renamed dependencies.
Check collisions with user identifiers and helper names.
Treat proc macros as host-executed dependencies.
Avoid hidden environment, filesystem, or network inputs.
Test the parser separately and compile a downstream consumer.
Include unsupported syntax and missing or duplicate attributes.
Inspect representative expansion for
readability and unexpected allocation.
Version syntax changes as part of the macro's public contract.
A macro emits Rust and does not
strengthen rustc's underlying type theory.
Use reference 0009 for architecture and failure fixtures.

## 19. Declarative macros
R(§19-01) [proof-element from section 19, sentence-level atomic element]
R(§19-02) [proof-element from section 19, sentence-level atomic element]
R(§19-03) [proof-element from section 19, sentence-level atomic element]

Choose a macro only where syntactic repetition requires one.
Use deliberate fragment specifiers and unambiguous separators.
Document expression evaluation count and ownership transfer.
Bind expressions once when
repeated evaluation would be surprising.
Keep temporary names scoped through a block expression.
Use defining-crate paths for exported
helper references where appropriate.
Test downstream expansion without convenient local imports.
Check adversarial local identifiers and helper visibility.
Handle empty, single, multiple, and trailing-separator inputs.
Avoid broad matcher arms that hide malformed syntax.
Review edition-sensitive fragment behavior.
Do not return from or mutate the caller unexpectedly.
Keep generated bounds and errors
understandable at the call site.
Compare growing syntax complexity with a
proc macro or ordinary data constructors.
Compile both accepted and rejected examples.
Use reference 0010 for the worked single-evaluation example.
Do not describe hygienic expansion
as proof of algorithm correctness.

## 21. Proof and formal-language boundaries
R(§21-01) [proof-element from section 21, sentence-level atomic element]
R(§21-02) [proof-element from section 21, sentence-level atomic element]
R(§21-03) [proof-element from section 21, sentence-level atomic element]

Name the obligation before selecting a formal technique.
Rust newtypes can prevent identifier interchange.
Checked constructors can establish bounded input invariants.
Typestate can restrict operation availability.
Ordinary Rust compilation does not prove
arbitrary termination or mathematical truth.
A Lean proof must name definitions,
assumptions, theorem, and environment.
Distinguish a proof object from a
report stating that a check passed.
Bind evidence to source identity
and the precise proposition instance.
A certificate schema does not verify the certificate's truth.
Keep untrusted decoded evidence
separate from trusted witness construction.
Reject stale digest, mismatched predicate,
unsupported verifier, and missing assumptions.
Bound verification resources and classify
timeout as unavailable or indeterminate evidence.
Keep runtime authorization separate
from structural or arithmetic proof.
Do not advertise a bridge as implemented
before exercising the actual verifier and consumer.
Treat Haskell and Idris concepts as
orientation, not automatic Rust equivalence.
Use references 0008 and 0013 for
detailed comparison and certificate design.
Record all remaining assumptions in the result.

## 24. Application adapters and deterministic core
R(§24-01) [proof-element from section 24, sentence-level atomic element]
R(§24-02) [proof-element from section 24, sentence-level atomic element]
R(§24-03) [proof-element from section 24, sentence-level atomic element]

Keep rendering and input translation outside domain rules.
Represent commands explicitly and
validate them at the domain boundary.
Use a headless path for testing pure transitions.
Inject clocks, randomness, and
I/O where reproducibility matters.
Keep simulation time separate from wall-clock time.
Record external inputs needed for replay.
Do not assume deterministic
cross-platform behavior without relevant evidence.
Keep long-running work off a UI thread
through the supported framework mechanism.
Closing a view is not proof that its background task stopped.
Use stable operation identity for progress and cancellation.
Keep CLI human output separate from machine-readable output.
Treat exit codes as a documented interface.
Validate worker replies as strictly as requests.
Keep framing, size, timeout, and queue limits explicit.
Test adapter mappings in addition to the shared domain types.
Use reference 0031 for game, desktop, CLI, and harness patterns.
State which platform behavior was actually exercised.


## 25. Test selection by claim
R(§25-01) [proof-element from section 25, sentence-level atomic element]
R(§25-02) [proof-element from section 25, sentence-level atomic element]
R(§25-03) [proof-element from section 25, sentence-level atomic element]

Choose the test layer from the failure mechanism.
Use unit tests for pure decisions.
Use integration tests for
producer-consumer and persistence boundaries.
Use compile-fail tests for intentionally unavailable operations.
Use property tests for meaningful
invariants over many combinations.
Use fuzzing for malformed-input spaces.
Use concurrency model exploration
for interleaving-sensitive algorithms.
Do not write tests that simply mirror
the implementation's branch structure.
A round trip can pass when encoder and decoder share a defect.
Include independent expected values or another useful oracle.
Check that test filters execute the intended nonzero case count.
Keep positive companions for negative tests.
A rejection-only suite can accidentally
approve an implementation that rejects everything.
Record generated-test seeds and minimized counterexamples.
Keep live external effects out of fuzz targets.
Use reference 0022 for layer selection and evidence limits.
Stop expanding tests when the relevant
uncertainty is resolved and required checks pass.

## 26. Compiler feedback loop
R(§26-01) [proof-element from section 26, sentence-level atomic element]
R(§26-02) [proof-element from section 26, sentence-level atomic element]
R(§26-03) [proof-element from section 26, sentence-level atomic element]

Run the narrow check before broad repository commands.
Read the first causal error and the source it identifies.
Explain the mismatch in terms of
types, ownership, bounds, or configuration.
Do not add clone, static, unsafe, or
broad lint suppression without a reason.
Inspect dependency versions when an expected API is unavailable.
Separate linker errors from Rust type errors.
Separate a lint suggestion from a semantic requirement.
Apply a focused correction and rerun the same relevant check.
Do not execute an old binary after a failed build.
Keep compiler and feature selection stable across comparisons.
Use a minimal isolated example
for a difficult language question.
Preserve tests that encode the requested contract.
Do not weaken acceptance merely to obtain a green result.
Review the final diff after formatting and generated changes.
Report unresolved warnings and baseline failures precisely.
Use reference 0029 for diagnostic triage.
A compiler pass must be followed by
behavioral evidence for a behavioral claim.

## 27. Reproducible command patterns
R(§27-01) [proof-element from section 27, sentence-level atomic element]
R(§27-02) [proof-element from section 27, sentence-level atomic element]
R(§27-03) [proof-element from section 27, sentence-level atomic element]

Substitute the actual package name and
supported features in these patterns.
Run commands from the inspected workspace root.
Do not copy the placeholder PACKAGE
literally into a completion receipt.
A locked command should fail rather
than silently change dependency resolution.
Use offline only when cached dependencies are sufficient.
Keep build output in the repository's allowed
target location or an external scratch target.
Record exit status and executed
test count after each meaningful check.

```sh
cargo check --locked -p PACKAGE
cargo test --locked -p PACKAGE --lib
cargo test --locked -p PACKAGE --test CONTRACT_TEST
cargo test --locked -p PACKAGE --doc
cargo check --locked -p PACKAGE --no-default-features
cargo fmt --all -- --check
cargo clippy --locked -p PACKAGE --all-targets -- -D warnings
```

The formatter pattern checks the
workspace and may expose unrelated baseline debt.
The Clippy pattern uses warnings-as-errors
only when that matches the project's gate.
Do not claim every target or
feature was covered by these examples.
Select the required supported
matrix from the actual package contract.
A missing target toolchain is a
recorded limitation, not a passing test.
Use direct rustc examples for isolated language
experiments when dependencies are unnecessary.
Keep generated binaries and temporary sources outside the Hub.
Record whether a command was a syntax check,
compilation, execution, or packaging operation.

## 28. Security and dependency checks
R(§28-01) [proof-element from section 28, sentence-level atomic element]
R(§28-02) [proof-element from section 28, sentence-level atomic element]
R(§28-03) [proof-element from section 28, sentence-level atomic element]

Identify attacker-controlled input
and the resources it can influence.
Validate sizes before allocation and recursion.
Keep authorization at the effect-owning component.
Inspect new dependencies, transitive
changes, build scripts, and proc macros.
Check current advisories against the
resolved versions when dependency risk is in scope.
A lockfile makes resolution
inspectable but does not establish trust.
Keep secrets out of logs, examples, fixtures, and receipts.
Use synthetic values for redaction tests.
Avoid full environment dumps during configuration diagnosis.
Review Debug implementations on secret-bearing types.
Use structured arguments instead of
shell interpolation for untrusted values.
Treat filesystem normalization and
race resistance as separate concerns.
Do not claim a clean advisory scan is a full security audit.
Record concrete findings and untested surfaces.
Use reference 0027 for the dependency and input workflow.
Do not retrieve real credentials
merely because a test could use them.
Scope any additional security work to
the actual task and threat boundary.

## 29. Observability and recovery evidence
R(§29-01) [proof-element from section 29, sentence-level atomic element]
R(§29-02) [proof-element from section 29, sentence-level atomic element]
R(§29-03) [proof-element from section 29, sentence-level atomic element]

Record request and attempt identity before consequential work.
Keep source-event time distinct from observation time.
Use monotonic time for in-process durations.
Keep structured fields useful for
correlation without exposing full private payloads.
Avoid unbounded metric labels.
Separate queue wait from execution time when diagnosing latency.
Record the last confirmed durable state.
Distinguish not-started, running, failed,
cancelled, completed, and indeterminate as needed.
A timeout does not prove a remote operation failed.
Reconcile unknown outcomes before creating a new attempt.
Prevent late completions from overwriting newer state.
Keep receipts attached to the
source and configuration they checked.
Report skipped and unavailable checks distinctly from failures.
Do not let a receipt grant the next operation automatically.
Test recovery before and after dispatch and commit.
Use reference 0028 for traces, receipts, and restart behavior.
A useful receipt supports reconstruction without
requiring unrestricted access to private material.

## 30. Review and refactoring
R(§30-01) [proof-element from section 30, sentence-level atomic element]
R(§30-02) [proof-element from section 30, sentence-level atomic element]
R(§30-03) [proof-element from section 30, sentence-level atomic element]

Read the intended behavior before evaluating the diff.
Trace validation, state change, persistence, and output.
Review failure paths and supported feature configurations.
Prioritize concrete correctness
defects over aesthetic preferences.
Explain the triggering condition
and consequence for each finding.
Use exact source evidence or a reproduction.
State uncertainty when a necessary
external contract is unavailable.
Keep optional improvements separate from blocking defects.
Prefer behavior-preserving extraction before semantic change.
Check public visibility and
dependency leakage after moving code.
Watch for changed drop order and lifetime requirements.
Do not repair unrelated code during a review-only request.
Run the relevant consumer tests after restructuring.
Review the final generated or formatted diff.
Return no findings when the evidence supports none.
Use reference 0030 for review quality and maintenance tradeoffs.
A bounded review cannot prove the absence of every defect.

## 31. Package resources and practical use
R(§31-01) [proof-element from section 31, sentence-level atomic element]
R(§31-02) [proof-element from section 31, sentence-level atomic element]
R(§31-03) [proof-element from section 31, sentence-level atomic element]

The references directory contains
27 public-safe focused supporting notes (governance-framework references omitted per the project release).
Use the reference whose trigger matches the
decision rather than loading all notes by default.
The schemas directory describes
candidate input and evidence shapes.
Run a real instance validator before
claiming a fixture satisfies a schema.
The fixtures directory should contain
accepted and rejected cases with expected outcomes.
Parsing a fixture file proves only that it is valid JSON.
The Rust templates are adaptation
starting points, not preapproved implementations.
Compile a copied template after
supplying the real domain types and behavior.
The general templates should capture
task-specific decisions rather than remain empty headings.
Keep source-lock values concrete
before using them for integrity claims.
Use package validation to check
counts, routes, and required structure.
Use behavioral example checks to test
the included standalone Rust snippets.
Use reference-closure checks to
catch missing or incorrect local links.
Keep the atlas and public-safe projection
synchronized with current source.
Regenerate digests only after
source and generated outputs are final.
A digest match proves byte identity, not semantic quality.
Keep candidate status and the
separate human verification seal intact.

### Reference routes

- [Rust engineering orientation](references/0001-rust-engineering-orientation.md)
- [Rust language and type system](references/0002-rust-language-and-type-system.md)
- [Algebraic data types and pattern matching](references/0003-algebraic-data-types-and-pattern-matching.md)
- [Traits, generics, GATs, and associated types](references/0004-traits-generics-gats-and-associated-types.md)
- [Ownership, borrowing, lifetimes, and drop](references/0005-ownership-borrowing-lifetimes-and-drop.md)
- [Typestate, capabilities, and proof witnesses](references/0006-typestate-capabilities-and-proof-witnesses.md)
- [Const generics, refinement, and type-level limits](references/0007-const-generics-refinement-and-type-level-limits.md)
- [Haskell, Lean, Idris orientation and non-equivalence](references/0008-haskell-lean-idris-orientation-and-non-equivalence.md)
- [Procedural macro architecture](references/0009-procedural-macro-architecture.md)
- [Declarative macros and hygiene](references/0010-declarative-macros-and-hygiene.md)
- [Crate, module, and workspace architecture](references/0019-crate-module-and-workspace-architecture.md)
- [API design, semver, and feature policy](references/0020-api-design-semver-and-feature-policy.md)
- [Error taxonomy and diagnostics](references/0021-error-taxonomy-and-diagnostics.md)
- [Testing, property, fuzz, and model checking](references/0022-testing-property-fuzz-and-model-checking.md)
- [Concurrency, async, cancellation, and backpressure](references/0023-concurrency-async-cancellation-and-backpressure.md)
- [Performance profiling and benchmarking](references/0024-performance-profiling-and-benchmarking.md)
- [Unsafe, FFI, and trusted computing base](references/0025-unsafe-ffi-and-trusted-computing-base.md)
- [Serde, schema versioning, and migrations](references/0026-serde-schema-versioning-and-migrations.md)
- [Security, supply chain, and secret boundaries](references/0027-security-supply-chain-and-secret-boundaries.md)
- [Observability, receipts, and recovery](references/0028-observability-receipts-and-recovery.md)
- [Agentic Rust compiler feedback workflow](references/0029-agentic-rust-compiler-feedback-workflow.md)
- [Code review, refactoring, and maintenance](references/0030-code-review-refactoring-and-maintenance.md)
- [Game, desktop, harness, and general application patterns](references/0031-game-desktop-harness-and-general-application-patterns.md)
- [Rust application delivery checklists](references/0032-rust-application-delivery-checklists.md)

## 32. Completion and calibrated claims
R(§32-01) [proof-element from section 32, sentence-level atomic element]
R(§32-02) [proof-element from section 32, sentence-level atomic element]
R(§32-03) [proof-element from section 32, sentence-level atomic element]

Lead the return with the behavior or artifact delivered.
List the relevant changed paths through usable links.
Summarize the tests actually executed and their results.
Keep focused success distinct
from repository-wide gate failures.
Name material untested targets,
features, migrations, and external services.
Report stale historical evidence as historical.
Explain compatibility and recovery
consequences where they affect users.
Preserve a source revision or other narrow recovery route.
Do not claim approved practices merely
because this document recommends them.
Distinguish documented language
guarantees from local engineering conventions.
Use the user's existing authorization
without repeating resolved permission questions.
Ask for a new decision only when a missing
choice or new effect actually requires it.
Do not treat optional future improvements
as unfinished parts of the requested task.
Keep the final explanation concise while
the artifacts contain the detailed evidence.
Use reference 0032 to select the relevant delivery checks.
The terminal state for this package remains
candidate, review-required, and verified: false.
A human can inspect and approve the
enriched source separately from any installation.