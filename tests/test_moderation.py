from src.models import ContentDraft
from src.moderation.service import moderate,can_publish
def test_clean_draft_passes():
    d=moderate(ContentDraft("1","meta","A practical AI workflow."))
    assert d.moderation_status=="passed"; assert d.status=="ready_for_approval"; assert not can_publish(d)
def test_banned_claim_fails():
    d=moderate(ContentDraft("2","meta","Guaranteed income in 7 days."))
    assert d.moderation_status=="failed"; assert d.status=="moderation_failed"
