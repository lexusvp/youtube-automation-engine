# Operations

## Secrets
META_ACCESS_TOKEN, META_PAGE_ID, META_IG_USER_ID, OPENAI_API_KEY.

## Approval
A post requires both moderation_status=passed and approved=true.

## Dry run
Scheduled workflows default to dry-run. Enable live publishing only after Meta permissions and test publishing are validated.

## Incident response
1. Disable publish workflow.
2. Revoke the affected Meta token.
3. Rotate the GitHub secret.
4. Review queue and workflow logs.
5. Re-enable after a successful dry-run.
