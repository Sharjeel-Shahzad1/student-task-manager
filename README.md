# Student Task Manager

A simple Python console application to manage student tasks.

Project status: Complete

## Features
- Add a task (empty titles are rejected)
- Display all tasks
- Mark a task as completed
- Delete a task using its ID

## Setup
1. Install Python 3.8 or newer.
2. Clone the repository:
   ```bash
   git clone https://github.com/Sharjeel-Shahzad1/student-task-manager.git
   cd student-task-manager
   ```

## Usage
```bash
python task_manager.py
```
Then choose an option from the menu:
```
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

## Running Tests
```bash
python -m unittest discover -s tests -v
```
Tests also run automatically with GitHub Actions on every push and pull request to `main`.

## Documentation
See [docs/user-guide.md](docs/user-guide.md) and [LAB-REPORT.md](LAB-REPORT.md).

## License
MIT
