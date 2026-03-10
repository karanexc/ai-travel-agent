from serpapi import GoogleSearch
from backend.config.settings import SERPAPI_API_KEY


def google_search(query: str, num_results: int = 5):
    """
    Performs a Google search using SerpAPI
    and returns the top search results.
    """

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    organic_results = results.get("organic_results", [])

    search_results = []

    for result in organic_results:

        title = result.get("title")
        link = result.get("link")
        snippet = result.get("snippet")

        search_results.append({
            "title": title,
            "link": link,
            "snippet": snippet
        })

    return search_results