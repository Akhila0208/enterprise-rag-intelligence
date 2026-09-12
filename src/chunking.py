from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):
    """
    Split loaded documents into smaller chunks for the RAG pipeline.

    Args:
        documents: List of documents returned by the document loader.
        chunk_size: Maximum size of each text chunk.
        chunk_overlap: Overlap between consecutive chunks.

    Returns:
        List of chunk dictionaries containing content, source, and chunk ID.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []

    for document in documents:
        split_texts = text_splitter.split_text(document["content"])

        for index, text in enumerate(split_texts):
            chunks.append({
                "content": text,
                "source": document["source"],
                "chunk_id": index
            })

    return chunks    
