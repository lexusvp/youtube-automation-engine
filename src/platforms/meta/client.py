import os,requests
from src.models import ContentDraft
from src.platforms.base import PlatformAdapter
GRAPH_VERSION=os.getenv("META_GRAPH_VERSION","v23.0")
class MetaAdapter(PlatformAdapter):
    def __init__(self,access_token=None,page_id=None,ig_user_id=None,dry_run=True):
        self.access_token=access_token or os.getenv("META_ACCESS_TOKEN")
        self.page_id=page_id or os.getenv("META_PAGE_ID")
        self.ig_user_id=ig_user_id or os.getenv("META_IG_USER_ID")
        self.dry_run=dry_run
    def _post(self,path,data):
        if self.dry_run: return {"dry_run":True,"path":path}
        if not self.access_token: raise RuntimeError("META_ACCESS_TOKEN is required")
        r=requests.post(f"https://graph.facebook.com/{GRAPH_VERSION}/{path}",data={**data,"access_token":self.access_token},timeout=30)
        r.raise_for_status(); return r.json()
    def publish_facebook_page(self,draft):
        if not self.page_id: raise RuntimeError("META_PAGE_ID is required")
        return str(self._post(f"{self.page_id}/feed",{"message":draft.text}).get("id"))
    def publish(self,draft):
        if not draft.approved or draft.moderation_status!="passed": raise PermissionError("Draft must pass moderation and receive human approval")
        return self.publish_facebook_page(draft)
