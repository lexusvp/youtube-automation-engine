import re
from src.models import ContentDraft
BANNED_PATTERNS=[r"\bguaranteed\s+income\b",r"\bget\s+rich\s+quick\b"]
def moderate(draft:ContentDraft)->ContentDraft:
    reasons=[]
    for pattern in BANNED_PATTERNS:
        if re.search(pattern,draft.text,re.I): reasons.append(f"Matched policy pattern: {pattern}")
    draft.moderation_reasons=reasons
    draft.moderation_status="failed" if reasons else "passed"
    draft.status="moderation_failed" if reasons else "ready_for_approval"
    return draft
def can_publish(draft): return draft.approved and draft.moderation_status=="passed"
