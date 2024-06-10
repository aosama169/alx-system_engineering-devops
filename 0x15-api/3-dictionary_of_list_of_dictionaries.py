#!/usr/bin/python3
"""Export todo list information of all employees to JSON"""
import json
import requests

if __name__ == "__main__":
    urlc = "https://jsonplaceholder.typicode.com/"
    users = requests.get(urlc + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(urlc + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
