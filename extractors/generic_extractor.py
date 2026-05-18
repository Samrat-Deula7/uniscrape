import re

from .utils import clean


class GenericExtractor:

    def __init__(self, soup):

        self.soup = soup

    def extract(self):

        data = {}

        # title
        h1 = self.soup.find("h1")

        data["name"] = (
            clean(h1.get_text())
            if h1 else None
        )

        # meta description
        meta = self.soup.find(
            "meta",
            attrs={
                "name": "description"
            }
        )

        data["description"] = (
            meta.get("content")
            if meta else None
        )

        # images
        images = []

        for img in self.soup.find_all("img"):

            src = img.get("src")

            if src:
                images.append(src)

        data["images"] = list(
            set(images)
        )

        # tuition regex
        text = self.soup.get_text(
            " ",
            strip=True
        )

        fees = re.findall(
            r'[\$£€₹]\s?[\d,]+',
            text
        )

        data["fees"] = list(
            set(fees)
        )

        # programs
        programs = {
            "bachelors": [],
            "masters": [],
            "phd": []
        }

        for a in self.soup.find_all("a"):

            txt = clean(
                a.get_text()
            )

            if not txt:
                continue

            lower = txt.lower()

            if any(x in lower for x in [
                "bachelor",
                "undergraduate",
                "bsc"
            ]):
                programs["bachelors"].append(txt)

            elif any(x in lower for x in [
                "master",
                "mba",
                "msc",
                "postgraduate"
            ]):
                programs["masters"].append(txt)

            elif any(x in lower for x in [
                "phd",
                "doctorate"
            ]):
                programs["phd"].append(txt)

        data["programs"] = programs

        return data
