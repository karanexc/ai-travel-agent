import re


import re

def extract_price_range(text):

    prices = re.findall(r"(?:[\$€£]|INR\s?)([0-9,]+)", text)

    prices = [int(p.replace(",", "")) for p in prices]

    if not prices:
        return None

    return sum(prices) // len(prices)


def calculate_trip_budget(
    flight_text,
    hotel_text,
    travelers,
    nights,
    hotel_type="mid-range"
):

    flight_price = extract_price_range(flight_text)
    hotel_price = extract_price_range(hotel_text)

    # fallback defaults if extraction fails
    if flight_price is None:
        print("Flight price not detected, using default")
        flight_price = 500

    if hotel_price is None:
        print("Hotel price not detected, using default")
        hotel_price = 150

    flight_total = flight_price * travelers
    hotel_total = hotel_price * nights

    transport_estimate = 100 * travelers
    activities_estimate = 80 * travelers

    total_cost = (
        flight_total
        + hotel_total
        + transport_estimate
        + activities_estimate
    )

    return {
        "flight_total": flight_total,
        "hotel_total": hotel_total,
        "transport_estimate": transport_estimate,
        "activities_estimate": activities_estimate,
        "total_trip_cost": total_cost
    }