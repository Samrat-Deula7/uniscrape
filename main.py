import json

from fetchUniLinks import LinkFetcher

URL = (
    "https://www.topuniversities.com/"
    "universities/"
    "massachusetts-institute-technology-mit"
)

topUniLinks = "https://www.topuniversities.com/world-university-rankings"


def main():

    fetchUniLinks = LinkFetcher(topUniLinks)

    soups = fetchUniLinks.fetch()

    print("*************************")
    print(soups)
    print("*************************")


main()
