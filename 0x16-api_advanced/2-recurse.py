#!/usr/bin/python3
"""Contain recursivwe function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return list of titles of all hotposts on given subreddit"""
    reqs = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if reqs.status_code == 200:
        for get_data in reqs.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = reqs.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
