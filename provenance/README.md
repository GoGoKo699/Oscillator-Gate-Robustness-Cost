# Source integrity

The [integrity manifest](reference-integrity.json) pins the seven scientific
Python files in [`checks/`](../checks/) and the four canonical reports in
[`references/`](../references/) by SHA-256 and byte count. The verifier checks
the full inventory before and after execution, including unexpected files
and unsupported paths.

The manifest also identifies the exact source commit and original paths for
the five core implementations and four reference reports. Their bytes can be
compared directly with those objects in Git history.

[Reproducibility](../REPRODUCIBILITY.md) describes the assertions, acceptance
policies, and receipts. The [platform comparison](platform-review.json)
records individual floating-point differences and report hashes for its
specified environments; its source paths refer to that recorded snapshot.
