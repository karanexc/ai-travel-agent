from backend.scraping.google_search import google_search
from backend.scraping.web_scraper import scrape_webpage
from backend.extractors.flight_extractor import extract_flight_info


query = "average flight price Mumbai to London duration airlines"

results = google_search(query)

all_text = ""

for r in results:
    url = r["link"]

    print("\nScraping:", url)

    page_text = scrape_webpage(url)

    if page_text:
        all_text += page_text + "\n"


print("\nSending combined text to LLM...\n")

flight_info = extract_flight_info(all_text)

print("\nExtracted Flight Info:\n")
print(flight_info)