import sys

from textutils.cleaner import clean
from textutils.counter import count_words
from textutils.tokenizer import tokenize


def main() -> None:
    if len(sys.argv) < 2:
        print("You need to write something")
        return
    text = sys.argv[1]
    cleaned = clean(text)
    tokenized = tokenize(cleaned)
    counted = count_words(tokenized)
    print(counted)
