# Performance profiling and benchmarking

## Purpose

Improve a measured user-visible
budget while preserving correctness.
Use this reference when latency, throughput,
allocation, startup, or binary size matters.
The outcome should explain a reproducible
workload and the practical effect of the change.

## Source posture

[Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html) documents optimization configuration.
[black_box](https://doc.rust-lang.org/std/hint/fn.black_box.html) documents a benchmarking aid.
[Criterion](https://bheisler.github.io/criterion.rs/book/) documents statistical benchmarking.
Tool recommendations are optional and
should follow the existing workspace setup.

## Practice

Name the budget before optimizing: latency
percentile, throughput, memory, or startup time.
Measure a representative workload rather
than a convenient synthetic input alone.
Use the same compiler, target, profile,
features, and dependency set for comparisons.
Keep correctness checks around the optimized path.
Profile first to identify the actual bottleneck.
Separate CPU time, allocation,
blocking I/O, and contention.
Avoid unsafe optimization until safe
alternatives and measurements justify the added obligation.
Record machine conditions that materially affect results.

## Worked allocation investigation

Suppose a parser repeatedly allocates a
String for identifiers used only during validation.
Measure allocation count and end-to-end
import latency on representative documents.
Inspect whether borrowed slices can
remain valid through the validation stage.
Keep owned values where data must
survive after the input buffer is released.
Benchmark both valid and rejected inputs
because failure paths can dominate real workloads.
Check whether borrowing retains an
excessively large buffer longer than before.
Run the same correctness fixtures after the change.
Report the observed improvement
and the memory-retention tradeoff.
Do not advertise “zero cost”
merely because the code uses references.

## Benchmark design

Prevent the compiler from
eliminating the operation being measured.
Keep setup and teardown outside the timed
region when they are not part of the question.
Include setup when user-visible
startup is the actual budget.
Use enough repeated measurements to understand noise.
Avoid comparing a warm cache against a
cold cache without labeling the difference.
Use input sizes that reveal scaling behavior.
Check adversarial cases if they can trigger nonlinear work.
Preserve the benchmark code and
exact invocation needed for reproduction.

## Interpretation

Compare distributions rather than a single best run.
Distinguish statistical difference from
a meaningful user-visible improvement.
Look for regressions in memory and tail
latency when average throughput improves.
Do not extrapolate one
machine's result to unsupported targets.
A microbenchmark can explain a mechanism
without predicting whole-application speed.
Inspect whether the optimized branch is
actually hot in the representative workload.
Treat noisy results as inconclusive
instead of choosing the favorable run.
Record absolute values as well as relative percentages.

## Common Rust choices

Reserve collection capacity when a
credible size estimate avoids repeated growth.
Avoid speculative huge
reservations driven by untrusted input.
Use iterators or loops according to
readability and measured behavior.
Check clone cost before removing
clones that encode necessary ownership.
Choose data structures from lookup,
insertion, ordering, and memory needs.
Do not assume hashing always
outperforms an ordered map at small sizes.
Measure monomorphization and binary
size when generic proliferation matters.
Keep debug and release results separate.

## Validation

Run semantic tests before and after optimization.
Benchmark the baseline and
candidate under comparable conditions.
Record toolchain, profile, features,
workload, machine, and sample method.
Include a regression threshold only when the
environment is stable enough to support it.
Test resource limits after changing allocation behavior.
Review overflow checks around size calculations.
Keep raw measurements available for inspection.
State what the benchmark excludes,
such as network latency or UI rendering.

## Limit

A faster microbenchmark does not prove a faster product.
black_box is a best-effort
optimization barrier, not a correctness mechanism.
Performance evidence cannot excuse an
unsound or semantically incorrect implementation.
