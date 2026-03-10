import requests
from bs4 import BeautifulSoup


def scrape_webpage(url: str):
    """
    Scrapes readable text from a webpage.
    Handles basic HTML pages.
    """

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers, timeout=4)

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "noscript"]):
            tag.extract()

        text = soup.get_text(separator=" ")

        cleaned = " ".join(text.split())

        return cleaned[:4000]

    except Exception as e:
        print(f"Scraping failed for {url}: {e}")
        return None