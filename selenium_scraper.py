from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import json

# Setup headless Chrome with webdriver-manager
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

all_quotes = []
driver.get("https://quotes.toscrape.com")

while True:
    time.sleep(1)  # For simplicity; you can use WebDriverWait for production-grade

    quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

    for quote in quote_elements:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        tags = [tag.text for tag in quote.find_elements(By.CLASS_NAME, "tag")]

        all_quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    # Click next page or break
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, ".pager .next a")
        next_btn.click()
    except:
        break

driver.quit()

# Save as JSON
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_quotes, f, ensure_ascii=False, indent=2)

# Save as CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
    writer.writeheader()
    for quote in all_quotes:
        writer.writerow({
            "text": quote["text"],
            "author": quote["author"],
            "tags": ", ".join(quote["tags"])
        })

print("✅ Selenium scraping complete! Saved to quotes.json and quotes.csv.")
