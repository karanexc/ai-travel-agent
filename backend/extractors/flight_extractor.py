from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from backend.config.settings import MODEL_NAME


llm = ChatOpenAI(model=MODEL_NAME)


def extract_flight_info(text: str):
    """
    Extracts flight information from scraped webpage text using an LLM.
    """

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are a travel data extractor.

Extract ONLY information that clearly appears in the text.

Do not guess or invent data.

Return:

Flight Information
Price:
Airlines:
Duration:
Notes:

Text:
{text}
"""
    )

    chain = prompt | llm

    response = chain.invoke({"text": text})

    return response.content