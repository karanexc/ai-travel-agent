from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from backend.config.settings import MODEL_NAME

llm = ChatOpenAI(model=MODEL_NAME)

def extract_hotel_info(text: str):

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
You are a travel data extraction assistant.

From the following text extract hotel pricing information.

Return ONLY plain text.
Do NOT use markdown symbols like ** or bullet points.

Extract:

1. Budget hotel price per night
2. Mid-range hotel price per night
3. Luxury hotel price per night
4. Helpful notes for travelers

Rules:

- Always include $ before prices
- Always return price ranges
- If exact values are missing estimate typical hotel prices
- Do NOT output markdown formatting

Text:
{text}

Output format:

Hotel Information

Budget: $<price range> per night
Mid-range: $<price range> per night
Luxury: $<price range> per night

Notes:
<short travel tips>
"""
    )

    chain = prompt | llm

    response = chain.invoke({"text": text})

    clean_output = response.content.replace("**", "")

    return clean_output