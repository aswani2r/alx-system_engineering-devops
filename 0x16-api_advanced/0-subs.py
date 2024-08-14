#!usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    base_url = "https://www.reddit.com/r/"
    headers = {
        "User-Agent": "YourAppName/1.0"
    }
    
    url = f"{base_url}{subreddit}.json"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()

            subscriber_count = data[1]['data']['children'][0]['data']['subscriber_count']
            
            return subscriber_count
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
