from backend.services.travel_service import plan_trip


result = plan_trip(
    origin="Mumbai",
    destination="London",
    travelers=3,
    days=5
)


print("\n\nFINAL RESULT\n")

print("\nFlights:\n")
print(result["flight_info"])

print("\nHotels:\n")
print(result["hotel_info"])

print("\nBudget:\n")
print(result["budget"])

print("\nItinerary:\n")
print(result["itinerary"])