# todo.py

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number!")

# Simple test
if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Build a project")
    show_tasks()
    remove_task(0)
    show_tasks()
