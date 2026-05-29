import cloudscraper
from bs4 import BeautifulSoup

class DescFetcher:

    def __init__(self,url):
        self.url = url

    def fetchDesc(self):
        # descData = ""
        text = ""
        
        scraper = cloudscraper.create_scraper(
            browser = {
                "browser" : "chrome",
                "platform" : "linux",
                "mobile" : False
            }
        )

        response = scraper.get(
            self.url,
            timeout = 30
        )

        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(
            html,
            "lxml"
        )
        soupDesc = soup.find("div",class_="card-content")

        if soupDesc:
            text = soupDesc.get_text()

       

        return text


        