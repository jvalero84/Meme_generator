"""A module containing an IngestorInterface class."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """A class representing an abstract interface that defines common aspects of concrete document ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path:str) -> bool:
        """Determine whether the provided file can be consumed by the importer."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Parse the file at the passed destination and output the content as a collection of QuoteModel objects. To be implemented on strategy objects."""
        pass
