"""Cross-round score aggregation and decision (PRD Phases 20, 45, 70)."""
from utils.logger import get_logger

logger = get_logger(__name__)

DEFAULT_WEIGHTS = {"ats": 0.25, "hr": 0.25, "technical": 0.30, "machine_test": 0.20}


def aggregate(scores: dict[str, float], weights: dict[str, float] | None = None) -> float:
    weights = weights or DEFAULT_WEIGHTS
    used = {k: w for k, w in weights.items() if k in scores}
    if not used:
        raise ValueError("No matching score components supplied")
    final = round(sum(scores[k] * w for k, w in used.items()) / sum(used.values()), 2)
    logger.info("Aggregated score: %s from %s", final, list(used))
    return final


def decide(final_score: float, select_at: float = 70.0, hold_at: float = 50.0) -> str:
    if final_score >= select_at:
        return "selected"
    if final_score >= hold_at:
        return "hold"
    return "rejected"