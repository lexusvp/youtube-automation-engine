# YouTube Automation Engine

Local-first AI-assisted automation for planning, generating, approving, scheduling, publishing and analytics.

## Status

**Prototype / production-readiness pass.** The core now validates configuration, guards publish inputs, validates timezone-aware schedules, retries transient YouTube API failures, provides a no-network dry-run command, and runs tests in GitHub Actions. Autonomous live publishing remains gated.

## Flow

research -> plan -> AI draft -> moderation -> human approval -> schedule -> publish -> analytics

AI creates drafts; humans approve final publishing.

## Structure

- `src/ai.py` — AI package generation and deterministic fallback
- `src/cli.py` — research, package and dry-run commands
- `src/config.py` — validated environment configuration
- `src/content.py` — queue and approval selection
- `src/youtube.py` — OAuth upload, validation, scheduling and retries
- `src/models.py`, `src/planner/`, `src/moderation/` — platform-neutral boundaries
- `src/platforms/meta/` — Meta adapter
- `src/analytics/` — analytics interface
- `docs/ARCHITECTURE.md` — architecture
- `docs/OPERATIONS.md` — operations
- `docs/ISSUES.md` — prioritized production-readiness work
- `.github/workflows/ci.yml` — test and CLI smoke gate

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
pytest -q
python -m src.cli research --count 5
python -m src.cli package --topic "AI automation"
python -m src.cli dry-run --topic "AI automation"
```

## Configuration

Secrets belong in local `.env` or GitHub Actions Secrets only.

YouTube:
- `UPLOAD_PRIVACY=private|unlisted|public`
- `VIDEO_CATEGORY` must be a positive integer
- `SCHEDULED_PUBLICATION=false` by default
- scheduled uploads require ISO-8601 timestamps with timezone

AI:
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

## CI

Every push and pull request runs pytest plus a no-network CLI smoke test.

## Production gate

Before autonomous live publishing: validate OAuth scopes and permissions, use a protected production environment, add persistent approval/audit state, and perform a staging/test publish.

See `docs/ISSUES.md`.
