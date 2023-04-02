import configparser
import json
import praw

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Authenticate with the Reddit API using PRAW
reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                     client_secret=config['REDDIT']['client_secret'],
                     user_agent=config['REDDIT']['user_agent'],
                     username=config['REDDIT']['username'],
                     password=config['REDDIT']['password'])

# Define the function to search for posts
def search_posts(subreddit_name, post_limit, search_query, output_file):
    # Get the subreddit object
    subreddit = reddit.subreddit(subreddit_name)

    # Search for posts in the subreddit
    search_results = subreddit.search(search_query, limit=post_limit)

    # Extract relevant information from the search results
    posts = []
    for result in search_results:
        post = {
            'title': result.title,
            'selftext': result.selftext
        }
        posts.append(post)

    # Save the posts to a JSON file
    with open(output_file, 'w') as f:
        json.dump(posts, f)

# Test the function with sample input
subreddit_name = 'careerguidance'
post_limit = 10
search_query = 'need help'
output_file = 'posts.json'
search_posts(subreddit_name, post_limit, search_query, output_file)
