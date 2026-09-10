import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text while preserving the actual content.
    """

    if not text:
        return ""

    # Replace Windows-style line endings with standard newlines
    text = text.replace("\r\n", "\n")

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces at the beginning/end of lines
    text = "\n".join(line.strip() for line in text.split("\n"))

    # Replace 3 or more consecutive newlines with 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()