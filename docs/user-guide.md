# User Guide

## Starting the app
Open a terminal in the project folder and run:
```bash
python task_manager.py
```

## Menu options
| Option | What it does |
|--------|--------------|
| 1. Add task | Type a title. Empty titles are not allowed. |
| 2. Show tasks | Lists all tasks. `[X]` means completed, `[ ]` means pending. |
| 3. Complete task | Enter the task ID to mark it as done. |
| 4. Delete task | Enter the task ID to remove it. |
| 5. Exit | Closes the app. |

## Example
```
Choose: 1
Task title: Submit DevOps assignment
Task 1 added.

Choose: 3
Task ID: 1
Task marked as completed.

Choose: 2
1. [X] Submit DevOps assignment
```

## Notes
- Task IDs are shown in the task list.
- Entering an ID that does not exist shows an error message.
- Tasks are kept in memory and are cleared when the app closes.
