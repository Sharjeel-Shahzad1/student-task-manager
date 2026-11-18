"""Student Task Manager - a simple console app to manage tasks."""


def show_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "X" if t["done"] else " "
        print(f'{t["id"]}. [{status}] {t["title"]}')
