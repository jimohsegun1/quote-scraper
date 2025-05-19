# 📝 Quote Scraper

A simple Python web scraper that extracts quotes, authors, and tags from [quotes.toscrape.com](https://quotes.toscrape.com). This project shows two different scraping approaches:

- ✅ `scraper.py` — Requests + BeautifulSoup
- ✅ `selenium_scraper.py` — Headless browser with Selenium + WebDriver Manager

---

## 🚀 Features

- Extracts text, author name, and tags
- Works with static and dynamic pages
- Outputs structured data in JSON and CSV
- Auto-handles ChromeDriver installation (Selenium version)

---

# Optional: Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install all dependencies
pip install -r requirements.txt

# Run BeautifulSoup version
python scraper.py

# Run Selenium version
python selenium_scraper.py

## 📁 Folder Structure

```text
quote-scraper/
├── scraper.py # BeautifulSoup scraper
├── selenium_scraper.py # Selenium (headless) scraper
├── quotes.json # Output JSON (auto-generated)
├── quotes.csv # Output CSV (auto-generated)
├── requirements.txt # All dependencies
└── README.md # Instructions and documentation
```
---



