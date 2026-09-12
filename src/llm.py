from langchain_aws import ChatBedrock


def create_llm(region_name="us-east-1"):
    """
    Create the Amazon Bedrock LLM used for RAG answer generation.

    Args:
        region_name: AWS region where Amazon Bedrock is available.

    Returns:
        Configured ChatBedrock model.
    """

    llm = ChatBedrock(
        model_id="amazon.nova-pro-v1:0",
        region_name=region_name,
        model_kwargs={
            "temperature": 0.1,
            "max_tokens": 1000
        }
    )

    return llm
