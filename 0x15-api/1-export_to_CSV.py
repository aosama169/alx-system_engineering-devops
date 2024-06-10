#!/usr/bin/python3
"""Export todo list information forgiven employee to CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    urlc = "https://jsonplaceholder.typicode.com/"
    user = requests.get(urlc + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(urlc + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
