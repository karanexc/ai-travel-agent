from backend.scraping.google_search import google_search
from backend.scraping.web_scraper import scrape_webpage

from backend.extractors.flight_extractor import extract_flight_info
from backend.extractors.hotel_extractor import extract_hotel_info

from backend.services.budget_calculator import calculate_trip_budget

from backend.agents.itinerary_generator import generate_itinerary


def collect_web_data(query):

    results = google_search(query)

    combined_text = ""

    for r in results[:3]:

        url = r["link"]

        print("Scraping:", url)

        page_text = scrape_webpage(url)

        if page_text:
            combined_text += page_text + "\n"

    return combined_text


def generate_trip(origin, destination, travelers, days):

    print("\nSearching flight information...\n")

    flight_query = f"flights from {origin} to {destination} price duration airlines travel time"

    flight_text = collect_web_data(flight_query)

    flight_info = extract_flight_info(flight_text)


    print("\nSearching hotel information...\n")

    hotel_query = f"average hotel price per night in {destination}"

    hotel_text = collect_web_data(hotel_query)

    hotel_info = extract_hotel_info(hotel_text)


    print("\nCalculating trip budget...\n")

    budget = calculate_trip_budget(
        flight_text=flight_info,
        hotel_text=hotel_info,
        travelers=travelers,
        nights=days
    )


    print("\nGenerating itinerary...\n")

    itinerary = generate_itinerary(
        origin=origin,
        destination=destination,
        travelers=travelers,
        days=days,
        budget=budget["total_trip_cost"]
    )


    return {
        "flight_info": flight_info,
        "hotel_info": hotel_info,
        "budget": budget,
        "itinerary": itinerary
    }