from backend.scraping.web_scraper import scrape_webpage

url = "https://en.wikipedia.org/wiki/London"

content = scrape_webpage(url)

print(content[:1000])