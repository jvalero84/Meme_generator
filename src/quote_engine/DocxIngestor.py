"""A module containing a DocxIngestor class."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List
import docx

class DocxIngestor(IngestorInterface):
    """A class DocxIngestor representing a strategy object which realizes IngestorInterface."""
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse a .docx file at the passed destination and output the content as a collection of QuoteModel objects."""
        quotes = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            parse = para.text.split('-')
            quotes.append(QuoteModel(parse[0], parse[1]))
        
        return quotes