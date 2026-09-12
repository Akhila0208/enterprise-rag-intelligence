import json
from pathlib import Path


def load_json_documents(folder_path):
    """
    Load JSON documents from a folder for the RAG pipeline.
    """

    documents = []

    folder = Path(folder_path)

    for file_path in folder.glob("*.json"):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            documents.append({
                "content": json.dumps(data),
                "source": file_path.name
            })

    return documents
