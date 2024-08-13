#!/usr/bin/python3

"""
Reddit API Client

This module provides a recursive function to query the Reddit API and return a list
containing the titles of all hot articles for a given subreddit.

Usage:
    recurse(subreddit)

Returns:
    A list of titles of hot articles for the given subreddit, or None if the subreddit
    is not valid
"""

import requests

def recurse(subreddit, after=None, hot_list=None):
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    if after is not None:
        url += f"?after={after}"
    headers = {"User-Agent": "Reddit API Client"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if "after" in data["data"]:
            recurse(subreddit, data["data"]["after"], hot_list)
        return hot_list
    else:
        return None
