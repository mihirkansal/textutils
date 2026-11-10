import string


def clean(text: str) -> str:
    text = text.lower()
    result = ""
    for char in text:
        if char not in string.punctuation:
            result = result + char
    return result
