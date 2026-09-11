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
R(§01-01) Use this skill for Rust implementation,
diagnosis, review, migration, and test work.
R(§01-02) Start from the requested behavior and
the repository's actual public contract.
R(§01-03) Apply documented Rust semantics to implementation
decisions and test the remaining runtime obligations.
R(§01-04) Treat this package as a review-required engineering candidate.
R(§01-05) The examples and procedures recommend practices;
they do not claim blanket approval by the Rust project.
R(§01-06) The source links identify language guarantees,
library contracts, and project-maintained guidance.
R(§01-07) Framework-specific mappings to external governance systems are proposed
integration guidance with their own source owners; those references are
available in the canonical source but are not part of this public-safe projection.
R(§01-08) Keep these categories explicit whenever a
stronger guarantee would change a decision.
R(§01-09) A successful check supports the named predicate on
the tested source, toolchain, features, and target.
R(§01-10) It does not establish complete
correctness across untested configurations.
R(§01-11) Use the user's existing
authorization for the requested local work.
R(§01-12) Do not transform a documentation or diagnosis
request into an unrelated implementation project.
R(§01-13) When asked to implement, carry the change
through relevant checks and a concrete handoff.
R(§01-14) When asked to review, report evidence-backed
findings without silently repairing unrelated code.
R(§01-15) When asked to diagnose, identify the cause and
reproduction before proposing the smallest correction.
R(§01-16) Read only references relevant to the task after this entrypoint.
R(§01-17) Each reference contains deeper decisions,
examples, failure cases, validation, and limits.
R(§01-18) The reference filenames are stable routes within this package.
## 02. Source and toolchain orientation
R(§02-01) Read the nearest charter, Cargo.toml,
lockfile, affected facade, tests, and one real caller.
R(§02-02) Resolve which directory is the workspace
and which package owns the changed code.
R(§02-03) Record the compiler version, edition, target,
feature set, and minimum supported compiler.
R(§02-04) Do not assume the latest online documentation
describes the compiler selected by the repository.
R(§02-05) Use version-specific documentation or a minimal
compile experiment for uncertain language behavior.
R(§02-06) Inspect rust-toolchain configuration
before invoking a different toolchain.
R(§02-07) A rust-version declaration is a support
commitment to verify, not proof that verification occurred.
R(§02-08) Check build scripts and procedural macros
before compiling unfamiliar dependencies.
R(§02-09) Compilation may execute host code even
when the final application never runs.
R(§02-10) Keep temporary experiments and
build output outside a source-only Hub.
R(§02-11) Use locked dependency resolution to
reproduce an application configuration.
R(§02-12) Treat an offline cache miss as an
environment limitation rather than a Rust defect.
R(§02-13) Inspect the working tree before
editing and preserve other authors' changes.
R(§02-14) Read the direct source when an old
handoff disagrees with the current checkout.
R(§02-15) Record the base identity used for comparison
in a durable receipt when the task needs one.
R(§02-16) Use the smallest source set that settles the decision.
R(§02-17) Do not inspect unrelated private material or
credentials as part of routine orientation.
R(§02-18) Route deeper practice through reference
0001 and the Cargo documentation linked there.
## 03. Translate the request into an engineering contract
R(§03-01) Write the observable behavior in terms
of input, state, operation, and result.
R(§03-02) Replace vague goals such as “robust import”
with explicit accepted and rejected cases.
R(§03-03) Identify the consumer that needs the changed behavior.
R(§03-04) Name the public API or transport
boundary through which the consumer reaches it.
R(§03-05) State which state may change and
what must remain unchanged on rejection.
R(§03-06) Separate structural validation from
domain interpretation and current permission.
R(§03-07) Identify the failure category the caller needs to distinguish.
R(§03-08) Specify relevant limits before designing
allocation, recursion, or queue behavior.
R(§03-09) Use a small transition table when state and
event combinations are the main uncertainty.
R(§03-10) Choose a representative valid
example and a meaningful negative example.
R(§03-11) Keep test oracles independent of the
implementation where a shared bug is plausible.
R(§03-12) Document reversible assumptions
and proceed with independent work.
R(§03-13) Resolve missing product semantics
before changing persisted meaning.
R(§03-14) Do not create abstractions until
their consumer and invariant are clear.
R(§03-15) Select a template only if its fields
improve this task's reproducibility.
R(§03-16) A short task may need only a
clear test and a concise explanation.
R(§03-17) A migration or external-effect
boundary needs explicit recovery semantics.
R(§03-18) Use reference 0001 for decomposition and 0032 for completion.
## 04. Type selection and checked construction
R(§04-01) Use structs for simultaneously
meaningful facts and enums for alternatives.
R(§04-02) Use distinct newtypes when accidentally
interchanging identifiers would be a defect.
R(§04-03) A type alias does not prevent
substitution between identical underlying types.
R(§04-04) Keep invariant-bearing fields
private and check all constructor paths.
R(§04-05) Use TryFrom or another fallible
constructor when some raw values are invalid.
R(§04-06) Reserve From for conversions whose
contract is genuinely infallible.
R(§04-07) Keep untrusted DTOs separate from validated domain values.
R(§04-08) Do not let derived deserialization bypass a checked constructor.
R(§04-09) Use Option when absence has one meaning
and an enum when absence causes differ.
R(§04-10) Select numeric widths from the domain
and protocol rather than the host machine.
R(§04-11) Use checked conversions at width and sign boundaries.
R(§04-12) Define float treatment for NaN, infinity, and
signed zero if those values enter ordering or identity.
R(§04-13) Check equality and hashing together
when implementing either manually.
R(§04-14) Do not derive Default if its value violates
the domain invariant or hides missing input.
R(§04-15) Review mutation methods for
preservation of constructor-established guarantees.
R(§04-16) A value checked once may still require
current-state validation before an effect.
R(§04-17) Keep external authorization outside a purely
structural marker unless the type's lifecycle truly enforces it.
R(§04-18) Use references 0002, 0003, and 0026
for construction and admission details.
## 05. Ownership decisions before borrow fixes
R(§05-01) Identify the owner responsible for
retaining and releasing each resource.
R(§05-02) Borrow when an operation only
inspects data for a bounded duration.
R(§05-03) Move when responsibility transfers to another component.
R(§05-04) Clone when an independent owned copy
is intended and its cost is acceptable.
R(§05-05) Do not use clone as an unexplained
default response to compiler diagnostics.
R(§05-06) Read the start and last use of a conflicting borrow.
R(§05-07) Shorten the borrow, extract a small
owned key, or separate lookup from mutation.
R(§05-08) Avoid retaining a tiny view through a huge
owner when copying would reduce memory pressure.
R(§05-09) Use slices and str for borrowed contiguous views.
R(§05-10) Use owned buffers when values must outlive the original input.
R(§05-11) Do not add static lifetimes to hide an invalid ownership model.
R(§05-12) Use stable identifiers instead of
self-references when that keeps movable structures simple.
R(§05-13) Arc provides shared ownership and does
not make arbitrary inner mutation safe.
R(§05-14) Use synchronization only where mutation is actually shared.
R(§05-15) Break reference-count cycles
through a deliberate ownership design.
R(§05-16) Keep RefCell borrow failures visible as
runtime behavior if interior mutability is chosen.
R(§05-17) Review resource release on early error,
cancellation, and partial construction.
R(§05-18) Use reference 0005 for lifetime and destruction procedures.
## 06. State modeling and transitions
R(§06-01) Represent different payload
requirements with explicit enum variants.
R(§06-02) Keep queued, running, failed, completed, and
unknown outcomes distinct when recovery differs.
R(§06-03) Avoid a status string plus optional
fields that permits contradictory combinations.
R(§06-04) Match explicitly on internal closed
enums to expose new variants at call sites.
R(§06-05) Use wildcard fallbacks only where
extensibility and fallback behavior are deliberate.
R(§06-06) Keep pure transition classification
separate from persistence and dispatch.
R(§06-07) Return the original state on rejection
when the API promises recoverability.
R(§06-08) Check expected revision and attempt
identity before applying asynchronous completion.
R(§06-09) Do not accept stale success merely
because its payload has a valid shape.
R(§06-10) Use runtime state for persistence and heterogeneous collections.
R(§06-11) Use typestate when unavailable
operations materially improve the public API.
R(§06-12) Keep constructors for privileged
states private to the validating component.
R(§06-13) Do not derive Clone for a consumable
capability without a clear duplication policy.
R(§06-14) Treat revocation and expiration as runtime
obligations when they can change externally.
R(§06-15) Test both accepted transitions and
forbidden source-state/event combinations.
R(§06-16) Confirm rejected transitions leave durable state unchanged.
R(§06-17) Persist the transition through the actual
transaction before reporting durable success.
R(§06-18) Use references 0003 and 0006 for the detailed design.
## 07. Traits and abstraction selection
R(§07-01) Start with a concrete implementation unless
a substitution need is already established.
R(§07-02) Introduce a trait for a real port, second
implementation, or useful test boundary.
R(§07-03) Keep methods narrow enough that a fake
represents the actual domain dependency.
R(§07-04) Use associated types for an
implementation-selected related type.
R(§07-05) Use generic parameters where multiple
parameterized implementations are meaningful.
R(§07-06) Place bounds on the method that needs
them rather than every use of a container.
R(§07-07) Choose static dispatch when concrete types are known.
R(§07-08) Choose dyn dispatch for runtime
heterogeneity after checking dyn compatibility.
R(§07-09) Do not assume generic methods, GATs, or async
trait syntax are automatically usable through dyn.
R(§07-10) Specify future Send requirements where callers need them.
R(§07-11) Document ownership, allocation, blocking,
and cancellation behavior beyond the signature.
R(§07-12) Check blanket implementations for
overlap and downstream compatibility.
R(§07-13) Use local wrappers for foreign
integrations constrained by orphan rules.
R(§07-14) Seal traits when external
implementation would undermine a required invariant.
R(§07-15) Avoid sealing merely to enforce an aesthetic preference.
R(§07-16) Compile a real consumer and a second
implementation before declaring the abstraction useful.
R(§07-17) Keep trait laws stated in prose
distinguishable from compiler-enforced bounds.
R(§07-18) Use reference 0004 for GAT and dynamic-interface examples.
## 08. Fixed shape and stronger guarantees
R(§08-01) Use const generics when
compile-time shape matters to the consumer.
R(§08-02) Prefer a slice when a runtime length is sufficient.
R(§08-03) Validate untrusted lengths before
allocating or constructing fixed-size values.
R(§08-04) Check multiplication and
conversion used to compute buffer sizes.
R(§08-05) Do not rely on target-dependent usize
width for a stable wire representation.
R(§08-06) A fixed-size array says nothing about
checksum validity or domain meaning.
R(§08-07) A phantom parameter does not establish a
predicate unless construction actually checks it.
R(§08-08) A sorted wrapper needs mutation methods that preserve ordering.
R(§08-09) A nonempty wrapper needs a defined policy
for consuming or removing its last item.
R(§08-10) Use executable runtime predicates for
value relationships outside the static model.
R(§08-11) Compile uncertain const
expressions on the supported stable compiler.
R(§08-12) Do not advertise unstable
features as universally available Rust.
R(§08-13) Separate arithmetic proof, termination proof,
structural validation, and current authorization.
R(§08-14) A formal theorem needs its
definitions, assumptions, and checker identity.
R(§08-15) A Rust Result return is explicit error
handling rather than a totality proof.
R(§08-16) Keep proof-tool adoption proportionate to a named obligation.
R(§08-17) Use references 0007, 0008, and
0013 for stronger-technique decisions.
## 09. Public API design
R(§09-01) Make ownership and cost visible in
method names, signatures, and documentation.
R(§09-02) Expose only the surface consumers
need through a deliberate facade.
R(§09-03) Keep internal types and dependencies private
unless exposing them is an intentional commitment.
R(§09-04) Document expected errors and panic
conditions for public operations.
R(§09-05) Include a short example that uses the actual exported path.
R(§09-06) Treat lifetime, Send, Sync, and trait
bounds as compatibility commitments.
R(§09-07) A borrowed return may reduce allocation while
imposing new lifetime constraints on callers.
R(§09-08) Consider adding a borrowed accessor
instead of replacing a compatible owned API.
R(§09-09) Use deprecation and a migration example
when removing an established contract.
R(§09-10) Do not expose debug formatting as a stable external format.
R(§09-11) Keep error variants useful for caller recovery
without leaking transport details into pure domain code.
R(§09-12) Review non-exhaustive enums when future variants are expected.
R(§09-13) Check downstream implementations
before adding required trait methods.
R(§09-14) Keep API compatibility separate
from stored-format compatibility.
R(§09-15) Compile a representative downstream crate
when changing exports or generic bounds.
R(§09-16) Measure performance claims rather than
using “zero cost” as a substitute for evidence.
R(§09-17) Use reference 0020 and the Rust
API Guidelines for focused review.
## 10. Crate and workspace boundaries
R(§10-01) Keep domain validation
independent of UI and transport frameworks.
R(§10-02) Use private modules before creating a crate
when ownership does not require separate packaging.
R(§10-03) Create a crate for justified reuse,
dependency isolation, ownership, or build behavior.
R(§10-04) Avoid a common crate that becomes a
dependency sink for unrelated concerns.
R(§10-05) Keep dependency direction acyclic and explicit.
R(§10-06) Use a composition root to connect
concrete adapters to domain ports.
R(§10-07) Read workspace members and
default-members before selecting a check command.
R(§10-08) Inspect resolver and inherited dependencies
rather than assuming every member uses root settings.
R(§10-09) Review cargo tree when an apparently
small change pulls a large dependency family.
R(§10-10) Keep optional integration dependencies
behind documented features where appropriate.
R(§10-11) Treat features as additive configuration where practical.
R(§10-12) Test supported minimal configurations
instead of relying only on all-features.
R(§10-13) Do not assume one all-features build covers
mutually exclusive or target-specific behavior.
R(§10-14) Keep machine-specific paths out of portable manifests.
R(§10-15) Check packaging contents when distribution is part of the task.
R(§10-16) Separate source-only governance
artifacts from generated build output.
R(§10-17) Use references 0019 and 0020 for
architecture and feature policy.
## 11. Error design and diagnostic mapping
R(§11-01) Classify errors according to caller recovery decisions.
R(§11-02) Distinguish malformed input, unsupported version, missing
data, conflict, unavailable dependency, and unknown outcome.
R(§11-03) Keep stable codes separate from human-readable explanation.
R(§11-04) Attach operation context at the
layer that understands its meaning.
R(§11-05) Preserve causal source errors internally where useful.
R(§11-06) Map errors deliberately at each transport boundary.
R(§11-07) Do not expose full debug output or
request bodies to external consumers.
R(§11-08) Use bounded messages when input controls diagnostic text.
R(§11-09) Avoid broad defaults that turn
malformed input into plausible successful data.
R(§11-10) Reserve panic for internal invariant
violations under the project's policy.
R(§11-11) Use Result for expected input and resource failures.
R(§11-12) An expect message should explain why
the operation cannot fail at that point.
R(§11-13) Review panic behavior in destructors and foreign boundaries.
R(§11-14) Do not classify every timeout as safe to retry.
R(§11-15) A conflict can require reloading and a
new decision rather than automatic replay.
R(§11-16) Test codes and structured fields when prose
wording is not part of the compatibility contract.
R(§11-17) Use reference 0021 for implementation and recovery details.
## 12. Serialization admission
R(§12-01) Decode into a raw DTO before
constructing a trusted domain value.
R(§12-02) Validate nested fields and array items
as carefully as the top-level object.
R(§12-03) A closed outer object can still
contain unconstrained nested values.
R(§12-04) Choose unknown-field behavior from the actual boundary contract.
R(§12-05) Use strict rejection for executable control data
when silent misspellings could change behavior.
R(§12-06) Use explicit extension mechanisms where
descriptive records require forward compatibility.
R(§12-07) Do not combine Serde deny_unknown_fields
with unsupported flattening arrangements.
R(§12-08) Keep absent, null, empty, and default
distinct when they carry different meaning.
R(§12-09) Use version tags before interpreting a stored or wire value.
R(§12-10) Prefer unambiguous enum tags for important input boundaries.
R(§12-11) Test untagged enum overlap before relying on variant selection.
R(§12-12) Do not let a derived deserializer
manufacture a checked or privileged type.
R(§12-13) Route admission through fallible conversion.
R(§12-14) Test schema and Rust acceptance
on the same representative cases.
R(§12-15) Ordinary JSON output is not a canonical byte contract by itself.
R(§12-16) Name the canonicalization algorithm
if digests depend on serialization.
R(§12-17) Use reference 0026 for detailed
admission and migration procedures.
## 13. Persistence and migration
R(§13-01) Identify the transaction that owns the durable change.
R(§13-02) Check expected revision when concurrent updates can race.
R(§13-03) Keep schema version and data meaning explicit.
R(§13-04) Do not reinterpret an old numeric field
after changing units without a migration.
R(§13-05) Use checked arithmetic during conversion.
R(§13-06) Preserve a recoverable previous
representation before destructive replacement.
R(§13-07) Verify the backup is readable
before claiming rollback readiness.
R(§13-08) Define whether migration is repeatable,
idempotent, or rejected after completion.
R(§13-09) Test interruption before conversion, before commit,
and after commit where the storage model permits it.
R(§13-10) Separate stored success from a
successful response that was never committed.
R(§13-11) Keep rejected historical records
available for diagnosis within privacy limits.
R(§13-12) Do not replace malformed data with
defaults merely to finish the migration.
R(§13-13) Test old-reader and new-reader
compatibility directions independently.
R(§13-14) Document when rollback cannot reverse external effects.
R(§13-15) Keep source and adapter revisions attached to converted records.
R(§13-16) Use references 0026 and 0028 for recovery and evidence.
R(§13-17) Return the migration's actual
tested range of historical versions.
## 14. Async and task ownership
R(§14-01) Name the component that starts,
observes, and completes each task.
R(§14-02) Avoid detached activity without a recovery or supervision owner.
R(§14-03) Bound queue size and define overload behavior.
R(§14-04) Keep blocking work away from executor
threads through the runtime's supported mechanism.
R(§14-05) Do not hold a lock across await
without a deliberate, reviewed reason.
R(§14-06) Inspect each awaited operation's cancellation behavior.
R(§14-07) Dropping a future can leave partial progress or external work.
R(§14-08) A select loop may repeatedly cancel losing branches.
R(§14-09) Preserve framing and partial I/O state
where cancellation would otherwise lose it.
R(§14-10) Distinguish cancellation request
from confirmed task termination.
R(§14-11) Observe task completion before
releasing resources the task still uses.
R(§14-12) Do not assume dropping a handle cancels its task.
R(§14-13) Use explicit graceful shutdown with
a deadline and a forced-stop outcome.
R(§14-14) Stop accepting work before draining outstanding operations.
R(§14-15) Keep cancellation and unknown completion visible to the caller.
R(§14-16) Use reference 0023 and the
actual locked runtime's documentation.
R(§14-17) Test overload, task failure, late reply, and shutdown races.
## 15. Concurrency and shared state
R(§15-01) Choose shared mutation only when ownership cannot remain local.
R(§15-02) Arc shares ownership but requires
appropriate inner synchronization for mutation.
R(§15-03) A mutex is often clearer than an ad hoc atomic protocol.
R(§15-04) Use read-write locks only when the
workload and contention justify them.
R(§15-05) Keep critical sections short.
R(§15-06) Do not call unknown or reentrant code
while holding a lock without a clear contract.
R(§15-07) Define behavior after poisoning rather
than blindly assuming invariants survived.
R(§15-08) Keep atomic-ordering arguments
beside the invariant they protect.
R(§15-09) Use compare-and-swap or transactions
where stale state would overwrite newer state.
R(§15-10) Test stale attempt completions and duplicate event delivery.
R(§15-11) Do not infer exactly-once behavior from a single process mutex.
R(§15-12) Consider Loom for small synchronization
algorithms with meaningful schedule exploration.
R(§15-13) Use the instrumentation required by the model.
R(§15-14) Separate modeled schedules from process crash
or remote-service behavior excluded by the test.
R(§15-15) Keep task and resource ownership visible during shutdown.
R(§15-16) Measure contention before
introducing more complex synchronization.
R(§15-17) Use references 0023 and 0028 for lifecycle and recovery.
## 16. Performance decisions
R(§16-01) Begin with a user-visible budget
rather than an optimization technique.
R(§16-02) Measure latency, throughput, allocation, memory,
startup, or binary size according to the actual problem.
R(§16-03) Profile representative workloads before changing hot-path code.
R(§16-04) Keep compiler, target, profile,
features, and dependencies comparable.
R(§16-05) Separate CPU work from blocking I/O and queue wait.
R(§16-06) Avoid comparing debug and release results
as if they measured the same configuration.
R(§16-07) Prevent benchmark elimination while preserving realistic inputs.
R(§16-08) Include setup only when it belongs to the user-visible budget.
R(§16-09) Test valid and rejected inputs when both occur in practice.
R(§16-10) Compare distributions and absolute
values rather than one favorable run.
R(§16-11) Check memory and tail-latency
regressions when average throughput improves.
R(§16-12) Do not trade soundness for an unmeasured speed claim.
R(§16-13) Review retained owners when
replacing owned values with borrowed slices.
R(§16-14) Bound reservations derived from untrusted lengths.
R(§16-15) Keep raw measurements and reproducible commands available.
R(§16-16) Use reference 0024 for benchmark design and interpretation.
R(§16-17) Run semantic tests around every optimized path.
## 17. Unsafe and FFI review
R(§17-01) Prefer safe code when it satisfies the measured requirement.
R(§17-02) Name every invariant the compiler cannot verify.
R(§17-03) Keep unsafe blocks small and justify the exact operation.
R(§17-04) Separate caller obligations of unsafe functions
from obligations inside their implementations.
R(§17-05) Review validity, alignment,
initialization, aliasing, ownership, and lifetime.
R(§17-06) Do not construct references from foreign
pointers solely because a foreign call returned success.
R(§17-07) Check pointer-length arithmetic
and complete allocation validity.
R(§17-08) Keep allocator ownership and release functions compatible.
R(§17-09) Define ABI, layout, target assumptions, and unwind behavior.
R(§17-10) Do not rely on ordinary Rust layout
matching a foreign representation.
R(§17-11) Review Clone, Drop, Send, and Sync together for wrapper types.
R(§17-12) Ensure safe public methods cannot
invalidate hidden raw-pointer assumptions.
R(§17-13) Do not rely on destructors always running for memory safety.
R(§17-14) Use Miri or sanitizers where
supported, recording excluded paths.
R(§17-15) Treat a passing tool run as bounded
evidence rather than proof of soundness.
R(§17-16) Keep an unsafe ledger with location,
invariant, tests, and removal condition.
R(§17-17) Use reference 0025 before modifying the trusted boundary.
## 18. Procedural macros
R(§18-01) Demonstrate the repeated
handwritten Rust before introducing a macro.
R(§18-02) Prefer ordinary functions or
declarative macros for simpler cases.
R(§18-03) Define the accepted syntax and supported item kinds.
R(§18-04) Separate parsing, semantic checking, and token emission.
R(§18-05) Retain spans so failures point to user input.
R(§18-06) Return intentional compile
diagnostics instead of internal panics.
R(§18-07) Preserve generics, where clauses, and unrelated attributes.
R(§18-08) Use explicit generated paths and test renamed dependencies.
R(§18-09) Check collisions with user identifiers and helper names.
R(§18-10) Treat proc macros as host-executed dependencies.
R(§18-11) Avoid hidden environment, filesystem, or network inputs.
R(§18-12) Test the parser separately and compile a downstream consumer.
R(§18-13) Include unsupported syntax and missing or duplicate attributes.
R(§18-14) Inspect representative expansion for
readability and unexpected allocation.
R(§18-15) Version syntax changes as part of the macro's public contract.
R(§18-16) A macro emits Rust and does not
strengthen rustc's underlying type theory.
R(§18-17) Use reference 0009 for architecture and failure fixtures.
## 19. Declarative macros
R(§19-01) Choose a macro only where syntactic repetition requires one.
R(§19-02) Use deliberate fragment specifiers and unambiguous separators.
R(§19-03) Document expression evaluation count and ownership transfer.
R(§19-04) Bind expressions once when
repeated evaluation would be surprising.
R(§19-05) Keep temporary names scoped through a block expression.
R(§19-06) Use defining-crate paths for exported
helper references where appropriate.
R(§19-07) Test downstream expansion without convenient local imports.
R(§19-08) Check adversarial local identifiers and helper visibility.
R(§19-09) Handle empty, single, multiple, and trailing-separator inputs.
R(§19-10) Avoid broad matcher arms that hide malformed syntax.
R(§19-11) Review edition-sensitive fragment behavior.
R(§19-12) Do not return from or mutate the caller unexpectedly.
R(§19-13) Keep generated bounds and errors
understandable at the call site.
R(§19-14) Compare growing syntax complexity with a
proc macro or ordinary data constructors.
R(§19-15) Compile both accepted and rejected examples.
R(§19-16) Use reference 0010 for the worked single-evaluation example.
R(§19-17) Do not describe hygienic expansion
as proof of algorithm correctness.
## 21. Proof and formal-language boundaries
R(§21-01) Name the obligation before selecting a formal technique.
R(§21-02) Rust newtypes can prevent identifier interchange.
R(§21-03) Checked constructors can establish bounded input invariants.
R(§21-04) Typestate can restrict operation availability.
R(§21-05) Ordinary Rust compilation does not prove
arbitrary termination or mathematical truth.
R(§21-06) A Lean proof must name definitions,
assumptions, theorem, and environment.
R(§21-07) Distinguish a proof object from a
report stating that a check passed.
R(§21-08) Bind evidence to source identity
and the precise proposition instance.
R(§21-09) A certificate schema does not verify the certificate's truth.
R(§21-10) Keep untrusted decoded evidence
separate from trusted witness construction.
R(§21-11) Reject stale digest, mismatched predicate,
unsupported verifier, and missing assumptions.
R(§21-12) Bound verification resources and classify
timeout as unavailable or indeterminate evidence.
R(§21-13) Keep runtime authorization separate
from structural or arithmetic proof.
R(§21-14) Do not advertise a bridge as implemented
before exercising the actual verifier and consumer.
R(§21-15) Treat Haskell and Idris concepts as
orientation, not automatic Rust equivalence.
R(§21-16) Use references 0008 and 0013 for
detailed comparison and certificate design.
R(§21-17) Record all remaining assumptions in the result.
## 24. Application adapters and deterministic core
R(§24-01) Keep rendering and input translation outside domain rules.
R(§24-02) Represent commands explicitly and
validate them at the domain boundary.
R(§24-03) Use a headless path for testing pure transitions.
R(§24-04) Inject clocks, randomness, and
I/O where reproducibility matters.
R(§24-05) Keep simulation time separate from wall-clock time.
R(§24-06) Record external inputs needed for replay.
R(§24-07) Do not assume deterministic
cross-platform behavior without relevant evidence.
R(§24-08) Keep long-running work off a UI thread
through the supported framework mechanism.
R(§24-09) Closing a view is not proof that its background task stopped.
R(§24-10) Use stable operation identity for progress and cancellation.
R(§24-11) Keep CLI human output separate from machine-readable output.
R(§24-12) Treat exit codes as a documented interface.
R(§24-13) Validate worker replies as strictly as requests.
R(§24-14) Keep framing, size, timeout, and queue limits explicit.
R(§24-15) Test adapter mappings in addition to the shared domain types.
R(§24-16) Use reference 0031 for game, desktop, CLI, and harness patterns.
R(§24-17) State which platform behavior was actually exercised.
## 25. Test selection by claim
R(§25-01) Choose the test layer from the failure mechanism.
R(§25-02) Use unit tests for pure decisions.
R(§25-03) Use integration tests for
producer-consumer and persistence boundaries.
R(§25-04) Use compile-fail tests for intentionally unavailable operations.
R(§25-05) Use property tests for meaningful
invariants over many combinations.
R(§25-06) Use fuzzing for malformed-input spaces.
R(§25-07) Use concurrency model exploration
for interleaving-sensitive algorithms.
R(§25-08) Do not write tests that simply mirror
the implementation's branch structure.
R(§25-09) A round trip can pass when encoder and decoder share a defect.
R(§25-10) Include independent expected values or another useful oracle.
R(§25-11) Check that test filters execute the intended nonzero case count.
R(§25-12) Keep positive companions for negative tests.
R(§25-13) A rejection-only suite can accidentally
approve an implementation that rejects everything.
R(§25-14) Record generated-test seeds and minimized counterexamples.
R(§25-15) Keep live external effects out of fuzz targets.
R(§25-16) Use reference 0022 for layer selection and evidence limits.
R(§25-17) Stop expanding tests when the relevant
uncertainty is resolved and required checks pass.
## 26. Compiler feedback loop
R(§26-01) Run the narrow check before broad repository commands.
R(§26-02) Read the first causal error and the source it identifies.
R(§26-03) Explain the mismatch in terms of
types, ownership, bounds, or configuration.
R(§26-04) Do not add clone, static, unsafe, or
broad lint suppression without a reason.
R(§26-05) Inspect dependency versions when an expected API is unavailable.
R(§26-06) Separate linker errors from Rust type errors.
R(§26-07) Separate a lint suggestion from a semantic requirement.
R(§26-08) Apply a focused correction and rerun the same relevant check.
R(§26-09) Do not execute an old binary after a failed build.
R(§26-10) Keep compiler and feature selection stable across comparisons.
R(§26-11) Use a minimal isolated example
for a difficult language question.
R(§26-12) Preserve tests that encode the requested contract.
R(§26-13) Do not weaken acceptance merely to obtain a green result.
R(§26-14) Review the final diff after formatting and generated changes.
R(§26-15) Report unresolved warnings and baseline failures precisely.
R(§26-16) Use reference 0029 for diagnostic triage.
R(§26-17) A compiler pass must be followed by
behavioral evidence for a behavioral claim.
## 27. Reproducible command patterns
R(§27-01) Substitute the actual package name and
supported features in these patterns.
R(§27-02) Run commands from the inspected workspace root.
R(§27-03) Do not copy the placeholder PACKAGE
literally into a completion receipt.
R(§27-04) A locked command should fail rather
than silently change dependency resolution.
R(§27-05) Use offline only when cached dependencies are sufficient.
R(§27-06) Keep build output in the repository's allowed
target location or an external scratch target.
R(§27-07) Record exit status and executed
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
R(§27-08) The Clippy pattern uses warnings-as-errors
only when that matches the project's gate.
R(§27-09) Do not claim every target or
feature was covered by these examples.
R(§27-10) Select the required supported
matrix from the actual package contract.
R(§27-11) A missing target toolchain is a
recorded limitation, not a passing test.
R(§27-12) Use direct rustc examples for isolated language
experiments when dependencies are unnecessary.
R(§27-13) Keep generated binaries and temporary sources outside the Hub.
R(§27-14) Record whether a command was a syntax check,
compilation, execution, or packaging operation.
## 28. Security and dependency checks
R(§28-01) Identify attacker-controlled input
and the resources it can influence.
R(§28-02) Validate sizes before allocation and recursion.
R(§28-03) Keep authorization at the effect-owning component.
R(§28-04) Inspect new dependencies, transitive
changes, build scripts, and proc macros.
R(§28-05) Check current advisories against the
resolved versions when dependency risk is in scope.
R(§28-06) A lockfile makes resolution
inspectable but does not establish trust.
R(§28-07) Keep secrets out of logs, examples, fixtures, and receipts.
R(§28-08) Use synthetic values for redaction tests.
R(§28-09) Avoid full environment dumps during configuration diagnosis.
R(§28-10) Review Debug implementations on secret-bearing types.
R(§28-11) Use structured arguments instead of
shell interpolation for untrusted values.
R(§28-12) Treat filesystem normalization and
race resistance as separate concerns.
R(§28-13) Do not claim a clean advisory scan is a full security audit.
R(§28-14) Record concrete findings and untested surfaces.
R(§28-15) Use reference 0027 for the dependency and input workflow.
R(§28-16) Do not retrieve real credentials
merely because a test could use them.
R(§28-17) Scope any additional security work to
the actual task and threat boundary.
## 29. Observability and recovery evidence
R(§29-01) Record request and attempt identity before consequential work.
R(§29-02) Keep source-event time distinct from observation time.
R(§29-03) Use monotonic time for in-process durations.
R(§29-04) Keep structured fields useful for
correlation without exposing full private payloads.
R(§29-05) Avoid unbounded metric labels.
R(§29-06) Separate queue wait from execution time when diagnosing latency.
R(§29-07) Record the last confirmed durable state.
R(§29-08) Distinguish not-started, running, failed,
cancelled, completed, and indeterminate as needed.
R(§29-09) A timeout does not prove a remote operation failed.
R(§29-10) Reconcile unknown outcomes before creating a new attempt.
R(§29-11) Prevent late completions from overwriting newer state.
R(§29-12) Keep receipts attached to the
source and configuration they checked.
R(§29-13) Report skipped and unavailable checks distinctly from failures.
R(§29-14) Do not let a receipt grant the next operation automatically.
R(§29-15) Test recovery before and after dispatch and commit.
R(§29-16) Use reference 0028 for traces, receipts, and restart behavior.
R(§29-17) A useful receipt supports reconstruction without
requiring unrestricted access to private material.
## 30. Review and refactoring
R(§30-01) Read the intended behavior before evaluating the diff.
R(§30-02) Trace validation, state change, persistence, and output.
R(§30-03) Review failure paths and supported feature configurations.
R(§30-04) Prioritize concrete correctness
defects over aesthetic preferences.
R(§30-05) Explain the triggering condition
and consequence for each finding.
R(§30-06) Use exact source evidence or a reproduction.
R(§30-07) State uncertainty when a necessary
external contract is unavailable.
R(§30-08) Keep optional improvements separate from blocking defects.
R(§30-09) Prefer behavior-preserving extraction before semantic change.
R(§30-10) Check public visibility and
dependency leakage after moving code.
R(§30-11) Watch for changed drop order and lifetime requirements.
R(§30-12) Do not repair unrelated code during a review-only request.
R(§30-13) Run the relevant consumer tests after restructuring.
R(§30-14) Review the final generated or formatted diff.
R(§30-15) Return no findings when the evidence supports none.
R(§30-16) Use reference 0030 for review quality and maintenance tradeoffs.
R(§30-17) A bounded review cannot prove the absence of every defect.
## 31. Package resources and practical use
R(§31-01) The references directory contains
27 public-safe focused supporting notes (governance-framework references omitted per the project release).
R(§31-02) Use the reference whose trigger matches the
decision rather than loading all notes by default.
R(§31-03) The schemas directory describes
candidate input and evidence shapes.
R(§31-04) Run a real instance validator before
claiming a fixture satisfies a schema.
R(§31-05) The fixtures directory should contain
accepted and rejected cases with expected outcomes.
R(§31-06) Parsing a fixture file proves only that it is valid JSON.
R(§31-07) The Rust templates are adaptation
starting points, not preapproved implementations.
R(§31-08) Compile a copied template after
supplying the real domain types and behavior.
R(§31-09) The general templates should capture
task-specific decisions rather than remain empty headings.
R(§31-10) Keep source-lock values concrete
before using them for integrity claims.
R(§31-11) Use package validation to check
counts, routes, and required structure.
R(§31-12) Use behavioral example checks to test
the included standalone Rust snippets.
R(§31-13) Use reference-closure checks to
catch missing or incorrect local links.
R(§31-14) Keep the atlas and public-safe projection
synchronized with current source.
R(§31-15) Regenerate digests only after
source and generated outputs are final.
R(§31-16) A digest match proves byte identity, not semantic quality.
R(§31-17) Keep candidate status and the
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
R(§32-01) Lead the return with the behavior or artifact delivered.
R(§32-02) List the relevant changed paths through usable links.
R(§32-03) Summarize the tests actually executed and their results.
R(§32-04) Keep focused success distinct
from repository-wide gate failures.
R(§32-05) Name material untested targets,
features, migrations, and external services.
R(§32-06) Report stale historical evidence as historical.
R(§32-07) Explain compatibility and recovery
consequences where they affect users.
R(§32-08) Preserve a source revision or other narrow recovery route.
R(§32-09) Do not claim approved practices merely
because this document recommends them.
R(§32-10) Distinguish documented language
guarantees from local engineering conventions.
R(§32-11) Use the user's existing authorization
without repeating resolved permission questions.
R(§32-12) Ask for a new decision only when a missing
choice or new effect actually requires it.
R(§32-13) Do not treat optional future improvements
as unfinished parts of the requested task.
R(§32-14) Keep the final explanation concise while
the artifacts contain the detailed evidence.
R(§32-15) Use reference 0032 to select the relevant delivery checks.
R(§32-16) The terminal state for this package remains
candidate, review-required, and verified: false.
R(§32-17) A human can inspect and approve the
enriched source separately from any installation.