import json


class JSONLDExtractor:

    def __init__(self, soup):
        self.soup = soup

    def extract(self):

        data = {
            "jsonld": []
        }

        scripts = self.soup.find_all(
            "script",
            type="application/ld+json"
        )

        for script in scripts:

            try:
                content = script.string

                if not content:
                    continue

                parsed = json.loads(content)

                data["jsonld"].append(parsed)

            except Exception:
                continue

        return data
