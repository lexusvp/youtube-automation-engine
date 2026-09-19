import os
from dataclasses import dataclass
from dotenv import load_dotenv
load_dotenv()
TRUE_VALUES={"1","true","yes","on"}; ALLOWED_PRIVACY={"private","unlisted","public"}
def _optional(name):
    v=os.getenv(name); return v.strip() if v and v.strip() else None
def _int_env(name,default):
    raw=os.getenv(name,str(default)).strip()
    try: v=int(raw)
    except ValueError as e: raise ValueError(f"{name} must be an integer") from e
    if v<1: raise ValueError(f"{name} must be >= 1")
    return v
def _bool_env(name,default=False):
    raw=os.getenv(name,str(default)).strip().lower()
    if raw not in TRUE_VALUES and raw not in {"0","false","no","off"}: raise ValueError(f"{name} must be a boolean")
    return raw in TRUE_VALUES
@dataclass(frozen=True)
class Settings:
    youtube_client_id:str|None=None; youtube_client_secret:str|None=None; youtube_refresh_token:str|None=None; youtube_channel_id:str|None=None; openai_api_key:str|None=None; openai_model:str="gpt-4o-mini"; upload_privacy:str="private"; video_category:int=27; scheduled_publication:bool=False
    @classmethod
    def from_env(cls):
        privacy=os.getenv("UPLOAD_PRIVACY","private").strip().lower()
        if privacy not in ALLOWED_PRIVACY: raise ValueError(f"UPLOAD_PRIVACY must be one of {sorted(ALLOWED_PRIVACY)}")
        return cls(_optional("YOUTUBE_CLIENT_ID"),_optional("YOUTUBE_CLIENT_SECRET"),_optional("YOUTUBE_REFRESH_TOKEN"),_optional("YOUTUBE_CHANNEL_ID"),_optional("OPENAI_API_KEY"),os.getenv("OPENAI_MODEL","gpt-4o-mini").strip(),privacy,_int_env("VIDEO_CATEGORY",27),_bool_env("SCHEDULED_PUBLICATION",False))
    @property
    def has_youtube_credentials(self): return all((self.youtube_client_id,self.youtube_client_secret,self.youtube_refresh_token))
    @property
    def has_openai_key(self): return bool(self.openai_api_key)
settings=Settings.from_env()
