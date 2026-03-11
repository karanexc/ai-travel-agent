from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from backend.config.settings import MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)


def extract_hotel_info(text: str):

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are a travel assistant.

From the following text extract hotel recommendations.

Return:

- 3 budget hotels
- 3 mid-range hotels
- 3 luxury hotels

Output must be structured JSON.

Text:
{text}

Output:

{{
 "budget_hotels": ["hotel1", "hotel2", "hotel3"],
 "midrange_hotels": ["hotel1", "hotel2", "hotel3"],
 "luxury_hotels": ["hotel1", "hotel2", "hotel3"]
}}
"""
    )

    chain = prompt | llm

    response = chain.invoke({"text": text})

    return response.content