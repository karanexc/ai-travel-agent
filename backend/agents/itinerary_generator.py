from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from backend.config.settings import MODEL_NAME


llm = ChatOpenAI(model=MODEL_NAME)


def generate_itinerary(
    origin,
    destination,
    travelers,
    days,
    budget
):

    prompt = PromptTemplate(
        input_variables=[
            "origin",
            "destination",
            "travelers",
            "days",
            "budget"
        ],
        template="""
You are an AI travel planner.

Create a detailed travel itinerary.

Trip Details:

Origin: {origin}
Destination: {destination}
Travelers: {travelers}
Days: {days}
Estimated Budget: {budget}

Create a day-by-day itinerary including:

- Major attractions
- Food spots
- Activities
- Transport suggestions

Output format:

Trip Summary
Day 1
Day 2
Day 3
Day 4
...
"""
    )

    chain = prompt | llm

    response = chain.invoke({
        "origin": origin,
        "destination": destination,
        "travelers": travelers,
        "days": days,
        "budget": budget
    })

    return response.content