# Rust application delivery checklists

## Purpose

Close an engineering change with
evidence appropriate to its actual risk.
Use this reference when preparing a handoff,
release candidate, or completed implementation report.
The checklist should identify remaining uncertainty
without turning every small change into a release program.

## Source posture

[Cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) documents test execution.
[Cargo package](https://doc.rust-lang.org/cargo/commands/cargo-package.html) documents package preparation.
[Rustdoc tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) documents example checks.
Select checks according to the
requested change and repository requirements.

## Practice

State the concrete behavior delivered.
Identify changed public contracts, stored
formats, dependencies, and configuration.
Review the final diff for unrelated or accidental changes.
Run formatting and relevant compiler checks.
Run behavior tests that exercise the changed invariant.
Check documentation examples when the public API changed.
Record unsupported or untested configurations.
Keep approval and publication separate from local
validation when those effects were not requested.

## Worked parser delivery

Suppose a parser now rejects duplicate normalized IDs.
Report the accepted and rejected
behavior in one clear sentence.
List the targeted regression and valid-path tests.
State whether wire admission and
downstream storage were exercised.
Record the compiler and feature configuration.
Explain any migration consequence
for previously stored duplicates.
Include a recovery route if the new rule blocks historical data.
Do not claim all parser inputs are
safe because a finite fixture set passed.
Link the changed source and relevant receipt for inspection.

## Configuration matrix

Check the package's default configuration.
Check minimal features when the package supports them.
Check supported optional integrations touched by the change.
Do not assume all-features
represents every meaningful combination.
Run the minimum supported compiler before making an MSRV claim.
Cross-compile and execute on target
separately where platform support is promised.
Keep unavailable environments visible
rather than fabricating successful coverage.
Use existing CI requirements as the
baseline for repository-wide gates.

## Data and recovery

Test migration from supported
historical versions when stored meaning changes.
Verify rollback data is readable
before claiming recovery readiness.
Define behavior for partial writes and interrupted operations.
Check idempotency or duplicate
handling where retries are possible.
Preserve attempt identity for uncertain external outcomes.
Keep source backups or Git revision
locators sufficient to reproduce the prior version.
Do not remove historical data merely
because the new code no longer uses it.
Document irreversible consequences
before a separately authorized release.

## Documentation and packaging

Update the public example to show the changed behavior.
Document errors and compatibility consequences.
Inspect package contents if distributing a crate or binary.
Exclude credentials, caches, temporary
outputs, and unrelated private sources.
Record required runtime resources and target assumptions.
Do not equate a successful package
build with installation or deployment.
Keep generated projections
synchronized with their source revision.
Label historical receipts so users do
not mistake them for current checks.

## Final verification

Record command, exit status,
executed cases, and material warnings.
Distinguish focused success from repository-wide failures.
State which checks were skipped and why.
Confirm no zero-test filter was mistaken for a behavioral pass.
Review changed files after formatting or generation.
Check links in the handoff and generated review surface.
Summarize the remaining risk in terms of user behavior.
Stop when the requested outcome
and relevant checks are complete.

## Acceptance boundary

A completed local change can remain a review-required candidate.
A machine pass cannot supply a missing human semantic decision.
Existing user authorization should be used
without repeatedly requesting the same permission.
A new external effect needs authority only
when it falls outside that authorization.
Keep the next action concrete, such as reviewing a
migration result or running a target-specific test.
Do not append speculative future work
as though it were part of completion.

## Limit

This checklist proves only the checks actually performed.
Release readiness depends on the
application's real operational and review requirements.
A documentation update does not
establish newly implemented runtime behavior.
