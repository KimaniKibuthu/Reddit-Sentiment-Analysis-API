"""
This script contains a function to analyse the sentiment of a list of comments using the VADER sentiment analysis tool.
"""

# library imports
from typing import List, Dict, Union

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.scripts.get_logger import logger
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

# Download VADER lexicon
nltk.download("vader_lexicon")


# Define function to analyse the sentiment of a list of comments
def analyse_sentiments(
    comments: List[Dict[str, Union[str, Dict]]]
) -> List[Dict[str, Union[str, Dict]]]:
    """
    Analyzes the sentiment of a list of comments using the VADER sentiment analysis tool.

    Parameters:
    - comments (List[Dict[str, Union[str, Dict]]]): A list of dictionaries, each containing a comment.
      Each dictionary must have a key 'text' with the comment text as the value.

    Returns:
    - List[Dict[str, Union[str, Dict]]]: The input list of comments, updated with a new key 'scores'
      containing the sentiment analysis results for each comment.
    """
    try:
        logger.info("Analysing sentiments...")
        sia = SIA()
        updated_comments_list = []
        for comment in comments:
            score = sia.polarity_scores(comment["text"])
            comment["scores"] = {}
            comment["scores"]["polarity_scores"] = score
            if score["compound"] >= 0.3:
                comment["scores"]["sentiment"] = "positive"
            elif score["compound"] <= -0.3:
                comment["scores"]["sentiment"] = "negative"
            else:
                comment["scores"]["sentiment"] = "neutral"
            updated_comments_list.append(comment)
        logger.info("Sentiments analysed.")
        return updated_comments_list
    except Exception as e:
        logger.error(f"Failed to analyse sentiments: {e}")
        raise


if __name__ == "__main__":
    pass
