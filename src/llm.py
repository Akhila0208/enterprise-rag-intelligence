from langchain_aws import ChatBedrock
from config import AWS_REGION, LLM_MODEL_ID


def create_llm(region_name=AWS_REGION):
    """
    Create the Amazon Bedrock LLM used for RAG answer generation.

    Args:
        region_name: AWS region where Amazon Bedrock is available.

    Returns:
        Configured ChatBedrock model.
    """

    llm = ChatBedrock(
        model_id=LLM_MODEL_ID,
        region_name=region_name,
        model_kwargs={
            "temperature": 0.1,
            "max_tokens": 1000
        }
    )

    return llm
