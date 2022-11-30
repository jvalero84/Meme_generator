
"""A module containing a QuoteModel class."""
class QuoteModel:
    """A class representing a Quote made up of a quote body and the author."""

    def __init__(self, body:str, author:str):
        """Construct a QuoteModel object initializing two attributes."""
        self.body = body
        self.author = author
    
    def __str__(self):
        """Print the string representation of this object as "body" - author."""
        return f'\"{self.body}\" - {self.author}'