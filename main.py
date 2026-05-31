import json

from fetchUniLinks import LinkFetcher
from fetchDesc import DescFetcher
from fetchCourses import CoursesFetcher
from fetchLogo import LogoFetcher
from fetchCost import CostFetcher
import pandas as pd

URL = (
    "https://www.topuniversities.com/"
    "universities/"
    "massachusetts-institute-technology-mit"
)

topUniLinks = "https://www.topuniversities.com/world-university-rankings"


def main():
    logo = []
    url = []
    desc = []
    courses = []
    cost = []

    data = {
        "Logo" : logo,
        "URL" : url,
        "DESC" : desc,
        "Courses" : courses,
        "Cost" : cost
    }

    try:     

        fetchUniLinks = LinkFetcher(topUniLinks)

        soups = fetchUniLinks.fetch()

        print("*************************")
        print(soups)
        print("*************************")

        for i, soup in enumerate(soups):
            fetchUniDesc = DescFetcher(soup)

            descData = fetchUniDesc.fetchDesc()

            fetchUniCourses = CoursesFetcher(soup)

            CoursesData = fetchUniCourses.fetchCourses()

            fetchUniLogo = LogoFetcher(soup)

            LogoData = fetchUniLogo.fetchLogo()

            fetchUniCost = CostFetcher(soup)

            costData = fetchUniCost.fetchCost()



            print("\n")
            print("################ LOGO ###################")
            print(LogoData)
            logo.insert(i,LogoData)
            print("\n")
            print("############### URL ##################")
            print(soup)
            url.insert(i,soup)
            print("\n")
            print("############### Description ##################")
            print(descData)
            desc.insert(i,descData)
            print("\n")
            print("############### Courses ##################")
            print(CoursesData)
            courses.insert(i,CoursesData)
            print("\n")
            print("############# Cost #################")
            print(costData)
            cost.insert(i,costData)
    
    finally:
        df = pd.DataFrame(data)

        df.to_json("UniData.json",orient="records",indent=4)
        

main()
