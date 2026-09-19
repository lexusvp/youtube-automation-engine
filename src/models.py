from dataclasses import dataclass, field
from typing import Literal
Status = Literal["idea","draft","moderation_failed","ready_for_approval","approved","scheduled","published","analyzed"]
@dataclass
class ContentDraft:
    id:str
    platform:str
    text:str
    status:Status="draft"
    approved:bool=False
    moderation_status:str="pending"
    moderation_reasons:list[str]=field(default_factory=list)
    publish_at:str|None=None
    media_url:str|None=None
