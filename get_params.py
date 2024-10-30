import os
from databricks.sdk.runtime import dbutils

def set_secrets() -> dict:
    """
    Load and set secrets from a '.env' file as environment variables.

    This function checks for the presence of a '.env' file in the current directory.
    If the file exists, it loads the environment variables from the file and sets
    them in the environment. If the file does not exist, it prints a warning message.

    Returns:
        None
    """

    secrets_dict = {
        "AZURE_OPENAI_KEY": os.getenv("AZURE_OPENAI_KEY"),
        "AZURE_OPENAI_MODEL": os.getenv("AZURE_OPENAI_MODEL"),
        "AZURE_OPENAI_ENDPOINT": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "AZURE_KEY_VAULT_NAME": os.getenv("AZURE_KEY_VAULT_NAME"),
        "AZURE_KEY_VAULT_URI": os.getenv("AZURE_KEY_VAULT_URI"),
        "AZURE_EMBEDDINGS_OPENAI_MODEL": os.getenv("AZURE_EMBEDDINGS_OPENAI_MODEL"),
        "AZURE_OPENAI_PREVIEW_API_VERSION": os.getenv("AZURE_OPENAI_PREVIEW_API_VERSION"),
        "DATABRICKS_HOST": os.getenv("DATABRICKS_HOST"),
        "EMBEDDINGS_ENDPOINT": os.getenv("EMBEDDINGS_ENDPOINT"),
        "INDEX_NAME": os.getenv("INDEX_NAME"),
        "PERSONAL_ACCESS_TOKEN": os.getenv("PERSONAL_ACCESS_TOKEN"),
        "PYSPARK_PYTHON": os.getenv("PYSPARK_PYTHON"),
        "VECTOR_SEARCH_ENDPOINT_NAME": os.getenv("VECTOR_SEARCH_ENDPOINT_NAME")
    }
    
    return secrets_dict
