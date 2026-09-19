import os
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
@dataclass(frozen=True)
class Settings:
    youtube_client_id:str|None=None; youtube_client_secret:str|None=None; youtube_refresh_token:str|None=None; youtube_channel_id:str|None=None; openai_api_key:str|None=None; openai_model:str="gpt-4o-mini"; upload_privacy:str="private"; video_category:int=27
    @classmethod
    def from_env(cls):
        return cls(os.getenv("YOUTUBE_CLIENT_ID"),os.getenv("YOUTUBE_CLIENT_SECRET"),os.getenv("YOUTUBE_REFRESH_TOKEN"),os.getenv("YOUTUBE_CHANNEL_ID"),os.getenv("OPENAI_API_KEY"),os.getenv("OPENAI_MODEL","gpt-4o-mini"),os.getenv("UPLOAD_PRIVACY","private"),int(os.getenv("VIDEO_CATEGORY","27")))
    @property
    def has_youtube_credentials(self): return all((self.youtube_client_id,self.youtube_client_secret,self.youtube_refresh_token))
    @property
    def has_openai_key(self): return bool(self.openai_api_key)
settings=Settings.from_env()
