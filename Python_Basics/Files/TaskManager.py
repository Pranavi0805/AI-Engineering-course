"""
Project: Task Manager using File Handling

Description:
This project is a simple command-line Task Manager built using Python.
It demonstrates Python file handling concepts by storing tasks in a text file.

Features:
1. Add a new task.
2. View all tasks.
3. Mark a task as complete.
4. Delete a task.
5. Save tasks before exiting.

The tasks are stored in:
Python_Basics/Files/data/tasks.txt
"""

import os

# Base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create data folder if it doesn't exist
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# File to store tasks
FILE_NAME = os.path.join(DATA_DIR, "tasks.txt")


# Load tasks from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")


# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")


# Main Menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_task_complete(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye")
            break

        else:
            print("Invalid Choice. Please try again")


if __name__ == "__main__":
    main()