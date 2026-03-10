from backend.agents.itinerary_generator import generate_itinerary


itinerary = generate_itinerary(
    origin="Mumbai",
    destination="London",
    travelers=3,
    days=5,
    budget=2329
)

print("\nGenerated Itinerary:\n")
print(itinerary)