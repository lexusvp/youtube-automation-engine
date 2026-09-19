# Social Automation MVP Architecture

signals -> planner -> draft -> moderation -> human approval -> scheduler -> adapter -> analytics

## Boundaries
- Brand profile: voice, audience, prohibited claims and disclosures.
- Research: signals and candidate topics; never publishes.
- Planner: converts signals into structured drafts.
- AI provider: generation behind an interface.
- Moderation: deterministic checks plus optional AI review.
- Approval: explicit human decision, separate from moderation.
- Platform adapters: Meta first; future platforms implement the same contract.
- Scheduler/publisher: sends only approved, moderation-passed content.
- Analytics: metrics feed recommendations, not automatic policy changes.

## State machine
IDEA -> DRAFT -> MODERATION_FAILED | READY_FOR_APPROVAL -> APPROVED -> SCHEDULED -> PUBLISHED -> ANALYZED

No path should transition directly from IDEA/DRAFT to PUBLISHED.

## Security
Secrets live in environment variables locally and GitHub Actions Secrets in CI. Never store tokens, refresh tokens, app secrets, or .env files in Git.

## Meta scope
Phase 1 targets Instagram and Facebook Page publishing through Meta Graph API. Exact permissions and endpoints depend on the Meta app/account configuration and must be validated before production.

## Operations
GitHub Actions handles scheduled planning, QA and publishing. Production publishing remains dry-run until credentials and permissions are validated.
