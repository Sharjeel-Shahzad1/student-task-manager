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


def find_task(tasks, task_id):
    """Return the task with the given id, or None."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(tasks, task_id):
    """Mark a task as completed."""
    task = find_task(tasks, task_id)
    if task is None:
        raise ValueError(f"No task with id {task_id}.")
    task["done"] = True
    return task


def show_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "X" if t["done"] else " "
        print(f'{t["id"]}. [{status}] {t["title"]}')


def ask_id():
    """Ask the user for a task id and return it as an int (or None)."""
    value = input("Task ID: ").strip()
    if not value.isdigit():
        print("Please enter a valid number.")
        return None
    return int(value)


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
        elif choice == "3":
            task_id = ask_id()
            if task_id is not None:
                try:
                    complete_task(tasks, task_id)
                    print("Task marked as completed.")
                except ValueError as error:
                    print(f"Error: {error}")
        elif choice == "4":
            print("Coming soon.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
