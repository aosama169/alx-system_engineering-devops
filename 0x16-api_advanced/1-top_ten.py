#!/usr/bin/python3
"""Contain top ten func"""
import requests


def top_ten(subreddit):
    """Print titles of 10 hottest posts on given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    result = response.json().get("data")
    [print(c.get("data").get("title")) for c in result.get("children")]