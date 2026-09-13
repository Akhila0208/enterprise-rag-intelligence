from langchain_community.vectorstores import FAISS


def create_vector_store(chunks, embedding_model):
    """
    Create a FAISS vector store from document chunks.

    Args:
        chunks: List of chunk dictionaries.
        embedding_model: Configured embedding model.

    Returns:
        FAISS vector store containing the document chunks.
    """

    texts = [chunk["content"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        }
        for chunk in chunks
    ]

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
        metadatas=metadatas
    )

    return vector_store


def save_vector_store(vector_store, path="faiss_index"):
    """
    Save the FAISS index locally.
    """

    vector_store.save_local(path)


def load_vector_store(path, embedding_model):
    """
    Load an existing FAISS vector store.
    """

    return FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )
