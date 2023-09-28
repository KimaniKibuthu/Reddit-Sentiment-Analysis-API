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
async def get_recent_comments(
    subreddit_name: str,
    start_time: datetime = None,
    end_time: datetime = None,
    limit: int = 25,
) -> List[Dict[str, str]]:
    """
    Fetches the most recent comments from a specified subreddit and filters them by date if specified.

    Parameters:
    - subreddit_name (str): The name of the subreddit from which to fetch comments.
    - start_time (str, optional): The start time of the date range eg. 2023-09-28 15:00
    - end_time (str, optional): The end time of the date range eg. 2023-09-28 15:00
    - limit (int, optional): The maximum number of comments to fetch. Default is 25.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries, each containing the id, text, and creation time of a comment.
    """

    try:
        logger.info(f"Fetching recent comments from r/{subreddit_name}...")
        subreddit = reddit.subreddit(subreddit_name)
        comments = [
            {"id": comment.id, "text": comment.body, "created_utc": comment.created_utc}
            for comment in subreddit.comments(limit=limit)
        ]

        if start_time and end_time:
            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M").timestamp()
            end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M").timestamp()

            # Filter the comments based on the start and end times
            filtered_comments = [
                comment
                for comment in comments
                if start_time <= comment["created_utc"] <= end_time
            ]

            # Sort the filtered comments based on the 'created_utc' field
            sorted_comments = sorted(
                filtered_comments, key=lambda x: x["created_utc"], reverse=True
            )
            logger.info(f"Comments fetched and filtered by date range.")

            return sorted_comments

        else:
            return comments

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e


if __name__ == "__main__":
    pass
