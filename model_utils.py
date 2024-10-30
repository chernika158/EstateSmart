"""Module with functions for working with LLM."""
import ast
import re
from load_llm import load_llm


def check_extracted_date(answer_dict:dict):
    if 'created_at' in answer_dict.keys():
        if answer_dict['created_at'] is None:
            del answer_dict['created_at']
            return answer_dict
        
        cur_date = answer_dict['created_at']

        correct_date_pattern = r"^\d{4}-\d{2}-\d{2}$"
        if len(cur_date) == 10 and re.match(correct_date_pattern, cur_date):
            answer_dict['created_at'] = '2024-' + cur_date[5:]
        else:
            del answer_dict['created_at']
    return answer_dict


def get_filters_from_query(query: str) -> dict:
    chat_model = load_llm()
    system_prompt_filters_extraction = get_filter_prompt(model_name='gpt')

    messages = [
        {
        "role": "system",
        "content": system_prompt_filters_extraction,
        },
        {
            "role": "user",
            "content": query,
        },
    ]
    ai_answer = chat_model.invoke(messages)
    answer_dict = ast.literal_eval(ai_answer.content)
    answer_dict = check_extracted_date(answer_dict)

    return answer_dict


def format_context(documents, return_metadata_only:bool=False) -> str:
    """Format retrieved documents to pass down to the model."""
    formatted_context = str()
    for doc in documents:
        formatted_context += f"""Page Content: {doc.page_content}\nMetadata: {doc.metadata}\n\n"""
    if return_metadata_only:
        formatted_context += f"""Metadata: {doc.metadata}\n\n"""
    return formatted_context


def get_prompt_estate_agent_chatbot() -> str:
    prompt_estate_agent_chatbot = """You are an assistant for real estate agents.
    You are answering the questions related to the calls they made with their clients: details about the client like their name and phone number, date the viewing of the property is scheduled for, what kind of property the client is interested in, what are the upcoming scheduled viewings for a particular agent.

    Never make up the answer. If you don't know the answer say politely that you don't know the answer. If the question appears to be about a customer you don't have data on, say so.
    Keep the answer as concise as possible.

    Use the following pieces of context to answer the question at the end. The context are the transcripts of the calls.

    Pay attention to the dates. If the agent is asking when someone has called, then check the 'created_at' field in the context and use that date.
    If the agent is asking for what date did someone SCHEDULE A VIEWING then use the page_content (the call transcript itself) of the provided context.
    If the agent is asking about the agent that took the call, answer is the agent_ID field, a 4 digit number.
    """
    return prompt_estate_agent_chatbot


