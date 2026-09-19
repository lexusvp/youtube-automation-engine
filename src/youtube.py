import logging,time
from datetime import datetime,timezone
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from .config import settings
log=logging.getLogger(__name__)
SCOPES=["https://www.googleapis.com/auth/youtube.upload","https://www.googleapis.com/auth/youtube.readonly","https://www.googleapis.com/auth/yt-analytics.readonly"]
class YouTubeClient:
    def __init__(self):
        if not settings.has_youtube_credentials: raise RuntimeError("Missing YouTube OAuth credentials")
        c=Credentials(token=None,refresh_token=settings.youtube_refresh_token,token_uri="https://oauth2.googleapis.com/token",client_id=settings.youtube_client_id,client_secret=settings.youtube_client_secret,scopes=SCOPES)
        self.youtube=build("youtube","v3",credentials=c); self.analytics=build("youtubeAnalytics","v2",credentials=c)
    @staticmethod
    def _validate_file(path,label):
        if not path: raise ValueError(f"{label} is required")
        p=Path(path)
        if not p.is_file(): raise FileNotFoundError(f"{label} does not exist: {p}")
        if p.stat().st_size==0: raise ValueError(f"{label} is empty: {p}")
        return p
    def upload(self,video_path,title,description,tags,thumbnail_path=None,publish_at=None,max_attempts=3):
        video=self._validate_file(video_path,"video_path")
        if not title or not title.strip(): raise ValueError("title is required")
        if not isinstance(tags,list): raise TypeError("tags must be a list")
        status={"privacyStatus":settings.upload_privacy}
        if publish_at:
            if not settings.scheduled_publication: raise ValueError("Scheduled publication is disabled by configuration")
            try: dt=datetime.fromisoformat(publish_at.replace("Z","+00:00"))
            except ValueError as e: raise ValueError("publish_at must be ISO-8601") from e
            if dt.tzinfo is None: raise ValueError("publish_at must include a timezone")
            if dt<=datetime.now(timezone.utc): raise ValueError("publish_at must be in the future")
            status={"privacyStatus":"private","publishAt":dt.astimezone(timezone.utc).isoformat().replace("+00:00","Z")}
        thumb=None if thumbnail_path is None else self._validate_file(thumbnail_path,"thumbnail_path")
        body={"snippet":{"title":title.strip(),"description":description or "","tags":tags,"categoryId":str(settings.video_category)},"status":status}
        for attempt in range(1,max_attempts+1):
            try:
                r=self.youtube.videos().insert(part="snippet,status",body=body,media_body=MediaFileUpload(str(video),chunksize=-1,resumable=True)).execute()
                vid=r["id"]
                if thumb: self.youtube.thumbnails().set(videoId=vid,media_body=MediaFileUpload(str(thumb))).execute()
                return vid
            except HttpError:
                log.exception("YouTube upload attempt %s/%s failed",attempt,max_attempts)
                if attempt==max_attempts: raise
                time.sleep(2**(attempt-1))
        raise RuntimeError("YouTube upload failed")
