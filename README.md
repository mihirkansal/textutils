# textutils

A small command-line tool that cleans text, splits it into words, and counts how often each word appears.

## Install

Requires [uv](https://docs.astral.sh/uv/) and Python 3.15+.

```
uv tool install git+https://github.com/mihirkansal/textutils
```

## Usage

```
textutils "The cat! THE dog? the end."
```

Output:

```
{'the': 3, 'cat': 1, 'dog': 1, 'end': 1}
```

The text is lowercased and stripped of punctuation before counting, so `The`, `THE`, and `the` all count as the same word.

You can also use the functions from Python:

```python
from textutils.cleaner import clean
from textutils.counter import count_words
from textutils.tokenizer import tokenize

count_words(tokenize(clean("Hello, hello world!")))
# {'hello': 2, 'world': 1}
```

## Development

```
git clone https://github.com/mihirkansal/textutils
cd textutils
uv sync
```

Before committing, run:

```
uv run ruff check
uv run ruff format --check
uv run mypy src
```
