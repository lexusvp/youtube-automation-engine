import json
from dataclasses import dataclass
from openai import OpenAI
from .config import settings
@dataclass
class Package:
    title:str; hook:str; description:str; tags:list[str]; outline:list[str]; thumbnail_brief:str
def fallback(topic): return Package(f"{topic}: A Practical Build",f"Here is a practical system for {topic}.",f"A practical walkthrough of {topic}.",[topic,"AI","automation","YouTube"],["Problem","Architecture","Build","QA","Lessons"],f"Minimal thumbnail concept for {topic}.")
def generate_package(topic):
    if not settings.has_openai_key: return fallback(topic)
    r=OpenAI(api_key=settings.openai_api_key).chat.completions.create(model=settings.openai_model,temperature=.7,response_format={"type":"json_object"},messages=[{"role":"system","content":"You are a technical YouTube producer."},{"role":"user","content":f"Create a YouTube package for {topic}. Return JSON keys title, hook, description, tags, outline, thumbnail_brief. Avoid unsupported claims and clickbait."}])
    d=json.loads(r.choices[0].message.content); return Package(d["title"],d["hook"],d["description"],list(d["tags"]),list(d["outline"]),d["thumbnail_brief"])
def generate_ideas(count=10):
    return ["AI content automation with GitHub Actions","AI agents for business workflows","Kubernetes for AI workloads","LLM enterprise integration patterns","Reliable AI microservices","AI observability","Production AI architecture","AI-first content pipelines","Cloud architecture for AI SaaS","Automating developer workflows with AI"][:count]
