# Guiding principles: calledtoconstruct/pair-columbus-api

## Purpose and scope
A small Flask app from a pairing session that shows a random Maltese dog picture from dog.ceo.

## Stack and layout
Python: `api.py` (Flask app and `get_random_maltese`), pytest tests in `tests/test_api.py`. No requirements file.

## Commands
| Check | Command | Evidence |
|---|---|---|
| Setup | Not documented; the code imports flask and requests, tests import pytest | api.py, tests/test_api.py |
| Tests | `pytest tests/test_api.py` (pytest-style tests; they call the live dog.ceo API) | tests/test_api.py |
| Build / lint | None | - |
| CI | None | repository tree |

Commands marked as not written down come from the build files, not from project docs; confirm them before relying on them.

## Before every push
Before every push: run the build and type-check/lint that exist here, plus only the tests for the files or feature you changed (team rule, ideas #14 note 6797). Do not run the full suite locally as a routine gate; this repository has no CI that runs the full suite, so run the full suite only when the change is broad, and say in the PR that CI coverage is missing. Merge needs a positive review. Explain any new failure your change caused. Never weaken a valid test to make it pass, and never invent a command this file does not list.

## Project rules
- Tests need internet access; say so when they fail for network reasons rather than changing assertions.
- Keep it a minimal example.

## What to avoid
- Committing to the default branch; work on a branch and open a pull request.
- Deleting files, branches or history, or changing repository settings.
- Adding tooling, CI or dependencies that the change does not need.
- Rules copied from other projects (file-size limits, clocks, quotas) that this repository never adopted.

## Delivery and safety
- Nothing is deployed.

## Open questions
- No requirements file or README.

## Sources
Read from the `master` branch on 2026-11-08 ET: `api.py`, `tests/test_api.py`.

## Instruction updates
Check `guiding-principles.version` at the start of each turn and when you enter this project; reload this file when the version changes. Change this file, its version and date, and `PRINCIPLES_HISTORY.md` in the same commit. Team-wide role instructions are versioned separately in the team-process repository.
