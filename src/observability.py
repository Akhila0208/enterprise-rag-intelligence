
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("enterprise-rag")


def log_rag_interaction(question, answer, sources):
    """Record a RAG interaction for monitoring and debugging."""

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "answer": answer,
        "sources": sources,
    }

    logger.info(
        "RAG interaction | question=%s | sources=%s",
        question,
        sources,
    )

    with open(LOG_DIR / "rag_interactions.jsonl", "a") as file:
        file.write(json.dumps(event) + "\n")
