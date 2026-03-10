from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from backend.config.settings import MODEL_NAME


llm = ChatOpenAI(model=MODEL_NAME)


def extract_hotel_info(text: str):
    """
    Extracts hotel pricing information from scraped text using an LLM.
    """

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are a travel data extractor.

From the following text extract hotel pricing information.

Return:

Budget hotel average price per night
Mid-range hotel average price per night
Luxury hotel average price per night
Any useful notes for travelers

Text:
{text}

Output format:

Hotel Information
Budget:
Mid-range:
Luxury:
Notes:
"""
    )

    chain = prompt | llm

    response = chain.invoke({"text": text})

    return response.content