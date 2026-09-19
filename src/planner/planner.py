from src.ai import generate_package
from src.models import ContentDraft
def plan(topic:str,platform:str="meta")->ContentDraft:
    package=generate_package(topic)
    return ContentDraft(id=f"{platform}-{abs(hash(topic))}",platform=platform,text=f"{package.hook}\n\n{package.description}")
