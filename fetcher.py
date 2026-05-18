import cloudscraper
from bs4 import BeautifulSoup


class PageFetcher:

    def __init__(self, url):
        self.url = url

    def fetch(self):

        scraper = cloudscraper.create_scraper(
            browser={
                "browser": "chrome",
                "platform": "linux",
                "mobile": False
            }
        )

        response = scraper.get(
            self.url,
            timeout=30
        )

        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(
            html,
            "lxml"
        )

        return html, soup
