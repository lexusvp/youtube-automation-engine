from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class ResearchIdea:
    topic: str
    angle: str
    audience: str
    opportunity_score: int
    estimated_watch_time: str
    thumbnail_concept: str
    value_prop: str


def generate_ideas(topics: List[str] | None = None, audience: str = "builders and founders") -> List[ResearchIdea]:
    seeded_topics = topics or ["AI automation", "developer workflows", "content systems", "growth experiments"]
    ideas: List[ResearchIdea] = []

    for index, topic in enumerate(seeded_topics, start=1):
        ideas.append(
            ResearchIdea(
                topic=topic,
                angle=f"{topic} for practical execution in a real business environment",
                audience=audience,
                opportunity_score=82 + index * 4,
                estimated_watch_time="7-12 minutes",
                thumbnail_concept=f"{topic} explained visually with bold, high-contrast text",
                value_prop="Shows how to use automation to reduce repetitive work and increase output without sacrificing quality.",
            )
        )

    return ideas
