import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = "https://quotes.toscrape.com/page/{}/"
all_quotes = []

for page in range(1, 6):  # Scrape first 5 pages
    res = requests.get(base_url.format(page))
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.select(".quote")

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.select(".tags .tag")]

        all_quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

# Save to JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, ensure_ascii=False, indent=2)

# Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    writer.writeheader()
    for quote in all_quotes:
        writer.writerow({
            "text": quote["text"],
            "author": quote["author"],
            "tags": ", ".join(quote["tags"])
        })

print("✅ BeautifulSoup scraping complete. Saved to quotes.json and quotes.csv.")
