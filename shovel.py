import requests
from bs4 import BeautifulSoup

# Scrape quotes from the website and print them
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for quote in soup.select("div.quote"):
    text = quote.select_one("span.text").text
    author = quote.select_one("small.author").text
    print(f"{author}: {text}")


# Collect all quotes in a list
import csv

rows = []
for quote in soup.select("div.quote"):
    rows.append({
        "text": quote.select_one("span.text").text,
        "author": quote.select_one("small.author").text,
    })

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author"])
    writer.writeheader()
    writer.writerows(rows)