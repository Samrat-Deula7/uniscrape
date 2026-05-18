import json

from fetcher import PageFetcher
from parser import UniversityParser


URL = (
    "https://www.topuniversities.com/"
    "universities/"
    "massachusetts-institute-technology-mit"
)


def main():

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
