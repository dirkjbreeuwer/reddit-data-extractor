# Reddit Data Extractor

This project uses the Python Reddit API Wrapper (PRAW) to extract data from Reddit, such as posts and comments from specific subreddits, searching for keywords, and more.

## Requirements

- Python 3.6 or higher
- PRAW library

## Installation

1. Install Python 3.6 or higher if you don't already have it on your system.

2. Install the PRAW library by running the following command in your terminal or command prompt:

```bash
pip install praw
```

3. Clone or download this repository.

## Configuration

1. Create a Reddit account if you don't already have one.
2. Register a script app on Reddit:
3. Create a config.ini file in the project directory with the following content:

```ini
[REDDIT]
client_id = your_client_id
client_secret = your_client_secret
user_agent = your_user_agent
username = your_reddit_username
password = your_reddit_password
```

Replace your_client_id, your_client_secret, your_user_agent, your_reddit_username, and your_reddit_password with your corresponding information.