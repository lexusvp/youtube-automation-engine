import os,requests
GRAPH_VERSION=os.getenv("META_GRAPH_VERSION","v23.0")
def page_insights(metric="page_impressions"):
    token=os.getenv("META_ACCESS_TOKEN"); page=os.getenv("META_PAGE_ID")
    if not token or not page: raise RuntimeError("META_ACCESS_TOKEN and META_PAGE_ID are required")
    r=requests.get(f"https://graph.facebook.com/{GRAPH_VERSION}/{page}/insights",params={"metric":metric,"access_token":token},timeout=30)
    r.raise_for_status(); return r.json()
