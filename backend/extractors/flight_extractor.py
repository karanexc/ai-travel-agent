from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are a travel data extraction assistant.

From the following scraped travel website text extract flight information.

Return ONLY plain text. Do NOT use markdown symbols like ** or bullet points.

Extract:

1. Average flight price
2. Airlines operating the route
3. Flight duration
4. Important notes for travelers

Rules:
- Always estimate a reasonable price if none is found
- Never write "price not available"
- Never write "not specified"
- Always give a realistic estimate
- Output must follow the structure exactly

Text:
{text}

Output format:

Flight Information

Average Price: $<estimated price range>
Airlines: <comma separated airlines>
Duration: <estimated flight duration>

Notes:
<short useful travel advice>
"""
)

def extract_flight_info(text):

    chain = prompt | llm

    result = chain.invoke({"text": text})

    clean_output = result.content.replace("**", "")

    return clean_output