from backend.services.budget_calculator import calculate_trip_budget


flight_info = """
Flight Information
Price: $236 - $560
Airlines: Air India
Duration: 9 hours
"""

hotel_info = """
Hotel Information
Budget: $23 - $59
Mid-range: $99 - $204
Luxury: $395 - $403
"""

budget = calculate_trip_budget(
    flight_text=flight_info,
    hotel_text=hotel_info,
    travelers=3,
    nights=5
)

print("\nTrip Budget Breakdown:\n")

for k, v in budget.items():
    print(k, ":", v)