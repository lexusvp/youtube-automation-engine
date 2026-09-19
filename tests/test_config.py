import pytest
from src.config import Settings
def test_defaults(monkeypatch):
    for k in ["UPLOAD_PRIVACY","VIDEO_CATEGORY","SCHEDULED_PUBLICATION"]: monkeypatch.delenv(k,raising=False)
    s=Settings.from_env(); assert s.upload_privacy=="private" and s.video_category==27 and not s.scheduled_publication
def test_invalid_privacy(monkeypatch):
    monkeypatch.setenv("UPLOAD_PRIVACY","invalid")
    with pytest.raises(ValueError): Settings.from_env()
def test_invalid_category(monkeypatch):
    monkeypatch.setenv("VIDEO_CATEGORY","nope")
    with pytest.raises(ValueError): Settings.from_env()
def test_invalid_bool(monkeypatch):
    monkeypatch.setenv("SCHEDULED_PUBLICATION","maybe")
    with pytest.raises(ValueError): Settings.from_env()
