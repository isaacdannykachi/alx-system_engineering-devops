#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
