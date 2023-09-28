"""
The main module of the application. Contains the FastAPI app and the API endpoints.
"""

# library imports
from src.scripts.get_reddit_comments import get_recent_comments
from src.scripts.get_sentiment_analysis import analyse_sentiments
from src.scripts.sort_comments import sort_comments_by_polarity
from src.scripts.schema import Comment
from src.scripts.get_logger import logger
from typing import List
from datetime import datetime
import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse, RedirectResponse


# Initialise the FastAPI app
app = FastAPI()


# Define exception handler
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles HTTP exceptions, logging the error and returning a JSON response.

    Parameters:
    - request (Request): The request object.
    - exc (HTTPException): The HTTP exception.

    Returns:
    - JSONResponse: A JSON response containing the error details.
    """

    logger.error(f"An error occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


# Define root endpoint
@app.get("/", tags=["Root"])
async def index():
    """
    Redirects the client to the /docs endpoint.

    Returns:
    - RedirectResponse: A redirect response object.
    """

    return RedirectResponse(url="/docs")


# Define analyse endpoint
@app.get("/analyse/{subreddit_name}", response_model=List[Comment])
async def analyse(
    subreddit_name: str,
    start_time: str = None,
    end_time: str = None,
    filter_by: str = None,
    limit: int = Query(25, le=25),
):
    """
    Analyzes the sentiment of recent comments from a specified subreddit.

    Parameters:
    - subreddit_name (str): The name of the subreddit.
    - start_time (str, optional): The start time to filter comments in the format 2023-09-28 15:00.
    - end_time (str, optional): The end time to filter comments in the format 2023-09-28 15:00.
    - filter_by (str, optional): The sentiment to filter comments by (positive, negative, neutral).
    - limit (int, optional): The maximum number of comments to fetch. Default is 25, maximum is 25.

    Returns:
    - List[Comment]: A list of Comment objects containing the sentiment analysis results.
    """

    comments = await get_recent_comments(
        subreddit_name, start_time, end_time, limit
    )  # Make sure to await this async function
    if len(comments) == 0 and type(comments) == str:
        raise HTTPException(
            status_code=404, detail="No comments found in the specified date range."
        )
    else:
        analysed_comments_list = await analyse_sentiments(
            comments
        )  # Assume analyse_sentiments is also an async function
        if filter_by:
            analysed_comments_list = sort_comments_by_polarity(
                analysed_comments_list, filter_by
            )  # Sort comments by polarity if filter_by is provided

        analysed_comments = [
            Comment(
                id=comment["id"],
                text=comment["text"],
                polarity=analysed_comment["scores"]["polarity_scores"]["compound"],
                sentiment=analysed_comment["scores"]["sentiment"],
            )
            for comment, analysed_comment in zip(comments, analysed_comments_list)
        ]
        if len(analysed_comments) == 0:
            raise HTTPException(
                status_code=404, detail="No comments found in the specified date range."
            )
        else:
            return analysed_comments


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
