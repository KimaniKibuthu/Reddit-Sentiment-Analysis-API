from typing import List, Dict, Union

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.scripts.get_logger import logger


def sort_comments_by_polarity(
    comments: List[Dict[str, Union[str, Dict]]], filter_by: str = None
) -> List[Dict[str, Union[str, Dict]]]:
    """
    Filters a list of comments based on sentiment polarity specified by the `filter_by` argument.

    Each comment is a dictionary which should have a nested dictionary under the key 'scores',
    which in turn should have a key named 'sentiment' with values either 'positive', 'negative',
    or 'neutral'.

    Parameters:
    - comments : List[Dict[str, Union[str, Dict]]]
        A list of dictionaries where each dictionary represents a comment and its associated scores.

    - filter_by : str, optional
        A string specifying the sentiment polarity to filter comments by. Acceptable values are
        'positive', 'negative', 'neutral'. The function is case-insensitive to this argument.
        If this argument is None (default), the function returns the input list `comments` unmodified.

    Returns:

    - List[Dict[str, Union[str, Dict]]]
        A list of dictionaries representing comments filtered by the specified sentiment polarity.
        If `filter_by` is None, the original `comments` list is returned unmodified.

    """
    filtered_comments = []
    if filter_by == None:
        logger.info("comments not sorted by polarity.")
        return comments
    else:
        if filter_by.lower() == "positive":
            for comment in comments:
                if comment["scores"]["sentiment"] == "positive":
                    filtered_comments.append(comment)

        elif filter_by.lower() == "negative":
            for comment in comments:
                if comment["scores"]["sentiment"] == "negative":
                    filtered_comments.append(comment)

        elif filter_by.lower() == "neutral":
            for comment in comments:
                if comment["scores"]["sentiment"] == "neutral":
                    filtered_comments.append(comment)
        logger.info("Comments sorted by polarity.")
        return filtered_comments


if __name__ == "__main__":
    pass
