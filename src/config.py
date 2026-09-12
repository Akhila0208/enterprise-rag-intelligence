import os
from dotenv import load_dotenv


load_dotenv()


AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

EMBEDDING_MODEL_ID = os.getenv(
    "EMBEDDING_MODEL_ID",
    "amazon.titan-embed-text-v2:0"
)

LLM_MODEL_ID = os.getenv(
    "LLM_MODEL_ID",
    "amazon.nova-pro-v1:0"
)

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))
RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", "4"))
