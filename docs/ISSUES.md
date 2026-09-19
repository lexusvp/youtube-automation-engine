# Production-readiness second pass

## P0 — before autonomous publishing
- Validate OAuth scopes and account permissions in a staging/test account.
- Add persistent approval and audit storage.
- Keep live publishing behind a protected GitHub Environment.

## P1 — reliability
- Upload file validation and timezone-aware scheduling guards.
- Retry handling for transient YouTube API failures.
- CI on pushes and pull requests.
- Config validation and no-network CLI smoke tests.
- Logging around external API calls.

## P2 — expansion
- Complete Instagram media-container publishing.
- Normalize analytics and feed recommendation inputs.
- Add multiple AI-provider implementations.

## Completed in this pass
Configuration validation, YouTube input/schedule guards, transient-error retries, dry-run CLI, focused tests and CI.
