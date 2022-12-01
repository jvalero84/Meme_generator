"""A module containing a PDFIngestor class."""

from typing import List
import subprocess
from subprocess import CalledProcessError
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """A class PDFIngestor representing a strategy object which realizes IngestorInterface."""

    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a .pdf file at the passed destination and output the content as a collection of QuoteModel objects."""
        quotes = []
        if not os.path.isdir('./tmp'):
            os.makedirs('./tmp')
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        try:
            call = subprocess.run(['pdftotext', '-layout', path, tmp])
        except CalledProcessError as ex:
            print(ex)
        else:
            file_ref = open(tmp, "r")
        
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    quote = QuoteModel(parse[0], (parse[1]))
                    quotes.append(quote)
                
            file_ref.close()
        finally:
            os.remove(tmp)
        return quotes