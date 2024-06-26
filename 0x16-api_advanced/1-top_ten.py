#!/usr/bin/python3
"""Contain top ten func"""
import requests


def top_ten(subreddit):
    """Print titles of 10 hottest posts on given subreddit"""
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
