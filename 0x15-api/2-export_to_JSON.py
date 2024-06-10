#!/usr/bin/python3
"""Export todo list information for a given employee to JSON"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    urlc = "https://jsonplaceholder.typicode.com/"
    user = requests.get(urlc + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(urlc + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
