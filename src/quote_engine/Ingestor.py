"""A module containing a DocxIngestor class."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor

from typing import List

class Ingestor(IngestorInterface):
    """A class encapsulating all the ingestors to provide an interface to load any supported file type."""
    
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse a file at the passed destination and output the content as a collection of QuoteModel objects. It resolves the right ingestor by the extension of the file path."""
        quotes = []
        ingested = False
        for imp in cls.importers:
            if imp.can_ingest(path):
                try:
                    quotes = imp.parse(path)
                except BaseException as ex:
                    print(str(ex))
                    raise BaseException(f'The file {path} could not be parsed.')
                else:
                    ingested = True
                    break
        if ingested:
            return quotes
        else:
            raise BaseException(f'The file {path} could not be parsed.')
            