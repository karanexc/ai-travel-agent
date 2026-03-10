from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.travel_service import generate_trip
from backend.agents.query_parser import parse_travel_query

import json

app = FastAPI(title="AI Travel Planner")


class TripRequest(BaseModel):
    origin: str
    destination: str
    travelers: int
    days: int


@app.get("/")
def root():
    return {"message": "AI Travel Planner API running"}


# -------------------------------
# NORMAL FORM TRIP
# -------------------------------

@app.post("/plan-trip")
def plan_trip_api(request: TripRequest):

    result = generate_trip(
        origin=request.origin,
        destination=request.destination,
        travelers=request.travelers,
        days=request.days
    )

    return result


# -------------------------------
# AI CHAT TRIP
# -------------------------------

@app.post("/chat-plan")
def chat_plan(data: dict):

    user_query = data["query"]

    parsed = parse_travel_query(user_query)

    params = json.loads(parsed)

    trip = generate_trip(
        params["origin"],
        params["destination"],
        params["travelers"],
        params["days"]
    )

    return trip