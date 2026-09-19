# Social Automation Engine

Local-first, platform-neutral AI content automation. MVP starts with Meta (Facebook Page + Instagram) and keeps planning, moderation, approval, scheduling, publishing, and analytics separated.

## MVP flow

research -> plan -> draft -> moderation -> human approval -> schedule -> Meta adapter -> analytics

AI creates drafts. **Humans approve final publishing.** Dry-run is the default.

## Structure

- `src/models.py` — shared content state
- `src/planner/` — platform-neutral planning
- `src/moderation/` — policy checks and publish gate
- `src/platforms/meta/` — Meta Graph API adapter
- `src/analytics/` — analytics interfaces
- `docs/ARCHITECTURE.md` — system boundaries and state machine
- `docs/OPERATIONS.md` — secrets, dry-run and incident procedures
- `.github/workflows/` — CI and scheduled Meta jobs

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
pytest -q
python -m src.cli research --count 5
```

## Secrets

Use local environment variables or GitHub Actions Secrets only. Never commit API keys, OAuth tokens or refresh tokens.

Meta runtime secrets:
- META_ACCESS_TOKEN
- META_PAGE_ID
- META_IG_USER_ID
- META_GRAPH_VERSION (optional)

AI:
- OPENAI_API_KEY
- OPENAI_MODEL (optional)

## GitHub schedules

- Weekly planning: Monday
- Analytics pull: Tuesday
- Publishing workflow: manual dispatch with dry-run enabled

Live publishing should remain disabled until the Meta app, account permissions, token, and test post have been validated.

## Adding platforms

Implement `PlatformAdapter` under `src/platforms/<platform>`. Do not put platform-specific API calls into the planner or moderation service.

## License

MIT
