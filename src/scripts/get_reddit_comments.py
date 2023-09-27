"""
This script fetches the most recent comments from a specified subreddit.
"""
# library imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import praw
from src.scripts.get_logger import logger
from datetime import datetime
from typing import List, Dict
from src.scripts.config import load_config


# Get credentials from config file
configs = load_config()

CLIENT_ID = configs["CLIENT_ID"]
CLIENT_SECRET = configs["CLIENT_SECRET"]
USER_AGENT = configs["USER_AGENT"]

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT
)


# Define function to fetch recent comments from a subreddit
def get_recent_comments(subreddit_name: str, limit: int = 25) -> List[Dict[str, str]]:
    """
    Fetches the most recent comments from a specified subreddit.

    Parameters:
    - subreddit_name (str): The name of the subreddit from which to fetch comments.
    - limit (int, optional): The maximum number of comments to fetch. Default is 25.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries, each containing the id, text, and creation time of a comment.
    """
    try:
        logger.info(f"Fetching recent comments from r/{subreddit_name}...")
        subreddit = reddit.subreddit(subreddit_name)
        logger.info(f"Comments fetched.")
        return [
            {
                "id": comment.id,
                "text": comment.body,
                "created_utc": datetime.utcfromtimestamp(comment.created_utc).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            }
            for comment in subreddit.comments(limit=limit)
        ]

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e


if __name__ == "__main__":
    pass
