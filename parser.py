from extractors.jsonld_extractor import (
    JSONLDExtractor
)

from extractors.drupal_extractor import (
    DrupalExtractor
)

from extractors.generic_extractor import (
    GenericExtractor
)

from extractors.algolia_extractor import (
    AlgoliaExtractor
)


class UniversityParser:

    def __init__(self, html, soup):

        self.html = html
        self.soup = soup

    def parse(self):

        final = {}

        jsonld = JSONLDExtractor(
            self.soup
        ).extract()

        final.update(jsonld)

        drupal = DrupalExtractor(
            self.soup
        ).extract()

        final.update(drupal)

        generic = GenericExtractor(
            self.soup
        ).extract()

        final.update(generic)

        algolia = final.get(
            "algolia",
            {}
        )

        if (
            algolia.get("app_id")
            and
            algolia.get("api_key")
            and
            algolia.get("program_index")
        ):

            searcher = AlgoliaExtractor(
                app_id=algolia["app_id"],
                api_key=algolia["api_key"],
                index_name=algolia["program_index"]
            )

            query = final.get(
                "name",
                ""
            )

            programs = searcher.search(
                query
            )

            final["algolia_programs"] = (
                programs
            )

        return final
