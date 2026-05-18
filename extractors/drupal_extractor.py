import json


class DrupalExtractor:

    def __init__(self, soup):
        self.soup = soup

    def extract(self):

        data = {}

        script = self.soup.find(
            "script",
            attrs={
                "data-drupal-selector":
                "drupal-settings-json"
            }
        )

        if not script:
            return data

        try:

            parsed = json.loads(script.string)

            data["drupal"] = parsed

            # algolia
            algolia = parsed.get(
                "qs_global_site_search",
                {}
            )

            data["algolia"] = {
                "app_id": algolia.get("app_id"),
                "api_key": algolia.get("api_key"),
                "program_index":
                    algolia.get(
                        "algolia_program_index"
                    ),
                "university_index":
                    algolia.get(
                        "algolia_university_index"
                    )
            }

            # ranking history
            qs_profiles = parsed.get(
                "qs_profiles",
                {}
            )

            data["ranking_history"] = (
                qs_profiles.get(
                    "json_data",
                    []
                )
            )

            # similar universities
            similar = parsed.get(
                "similarUniversities",
                {}
            )

            data["similar_university_api"] = (
                similar.get(
                    "endpoints",
                    {}
                )
            )

        except Exception:
            pass

        return data
