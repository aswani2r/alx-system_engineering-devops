#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for employee {employee_id}.")
        return

    todos = response.json()

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    employee_name = todos[0]['username']
    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
