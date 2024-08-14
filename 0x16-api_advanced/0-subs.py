#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':'python3:subreddit.subscriber.counter:v1.0 (by /u/your_username)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers")
    else:
        return 0
except requests.RequestException:
	return 0
