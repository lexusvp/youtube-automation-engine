import pytest
from src.models import ContentDraft
from src.platforms.meta.client import MetaAdapter
def test_publish_requires_approval():
    with pytest.raises(PermissionError): MetaAdapter(dry_run=True).publish(ContentDraft("1","meta","hello"))
def test_dry_run():
    d=ContentDraft("1","meta","hello",approved=True,moderation_status="passed")
    assert MetaAdapter(page_id="123",dry_run=True).publish(d)=="None"
