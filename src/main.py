import argparse
import logging
from pathlib import Path

from rag_pipeline import build_rag_pipeline, ask_question


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
        answer = ask_question(
            retriever,
            llm,
            args.question
        )

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
                answer = ask_question(
                    retriever,
                    llm,
                    question
                )

                print("\nAnswer:\n")
                print(answer)
                print()

            except Exception as error:
                logger.exception(
                    "Failed to generate a response: %s",
                    error
                )


if __name__ == "__main__":
    main()
