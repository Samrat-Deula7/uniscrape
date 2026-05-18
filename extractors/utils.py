import re


def clean(text):

    if not text:
        return None

    return re.sub(
        r"\s+",
        " ",
        text
    ).strip()
