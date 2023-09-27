"""
This module contains the Pydantic model for a Comment, which is used to validate the data
"""
from pydantic import BaseModel

class Comment(BaseModel):
    """
    Pydantic model for a Comment, with id, text, polarity, and sentiment fields.
    """
    id: str
    text: str
    polarity: float
    sentiment: str