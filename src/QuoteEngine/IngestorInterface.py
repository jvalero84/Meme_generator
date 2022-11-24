"""A module containing an IngestorInterface class."""

from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """A class representing an abstract interface that defines common aspects of concrete document ingestors."""

    @classmethod
    def can_ingest(cls, path:str) -> bool:
        """A class method that determines if the given file can be imported."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
