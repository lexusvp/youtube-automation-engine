import json
from dataclasses import dataclass,asdict
from pathlib import Path
QUEUE=Path("content/queue.json")
@dataclass
class QueueItem:
    id:str; topic:str; approved:bool=False; video_path:str|None=None; thumbnail_path:str|None=None; publish_at:str|None=None
def load_queue():
    if not QUEUE.exists(): return []
    return [QueueItem(**x) for x in json.loads(QUEUE.read_text()).get("items",[])]
def save_queue(items):
    QUEUE.parent.mkdir(parents=True,exist_ok=True); QUEUE.write_text(json.dumps({"items":[asdict(x) for x in items]},indent=2)+"\n")
def next_approved_item(): return next((x for x in load_queue() if x.approved and x.video_path),None)
