"""A module containing a TextIngestor class."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List

class TextIngestor(IngestorInterface):
    """A class TextIngestor representing a strategy object which realizes IngestorInterface."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse a .txt file at the passed destination and output the content as a collection of QuoteModel objects."""
        quotes = []

        with open(path, 'r') as infile:
            for line in infile.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], int(parse[1]))
                    quotes.append(quote)
        
        return quotes
