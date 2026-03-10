from backend.scraping.google_search import google_search

query = "flights from Mumbai to London price"

results = google_search(query)

for r in results:
    print("\nTitle:", r["title"])
    print("Link:", r["link"])
    print("Snippet:", r["snippet"])