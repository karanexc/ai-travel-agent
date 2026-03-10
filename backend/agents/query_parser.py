from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
Extract travel planning details from the user query.

Return ONLY a JSON with:

origin
destination
travelers
days

Example:

User: Plan a 5 day trip from Paris to Tokyo for 2 people

Output:
{{
"origin": "Paris",
"destination": "Tokyo",
"travelers": 2,
"days": 5
}}

User query:
{query}
"""
)

def parse_travel_query(query):

    chain = prompt | llm

    result = chain.invoke({"query": query})

    return result.content