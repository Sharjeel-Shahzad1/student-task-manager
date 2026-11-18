"""Student Task Manager - a simple console app to manage tasks."""


def add_task(tasks, title):
    """Add a new task."""
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "title": title, "done": False}
    tasks.append(task)
    return task


def show_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "X" if t["done"] else " "
        print(f'{t["id"]}. [{status}] {t["title"]}')
