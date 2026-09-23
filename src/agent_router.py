"""Agentic routing layer for the Enterprise RAG Intelligence system."""

from dataclasses import dataclass
from typing import Literal

from rag_pipeline import ask_question
from retriever import retrieve_documents


AgentAction = Literal["rag_answer", "retrieve_sources"]


@dataclass
class AgentDecision:
    action: AgentAction
    reason: str


def route_query(question: str) -> AgentDecision:
    """
    Decide which tool should handle the user's request.

    Source/evidence-oriented questions use retrieval directly.
    All other enterprise questions use the grounded RAG pipeline.
    """
    query = question.lower()

    source_keywords = (
        "source",
        "sources",
        "evidence",
        "document",
        "documents",
        "reference",
        "references",
        "where did",
    )

    if any(keyword in query for keyword in source_keywords):
        return AgentDecision(
            action="retrieve_sources",
            reason="User requested supporting evidence or source documents.",
        )

    return AgentDecision(
        action="rag_answer",
        reason="Question requires a grounded generated answer.",
    )


def run_agent(retriever, llm, question: str):
    """Route a request to the appropriate enterprise AI tool."""

    decision = route_query(question)

    if decision.action == "retrieve_sources":
        results = retrieve_documents(retriever, question)

        return {
            "route": decision.action,
            "reason": decision.reason,
            "results": results,
        }

    answer = ask_question(
        retriever,
        llm,
        question,
    )

    return {
        "route": decision.action,
        "reason": decision.reason,
        "answer": answer,
    }
