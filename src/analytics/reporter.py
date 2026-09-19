from __future__ import annotations

from typing import Dict, List


def summarize_channel_metrics(metrics: Dict[str, float] | None = None) -> Dict[str, float]:
    stats = metrics or {
        "views": 1250,
        "watch_hours": 45.5,
        "ctr": 4.8,
        "avg_view_duration": 180,
        "subscribers": 42,
    }

    return {
        "views": stats.get("views", 0),
        "watch_hours": stats.get("watch_hours", 0),
        "ctr": stats.get("ctr", 0),
        "avg_view_duration": stats.get("avg_view_duration", 0),
        "subscribers": stats.get("subscribers", 0),
    }


def recommend_next_topics(metrics: Dict[str, float] | None = None) -> List[str]:
    result = summarize_channel_metrics(metrics)
    recommendations: List[str] = []

    if result["ctr"] > 4:
        recommendations.append("High-CTR workflow breakdowns")
    if result["avg_view_duration"] > 200:
        recommendations.append("Deep-dive technical explainers")
    if result["subscribers"] > 25:
        recommendations.append("Series-based product and automation case studies")

    if not recommendations:
        recommendations.append("Operational workflows for AI-powered creators")

    return recommendations
