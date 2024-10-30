from langchain_openai import AzureChatOpenAI
from langchain_community.embeddings import DatabricksEmbeddings
from get_params import set_secrets

def load_llm() -> AzureChatOpenAI:
    """Load the Azure OpenAI language model with the given parameters.

    Notes:
        The following environment variables must be set:
        - AZURE_OPENAI_API_KEY: The API key for Azure OpenAI.
        - AZURE_OPENAI_ENDPOINT: The endpoint for Azure OpenAI.
        - OPENAI_API_VERSION: The API version for Azure OpenAI.
        - AZURE_DEPLOYMENT_NAME: The deployment name for Azure OpenAI.
    """
    secrets = set_secrets()
    return AzureChatOpenAI(
        openai_api_type="azure",
        api_key=secrets.get("AZURE_OPENAI_KEY"),
        azure_endpoint=secrets.get("AZURE_OPENAI_ENDPOINT"),
        api_version=secrets.get("AZURE_OPENAI_PREVIEW_API_VERSION"),
        azure_deployment=secrets.get("AZURE_DEPLOYMENT_NAME"),
        model_name=secrets.get("AZURE_OPENAI_MODEL"),
        max_tokens=1000,
    )


def load_embedding_model() -> DatabricksEmbeddings:
    """
    Load the Azure OpenAI embedding model with the given parameters.

    This function creates and returns an instance of the AzureOpenAIEmbeddings model using
    the specified keyword arguments. The function uses LRU caching to store the model
    instance and reuse it for subsequent calls with the same parameters.

    Args:
        **model_kwards: Arbitrary keyword arguments to configure the AzureOpenAIEmbeddings model.

    Returns:
        AzureOpenAIEmbeddings: An instance of the AzureOpenAIEmbeddings model configured with the provided parameters.

    Notes:
        The following environment variables must be set:
        - AZURE_OPENAI_API_KEY: The API key for Azure OpenAI.
        - AZURE_OPENAI_ENDPOINT: The endpoint for Azure OpenAI.
        - OPENAI_API_VERSION: The API version for Azure OpenAI.
        - AZURE_EMBEDDINGS_DEPLOYMENT_NAME: The deployment name for Azure OpenAI embedding model.
    """

    # return AzureOpenAIEmbeddings(
    #     openai_api_type="azure",
    #     api_key=AZURE_OPENAI_API_KEY,
    #     azure_endpoint=AZURE_OPENAI_ENDPOINT,
    #     api_version=OPENAI_API_VERSION,
    #     azure_deployment=AZURE_EMBEDDINGS_DEPLOYMENT_NAME,
    #     **model_kwards,
    # )
    return DatabricksEmbeddings(endpoint=set_secrets().get("EMBEDDINGS_ENDPOINT"))