import pytest
from src.youtube import YouTubeClient
def test_missing_file():
    with pytest.raises(FileNotFoundError): YouTubeClient._validate_file("/missing/video.mp4","video_path")
def test_empty_file(tmp_path):
    p=tmp_path/"video.mp4"; p.write_bytes(b"")
    with pytest.raises(ValueError): YouTubeClient._validate_file(str(p),"video_path")
