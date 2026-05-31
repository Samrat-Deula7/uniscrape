import cloudscraper
from bs4 import BeautifulSoup

class CostFetcher:

    def __init__(self,url):
        self.url = url

    def fetchCost(self):
        cost = []
        AccommodationSoup = ""
        FoodSoup = ""
        TransportSoup = ""
        UtilitiesSoup = ""

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
         
        AccommodationSoup = soup.find("div",class_="card Accommodation")
        FoodSoup = soup.find("div",class_="card Food")
        TransportSoup = soup.find("div",class_="card Transport")
        UtilitiesSoup = soup.find("div",class_="card Utilities")
   
      


        cost = [
            {
                "Accommodation":AccommodationSoup.find("div").get_text(" ", strip=True) if AccommodationSoup else "",
                "Food":FoodSoup.find("div").get_text(" ", strip=True) if FoodSoup else "",
                "Transport":TransportSoup.find("div").get_text(" ", strip=True) if TransportSoup else "",
                "Utilities":UtilitiesSoup.find("div").get_text(" ", strip=True) if UtilitiesSoup else "",
                }
                ]

        return cost
