from langchain_aws import BedrockEmbeddings
from config import AWS_REGION, EMBEDDING_MODEL_ID

def create_embedding_model(region_name=AWS_REGION):
    """
    Create an Amazon Bedrock embedding model for the RAG pipeline.

    Args:
        region_name: AWS region where Amazon Bedrock is available.

    Returns:
        Configured BedrockEmbeddings instance.
    """

    embeddings = BedrockEmbeddings(
        region_name=region_name,
        model_id=EMBEDDING_MODEL_ID
    )

    return embeddings


def embed_chunks(chunks, embedding_model):
    """
    Generate vector embeddings for document chunks.
    """

    texts = [chunk["content"] for chunk in chunks]
    vectors = embedding_model.embed_documents(texts)

    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector

    return chunks
