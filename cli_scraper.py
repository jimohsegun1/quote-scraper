import argparse
import subprocess

def run_scraper(pages=None, output="quotes.json"):
    cmd = ["scrapy", "crawl", "quotes", "-o", output]
    if pages:
        cmd.append(f"-a pages={pages}")
    subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run quotes scraper with options")
    parser.add_argument("--pages", type=int, help="Number of pages to scrape")
    parser.add_argument("--output", type=str, default="quotes.json", help="Output file")

    args = parser.parse_args()
    run_scraper(pages=args.pages, output=args.output)