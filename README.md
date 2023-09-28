# Reddit Sentiment Analysis API Documentation

## Project Overview

This project is a RESTful API developed using FastAPI to analyze sentiments of recent comments from specified subreddits using Reddit's API and the NLTK library. The comments are analyzed using VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool provided by the NLTK library.


## Project Structure

```
Reddit_Sentiment_Analysis_API/
├── src/
│   ├── __init__.py
│   ├── scripts/
│   │   ├── __init__.py
|   |   ├── config.py
│   │   ├── get_reddit_comments.py
│   │   ├── get_sentiment_analysis.py
│   │   ├── get_logger.py
│   │   └── schema.py
│   └── logs/
├── config.json
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```


## Setup Instructions

### 1. Local Setup

1. Clone the repository to your local machine.

    `git clone https://github.com/KimaniKibuthu/Reddit-Sentiment-Analysis-API.git`

2. Go to https://www.reddit.com/prefs/apps. Here:
    - Click on the tab **apps**
    - Create app. As you create app choose **script**.
    - Copy the CLIENT ID and the CLIENT SECRET and copy them into the respective keys in the config.json.

3. Navigate to the project's root directory.
4. Create a virtual environment of your choice eg:
   ```bash
   python -m venv venv
   ```
5. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/Mac: `source venv/bin/activate`
6. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
7. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

   Open your browser and navigate to http://localhost:8080. You should see the FastAPI application running.

### 2. Docker Setup

1. Navigate to the project's root directory.
2. Go to https://www.reddit.com/prefs/apps. Here:
    - Click on the tab **apps**
    - Create app. As you create app choose **script**.
    - Copy the CLIENT ID and the CLIENT SECRET and copy them into the respective keys in the config.json.
3. Build the Docker image:
   ```bash
   docker build -t reddit-api .
   ```
4. Run the Docker container:
   ```bash
   docker run -d -p 8080:8080 reddit-api
   ```
5. Verify the Application:

    Open your browser and navigate to http://localhost:8080. You should see the FastAPI application running.
---

## API Usage

### Endpoint: `/analyse/{subreddit_name}`

- Method: `GET`
- URL Params:
  - `subreddit_name` (str): Name of the subreddit from which to fetch comments.
  - `start_time` (str, optional): The start time to filter comments in the format 2023-09-28 15:00.
  - `end_time` (str, optional): The end time to filter comments in the format 2023-09-28 15:00.
  - `filter_by` (str, optional): The sentiment to filter comments by (positive, negative, neutral).
  - `limit` (int, optional): The maximum number of comments to fetch and analyze. Default is 25, maximum is 100.
- Sample call using curl:
  `curl -X 'GET' \
  'http://localhost:8080/analyse/programming?start_time=2023-09-20%2015%3A00&end_time=2023-09-28%2018%3A00&filter_by=positive&limit=25' \
  -H 'accept: application/json'`
- Sample Postman request:
    `http://localhost:8080/analyse/programming?start_time=2023-09-20%2015%3A00&end_time=2023-09-28%2018%3A00&filter_by=positive&limit=25`


### Example Response

The response will be as follows:
```
[
  {
    "id": "k2lc0zj",
    "text": "This would be more damning if Oracle was a tech company.",
    "polarity": 0.7155,
    "sentiment": "positive"
  },
  {
    "id": "k2lbqxw",
    "text": "Sweet.  Hopefully this means I could open a browser tab or two without it choking so badly like earlier models.",
    "polarity": 0.7893,
    "sentiment": "positive"
  },
  {
    "id": "k2lbh5c",
    "text": "I hate oracle almost religiously. Like when the day comes that the company burns to the ground and goes bankrupt (,if it ever does) I will celebrate.\n\nUntil then it warms my heart that their flagship product is difficult to maintain.",
    "polarity": 0.34,
    "sentiment": "positive"
  },
  {
    "id": "k2lb9ao",
    "text": "The Pi 4 already has a hardware HEVC decoder. Not sure what the 'pain point' was with it, but the decoder in the Pi 5 is very likely to be the same.\nAnd the specs don't mention any AV1 hardware decoding, so it's safe to assume it's not supported.",
    "polarity": 0.3182,
    "sentiment": "positive"
  },
  {
    "id": "k2laet2",
    "text": "Thanks for the help.  Is default sort price high to low or something?  Doesn't seem very consumer friendly.",
    "polarity": 0.3612,
    "sentiment": "positive"
  },
  {
    "id": "k2la9px",
    "text": "It's for flexibility, besides there's not a lot of room on the PCB for a SSD to begin with, even the smallest m.2 drives are nearly a quarter of the PCB",
    "polarity": 0.34,
    "sentiment": "positive"
  }
]
```

## Logging

Logs are written to the `logs/` directory located under the `src/` directory. The logging is configured in `src/scripts/get_logger.py`.



## License

[MIT License](https://opensource.org/licenses/MIT)
