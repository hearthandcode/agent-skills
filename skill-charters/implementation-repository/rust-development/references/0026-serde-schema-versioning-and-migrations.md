# Serde, schema versioning, and migrations

## Purpose

Make wire admission and persisted evolution explicit.
Use this reference when deriving
serialization, accepting JSON, or changing stored schemas.
The result should preserve meaning across
boundaries and reject malformed authority-bearing input.

## Source posture

[Serde container attributes](https://serde.rs/container-attrs.html) documents unknown-field and conversion controls.
[Serde enum representations](https://serde.rs/enum-representations.html) documents tagging choices.
[JSON Schema validation](https://json-schema.org/draft/2020-12/json-schema-validation.html) defines validation keywords.
The contract below is a local design
recommendation that must match
the actual producer and consumer.

## Practice

Use a dedicated raw DTO before
constructing validated domain values.
Choose unknown-field behavior from the
boundary's compatibility and safety requirements.
Reject unknown authority-bearing fields
rather than silently ignoring a misspelled control.
For extensible descriptive records,
define an explicit extension mechanism.
Do not combine deny_unknown_fields
with unsupported flattening patterns.
Route checked values through fallible
conversion instead of bypassing constructors.
Version stored meaning explicitly.
Define missing, null, empty, and default as
separate cases where the domain distinguishes them.

## Worked migration

Suppose version 1 stores a timeout as
integer seconds and version 2 uses milliseconds.
Read the version before interpreting the numeric field.
Convert using checked multiplication and reject overflow.
Preserve the original record or a
reversible backup before replacing stored data.
Test zero, a normal value, the maximum
supported value, and an overflow case.
Define whether missing timeout
inherits a default or remains unspecified.
Write a version 2 record only after
successful conversion and validation.
Test reading old and new records through the actual consumer.
Do not rename the field without
acknowledging the unit and compatibility change.

## Shape versus meaning

A schema's string type does not prove
the string contains a valid identifier.
A top-level closed object can still
contain unconstrained nested objects.
Validate array items, numeric bounds,
nested required fields, and allowed variants.
Use minimum lengths only when
empty values are semantically invalid.
Keep cross-field constraints in a named
validator when the schema cannot express them clearly.
Compare schema acceptance with Rust deserialization acceptance.
Test extra fields, wrong types,
unsupported tags, and malformed nested values.
Avoid claiming canonical bytes from ordinary serializer output.

## Enum and compatibility choices

Choose tagging that makes variant
selection unambiguous for consumers.
Untagged enums can accept overlapping shapes in surprising ways.
Test ambiguity before using untagged
decoding for security-relevant input.
Do not use default variants to
hide unsupported protocol versions.
Preserve stable wire names when internal Rust names change.
A newly added optional field may still
change behavior if its default has meaning.
Keep old-reader and new-reader
compatibility requirements explicit.
Distinguish source compatibility
from persisted-data compatibility.

## Migration operations

Use a transaction or staged replacement
when partial writes would corrupt state.
Record migration identity and source version for recovery.
Make repeated execution either safe or explicitly rejected.
Test interruption before write, during
conversion, and after commit where feasible.
Validate backups by reading them
before claiming rollback readiness.
Avoid destructive cleanup until the
replacement is verified within the authorized workflow.
Preserve rejected records for diagnosis within privacy limits.
Do not silently reinterpret
malformed old records as valid defaults.

## Validation

Run a real schema validator on
instances, not merely parse the schema JSON.
Check the schema itself against its declared draft.
Pair each invalid fixture with the expected failed predicate.
Test Rust and schema admission
against the same representative cases.
Exercise migration round trips
only where reversibility is promised.
Include independent expected outputs so
shared encoder-decoder bugs do not pass unnoticed.
Record schema, adapter, and migration versions.
Keep untested compatibility directions visible.

## Limit

Schema validity does not establish
provenance, authorization, or truth.
Serde derives cannot enforce a domain
invariant unless the admission path includes it.
A successful migration test covers its
fixtures, not every historical record.