def get_filter_prompt(model_name:str = 'gpt') -> str:
    """Get the prompt for extracting a filter from a user query for corresponding model."""
    prompt_gpt = """You are a bot analysing user query for meaningful contents.
        Analyse the user query below and give extracted contents in form of a dictionary.
        The meaningful information can come in different parts of the user query.
        Do extract as much as you can, you must extract everything that was mentioned in the input.
        Follow the guidelines below:
        ###
        Guidelines:
        1) There are exactly 3 categories of meaningful content you can extract: 
        1. customer_name: a full name of ANY person, like Ana Perkins, Lucas Johnson, Mohammad Farsi, Kai Wong Lee, etc.
        2. customer_phone: a UK phone number, in formats like +447856999888 or 07856999888.
        3. created_at: call date, i.e. when sombody called, like October 2nd, September 1, etc.

        2) Only extract the dates that are explicitly stated. If there's no date in the input, DO NOT INCLUDE 'created_at' in the output at all.
        3) Never come up with information you haven't seen in the query. If you recognise no relevant information, return an empty dictionary.
        4) Return the python dictionary only, in the format that I've specified in examples.
        ###
        Check out the examples below:
        ###
        Examples:
        \n\n1. User query: "Who called me on October 4th?"
        Output: {'created_at': '2024-10-04'}
        \n\n2. User query: "What's the phone number of Lucas Johnson and when did he call?"
        Output: {'customer_name': 'Lucas Johnson'}
        \n\n3.User query: "What is the date of the next scheduled viewing for agent Anna?"
        Output: {}
        \n\n4.User query: "When was the viewing with Mia Perkins and John Johnson?"
        Output: {'customer_name': ['Mia Perkins', 'John Johnson']}
        \n\n5.User query: "What is the name of customer with phone number +447856999888 and when did they call?
        Output: {'customer_phone': '+447856999888'}
        \n\n6.User query: "Did Ana Jenkins call me on September 1st and what is her number?"
        Output: {'customer_name': 'Ana Jenkins', 'created_at': '2024-09-01'}
        ###
        ATTENTION: DO NOT RETURN JSON, PYTHON OR ANY OTHER DECORATORS.
        RETURN PYTHON DICTIONARY in format {'key': 'value', 'key2': 'value2',} like in the examples above.
        """

    prompt_databricks = """You are a bot analysing user query for meaningful contents.
        There are exactly 3 categories of meaningful content you can extract: customer_name, customer_phone, created_at (call date).
        Analyse the query below and give extracted contents in form of a dictionary.
        
        Only extract the dates that are explicitly stated. Never come up with information you haven't seen in the query.
        If there's no date, DO NOT INCLUDE 'created_at' in the output.

        Follow the examples below:

        Example input: "Who called me on October 4th?"
        Output: {'created_at': '2024-10-04'}
        Example input: "What's the phone number of Lucas Johnson and when did he call?"
        Output: {'customer_name': 'Lucas Johnson'}
        Example input: "What is the date of the next scheduled viewing for agent Anna?"
        Output: {}
        Example input: "What is the name of customer with phone number +447856999888 and when did they call?
        Output: {'customer_phone': '+447856999888'}
        Example input: "Did Ana Jenkins call me on September 1st and what is her number?"
        Output: {'customer_name': 'Ana Jenkins', 'created_at': '2024-09-01'}

        Return the dictionary only. If you recognise no relevant information, return an empty dictionary.
        Do not come up with meaningful information! Only extract the information from the query.
        """

    prompts_dict = {'gpt': prompt_gpt,
                    'databricks': prompt_databricks}
    return prompts_dict[model_name]


def get_chatbot_template() -> str:
    chatbot_template = """You are an assistant for real estate agents.
    You are answering the questions related to the calls they made with their clients: details about the client like their name and phone number, date the viewing of the property is scheduled for, what kind of property the client is interested in, what are the upcoming scheduled viewings for a particular agent.

    Never make up the answer. If you don't know the answer say politely that you don't know the answer. If the question appears to be about a customer you don't have data on, say so.
    Keep the answer as concise as possible.

    Use the following pieces of context to answer the question at the end. The context are the transcripts of the calls.

    Pay attention to the dates. If the agent is asking when someone has called, then check the 'created_at' field in the context and use that date.
    If the agent is asking for what date did someone SCHEDULE A VIEWING then use the page_content (the call transcript itself) of the provided context.
    If the agent is asking about the agent that took the call, answer is the agent_ID field, a 4 digit number.
    {context}
    {question}
    """
    return chatbot_template


### Stashed functions (not used for the current agent) ###

def get_chatbot_template_dbx() -> str:
    chatbot_template = """You are an assistant for real estate agents. You are answering the questions related to the calls they made with their clients: details about the client like their name and phone number, date the viewing of the property is scheduled for, what kind of property the client is interested in, what are the upcoming schduled viewings for a particular agent. If the question is not related to this topic, kindly decline to answer. If you don't know the answer, just say that you don't know, don't try to make up an answer. If the question appears to be for a customer don't have data on, say so.  Keep the answer as concise as possible.  Provide all answers only in English.
    Use the following pieces of context to answer the question at the end:
    Pay attention to the dates. If agent is asking when someone has called, then check the 'created_at' field in the context and use that date. You can find it at this path data['source_documents'][i]['metadata']['created_at'] where i is the index of source document.
    If agent is asking for what date did someone SCHEDULE A VIEWING then use the page_content of the provided context.
    {context}

    Question: {question}
    Answer:
    """
    return chatbot_template


# def get_filters_from_query_dbrx(query: str) -> dict:
#     chat_model = ChatDatabricks(
#         endpoint="databricks-dbrx-instruct",
#         temperature=0.1,
#         max_tokens=500,
#         # other supported parameters: https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.databricks.ChatDatabricks.html 
#     )

#     messages = [
#         ("system", get_filter_prompt(model_name='databricks')),
#         ("user", query),
#     ]
#     ai_answer = chat_model.invoke(messages)
#     answer_dict = ast.literal_eval(ai_answer.content)
#     answer_dict = check_extracted_date(answer_dict)

#     return answer_dict
    