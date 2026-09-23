import argparse
import logging
from pathlib import Path

from rag_pipeline import build_rag_pipeline
from agent_router import run_agent
from observability import log_rag_interaction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    """
    Run the Enterprise RAG Intelligence pipeline from the command line.
    """

    parser = argparse.ArgumentParser(
        description="Enterprise RAG Intelligence using Amazon Bedrock and FAISS"
    )

    parser.add_argument(
        "--data",
        type=str,
        required=True,
        help="Path to the folder containing JSON documents"
    )

    parser.add_argument(
        "--question",
        type=str,
        help="Question to ask the RAG system"
    )

    args = parser.parse_args()

    data_path = Path(args.data)

    if not data_path.exists():
        raise FileNotFoundError(
            f"Data folder does not exist: {data_path}"
        )

    logger.info("Building RAG pipeline...")

    retriever, llm = build_rag_pipeline(
        str(data_path)
    )

    logger.info("RAG pipeline initialized successfully.")

    if args.question:
        result = run_agent(
            retriever,
            llm,
            args.question
        )
        answer = result.get("answer", str(result.get("results", "")))
        print(f"Agent route: {result['route']}")
        print(f"Reason: {result['reason']}")

        sources = [line.split("] ", 1)[-1].split(" - Chunk")[0] for line in answer.splitlines() if line.startswith("[")]
        log_rag_interaction(args.question, answer, sources)
     
        print("\n================ RAG RESPONSE ================\n")
        print(answer)
        print("\n==============================================\n")
    else:
        print("\nEnterprise RAG Intelligence")
        print("Type 'exit' to stop.\n")

        while True:
            question = input("Ask a question: ").strip()

            if question.lower() in {"exit", "quit"}:
                print("Exiting RAG application.")
                break

            if not question:
                continue

            try:
                result = run_agent(retriever, llm, question)

                print(f"\nAgent route: {result['route']}")

                print(f"Reason: {result['reason']}")


                if "answer" in result:

                    print("\nAnswer:\n")

                    print(result["answer"])

                else:

                    print("\nRetrieved sources:\n")

                    for item in result["results"]:

                        print(item)

                print()

            except Exception as error:
                logger.exception(
                    "Failed to generate a response: %s",
                    error
                )


if __name__ == "__main__":
    main()
