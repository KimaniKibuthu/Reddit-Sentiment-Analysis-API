"""
The main module of the application. Contains the FastAPI app and the API endpoints.
"""

# library imports
from src.scripts.get_reddit_comments import get_recent_comments
from src.scripts.get_sentiment_analysis import analyse_sentiments
from src.scripts.schema import Comment
from src.scripts.get_logger import logger
from typing import List
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
async def analyse(subreddit_name: str, limit: int = Query(25, le=25)):
    """
    Analyzes the sentiment of recent comments from a specified subreddit.

    Parameters:
    - subreddit_name (str): The name of the subreddit.
    - limit (int, optional): The maximum number of comments to fetch. Default is 25, maximum is 25.

    Returns:
    - List[Comment]: A list of Comment objects containing the sentiment analysis results.
    """

    comments = get_recent_comments(subreddit_name, limit)
    analysed_comments_list = analyse_sentiments(
        comments
    )  # Pass the entire list of comments
    analysed_comments = []
    for comment, analysed_comment in zip(comments, analysed_comments_list):
        analysed_comments.append(
            Comment(
                id=comment["id"],
                text=comment["text"],
                polarity=analysed_comment["scores"]["polarity_scores"]["compound"],
                sentiment=analysed_comment["scores"]["sentiment"],
            )
        )
    return analysed_comments


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
