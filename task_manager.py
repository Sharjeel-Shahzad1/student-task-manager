"""Student Task Manager - a simple console app to manage tasks."""


def add_task(tasks, title):
    """Add a new task. Rejects empty titles."""
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
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


def main():
    tasks = []
    while True:
        print("\n1. Add task\n2. Show tasks\n3. Complete task\n4. Delete task\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                task = add_task(tasks, input("Task title: "))
                print(f"Task {task['id']} added.")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "2":
            show_tasks(tasks)
        elif choice in ("3", "4"):
            print("Coming soon.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
