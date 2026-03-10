from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.travel_service import plan_trip


app = FastAPI(title="AI Travel Planner")


class TripRequest(BaseModel):
    origin: str
    destination: str
    travelers: int
    days: int


@app.get("/")
def root():
    return {"message": "AI Travel Planner API running"}


@app.post("/plan-trip")
def plan_trip_api(request: TripRequest):

    result = plan_trip(
        origin=request.origin,
        destination=request.destination,
        travelers=request.travelers,
        days=request.days
    )

    return result