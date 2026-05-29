import json

from fetcher import PageFetcher
from fetchUniLinks import LinkFetcher
from parser import UniversityParser

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

    fetcher = PageFetcher(URL)

    html, soup = fetcher.fetch()

    parser = UniversityParser(
        html,
        soup
    )

    data = parser.parse()

    print(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        )
    )


if __name__ == "__main__":
    main()
