"""A module containing a CSVIngestor class."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

from typing import List
import pandas

class CSVIngestor(IngestorInterface):
    """A class CSVIngestor representing a strategy object which realizes IngestorInterface."""
    
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse a .csv file at the passed destination and output the content as a collection of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception')
        
        quotes = []
        
        dataframe = pandas.read_csv(path, header=0)
        
        for index, row in dataframe.iterrows():
            quotes.append(QuoteModel(row['body'], row['author']))
        
        return quotes