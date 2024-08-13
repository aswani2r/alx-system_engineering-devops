#!/usr/bin/python3

"""
Reddit API Client

This module provides a recursive function to query the Reddit API, parse the title
of all hot articles, and print a sorted count of given keywords.

Usage:
    count_words(subreddit, word_list)

Returns:
    None
"""

import requests
import re

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles
    for a given subreddit and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): The list of keywords to count.
        after (str, optional): The pagination token to use for the next page of results.
        word_count (dict, optional): The dictionary to store the count of each keyword.

    Returns:
        None
    """
    if after is None:
        after = ""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    if after:
        url += f"?after={after}"
    headers = {"User-Agent": "Reddit API Client"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                count = len(re.findall(r'\b' + re.escape(word) + r'\b', title))
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count
        if "after" in data["data"]:
            count_words(subreddit, word_list, data["data"]["after"], word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return

def main(subreddit, word_list):
    count_words(subreddit, word_list)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        main(sys.argv[1], [x for x in sys.argv[2].split()])
