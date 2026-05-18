import requests


class AlgoliaExtractor:

    def __init__(
        self,
        app_id,
        api_key,
        index_name
    ):

        self.app_id = app_id
        self.api_key = api_key
        self.index_name = index_name

    def search(self, query):

        url = (
            f"https://{self.app_id}"
            f"-dsn.algolia.net/1/indexes/"
            f"{self.index_name}/query"
        )

        headers = {
            "X-Algolia-API-Key":
                self.api_key,

            "X-Algolia-Application-Id":
                self.app_id,

            "Content-Type":
                "application/json"
        }

        payload = {
            "query": query,
            "hitsPerPage": 50
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            return {}

        return response.json()
