#!/usr/bin/python3
"""
Script to retrieve and display employee TODO list progress.
"""

import requests
import sys

def fetch_todo_list(employee_id):
    """
    Fetches and returns the TODO list for the given employee ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()

def display_progress(employee_id, todo_list):
    """
    Displays the progress of the employee's TODO list.
    """
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    num_completed_tasks = len(completed_tasks)
    employee_name = todo_list[0]['name'] if todo_list else "Unknown"

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    print(f"\t{employee_name}: {num_completed_tasks} / {total_tasks}")
    print("Completed tasks:")
    for task in completed_tasks:
        print(f"\t- {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = fetch_todo_list(employee_id)
    display_progress(employee_id, todo_list)

