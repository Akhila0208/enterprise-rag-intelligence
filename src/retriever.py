from config import TOP_K
def create_retriever(vector_store, k=TOP_K):
    """
    Create a retriever for semantic search over the vector store.

    Args:
        vector_store: FAISS vector store containing document embeddings.
        k: Number of relevant chunks to retrieve.

    Returns:
        Configured vector store retriever.
    """

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    return retriever


def retrieve_documents(retriever, query):
    """
    Retrieve the most relevant document chunks for a user query.

    Args:
        retriever: Configured vector store retriever.
        query: User question.

    Returns:
        List of relevant documents.
    """

    documents = retriever.invoke(query)

    return documents
