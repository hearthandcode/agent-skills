# Code review, refactoring, and maintenance

## Purpose

Review changes for observable defects and
preserve behavior during structural improvement.
Use this reference when assessing a diff,
extracting modules, or paying down local maintenance debt.
The result should prioritize
actionable risks over stylistic preference.

## Source posture

[API guidelines](https://rust-lang.github.io/api-guidelines/checklist.html) provides design recommendations.
[Cargo SemVer](https://doc.rust-lang.org/cargo/reference/semver.html) provides compatibility guidance.
The review procedure here is local engineering advice.
Use the actual diff, tests, and
consumers as primary evidence for a finding.

## Practice

Read the stated behavior change
before judging implementation details.
Trace input through validation,
state change, persistence, and output.
Review failure paths with the same
attention as the successful path.
Check ownership, public
compatibility, concurrency, and resource limits.
Separate a concrete defect from
an optional design improvement.
Attach a finding to the smallest relevant
location and explain the triggering condition.
Do not repair unrelated code during a review-only task.
Preserve existing dirty work and
identify overlapping ownership before editing.

## Worked refactor review

Suppose a validator is moved from a
desktop command into a domain module.
Compare accepted and rejected
inputs before and after the move.
Check whether the adapter still
calls the validator before persistence.
Verify that error codes remain stable.
Inspect whether a convenience
default was introduced during extraction.
Run tests through the command
boundary as well as the domain function.
Check that the new module does
not import desktop framework types.
Review public visibility changes caused by the move.
A file reorganization is not behavior-preserving
merely because the function body looks similar.

## Finding quality

Describe a concrete input, state, or
configuration that triggers the defect.
Explain the user-visible or operational consequence.
Use evidence from the changed
code or a reproducible check.
Avoid hypothetical failures
requiring unsupported assumptions.
State uncertainty when an
external contract is unavailable.
Prioritize data loss, authorization defects,
unsoundness, and broken supported behavior.
Keep style suggestions separate
from blocking correctness findings.
Do not claim a clean review
proves the absence of all defects.

## Refactoring discipline

Prefer behavior-preserving
extraction before changing semantics.
Keep public API changes deliberate and documented.
Use existing tests as a baseline but add a
targeted case when coverage misses the moved boundary.
Avoid broad renaming that obscures a small functional fix.
Preserve error distinctions and
ordering where consumers rely on them.
Check trait bounds and lifetimes after moving generic code.
Watch for changed drop order
when restructuring owned fields.
Review feature-gated paths that ordinary local tests omit.

## Maintenance decisions

Remove dead code only after checking
generated callers and feature configurations.
Do not add a generic framework
for a single local recurrence.
Update examples and documentation with the changed API.
Keep dependency upgrades separate when
they introduce independent compatibility risk.
Record a durable design rationale only for
decisions future maintainers must understand.
Prefer a narrow correction over
accumulating universal rules from one incident.
Use deprecation when consumers need a transition period.
Keep historical receipts
attached to their original revision.

## Validation

Run relevant behavior tests and compile affected consumers.
Check diff whitespace and
formatting without rewriting unrelated files.
Exercise supported features touching the changed path.
Use a negative test for the defect the
refactor could accidentally reintroduce.
Review the final diff after mechanical tooling.
Confirm documentation examples still compile.
Report tests actually run and material gaps.
Return no findings when evidence
does not support an actionable defect.

## Limit

Review is a bounded examination,
not a guarantee of correctness.
Passing tests cannot substitute for
understanding the changed contract.
Refactoring authority does not imply permission
to change product semantics or publish a release.
