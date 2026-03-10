from backend.scraping.google_search import google_search
from backend.scraping.web_scraper import scrape_webpage
from backend.extractors.hotel_extractor import extract_hotel_info


query = "average hotel price per night in London for tourists"

results = google_search(query)

combined_text = ""

for r in results:
    url = r["link"]

    print("\nScraping:", url)

    page_text = scrape_webpage(url)

    if page_text:
        combined_text += page_text + "\n"


print("\nSending combined text to LLM...\n")

hotel_info = extract_hotel_info(combined_text)

print("\nExtracted Hotel Info:\n")
print(hotel_info)