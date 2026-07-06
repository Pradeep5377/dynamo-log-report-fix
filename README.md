# Terminal-Bench 2 (Harbor) – Log Report Fix

This repository contains my fixes for the Project Dynamo Harbor task.

## Changes made

- Fixed `task.toml`
  - Corrected `artifacts` format.
  - Updated artifact path.
  - Disabled unnecessary internet access.

- Fixed Docker environment
  - Removed solution leakage.
  - Updated Docker image configuration.

- Improved verifier
  - Validates JSON contents instead of file existence.
  - Writes `reward.txt` and `ctrf.json`.

- Rewrote task instructions
  - Added clear success criteria.
  - Matched verifier expectations.

## Validation

Oracle:

```
Reward = 1.0
```

No-op:

```
Reward = 0.0
```

This confirms the verifier correctly distinguishes a valid solution from a no-op agent.
