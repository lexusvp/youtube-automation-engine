from datetime import datetime,timezone
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from .config import settings
SCOPES=["https://www.googleapis.com/auth/youtube.upload","https://www.googleapis.com/auth/youtube.readonly","https://www.googleapis.com/auth/yt-analytics.readonly"]
class YouTubeClient:
    def __init__(self):
        if not settings.has_youtube_credentials: raise RuntimeError("Missing YouTube OAuth credentials")
        c=Credentials(token=None,refresh_token=settings.youtube_refresh_token,token_uri="https://oauth2.googleapis.com/token",client_id=settings.youtube_client_id,client_secret=settings.youtube_client_secret,scopes=SCOPES)
        self.youtube=build("youtube","v3",credentials=c); self.analytics=build("youtubeAnalytics","v2",credentials=c)
    def upload(self,video_path,title,description,tags,thumbnail_path=None,publish_at=None):
        status={"privacyStatus":"private"}
        if publish_at:
            dt=datetime.fromisoformat(publish_at.replace("Z","+00:00"))
            if dt<=datetime.now(timezone.utc): raise ValueError("publish_at must be in the future")
            status["publishAt"]=dt.astimezone(timezone.utc).isoformat().replace("+00:00","Z")
        body={"snippet":{"title":title,"description":description,"tags":tags,"categoryId":str(settings.video_category)},"status":status}
        r=self.youtube.videos().insert(part="snippet,status",body=body,media_body=MediaFileUpload(video_path,chunksize=-1,resumable=True)).execute()
        if thumbnail_path: self.youtube.thumbnails().set(videoId=r["id"],media_body=MediaFileUpload(thumbnail_path)).execute()
        return r["id"]
