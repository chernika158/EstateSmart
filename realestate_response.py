import os

from databricks.vector_search.client import VectorSearchClient
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_community.chat_models import ChatDatabricks
from langchain_community.embeddings import DatabricksEmbeddings
from langchain_community.vectorstores import DatabricksVectorSearch

from typing import Union, Tuple

from get_params import set_secrets
from load_llm import load_llm
from model_utils import get_filters_from_query, format_context, get_prompt_estate_agent_chatbot, get_chatbot_template

secrets = set_secrets()

host = secrets.get("DATABRICKS_HOST")
index_name = secrets.get("INDEX_NAME")
EMBEDDINGS_ENDPOINT = secrets.get("EMBEDDINGS_ENDPOINT")
VECTOR_SEARCH_ENDPOINT_NAME = secrets.get("VECTOR_SEARCH_ENDPOINT_NAME")
PERSONAL_ACCESS_TOKEN = secrets.get("PERSONAL_ACCESS_TOKEN")

embedding_model = DatabricksEmbeddings(endpoint=EMBEDDINGS_ENDPOINT)
text_column = "conversation_text"
include_metadata = ['property_number',
                    'conversation_ID',
                    'customer_ID',
                    'agent_ID',
                    'customer_name',
                    'customer_phone',
                    'created_at'
                    ]


def get_retriever_with_prefiter(persist_dir: str = None, filter_dict: dict=None):
    vsc = VectorSearchClient(workspace_url=host, personal_access_token=PERSONAL_ACCESS_TOKEN)
    vs_index = vsc.get_index(
        endpoint_name=VECTOR_SEARCH_ENDPOINT_NAME,
        index_name=index_name
    )

    vectorstore = DatabricksVectorSearch(
        vs_index, 
        text_column=text_column,
        embedding=embedding_model,
        columns=include_metadata,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k":10, "filters":filter_dict})
    return retriever

def get_llm_answer_using_context(user_query: str,
                                 return_source_documents: bool = False) -> Union[str, Tuple[str, list]]:
    """Get Real Estate Chatbot answer to the user_query leveraging the retrieved documents."""
    chat_model = load_llm()
    # extract meaningful information to use as filter in retriever, e.g. customer_name
    filters_extracted = get_filters_from_query(user_query)
    # print(f"Extracted meaningful info:\n{filters_extracted}")

    # get relevant documents and process them to use in the prompt
    retriever = get_retriever_with_prefiter(filter_dict=filters_extracted)
    retrieved_docs = retriever.invoke(user_query)
    formatted_context = format_context(retrieved_docs)

    # put together prompt and context and query the llm
    prompt_estate_agent_chatbot = get_prompt_estate_agent_chatbot()
    chatbot_prompt = f"""{prompt_estate_agent_chatbot} {formatted_context}"""
    messages = [
        {
            "role": "system",
            "content": chatbot_prompt,
        },
        {
            "role": "user",
            "content": f"Question: {user_query}\n\nAnswer:",
        },
    ]
    ai_answer = chat_model.invoke(messages)

    if return_source_documents:
        return ai_answer.content, retrieved_docs
    return ai_answer.content