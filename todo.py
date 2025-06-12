import sys
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.writelines(task + "\n" for task in tasks)

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: {task}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index] = "[✔] " + tasks[index]
        save_tasks(tasks)
        print("Marked as done.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        print(f"Deleted: {tasks[index]}")
        del tasks[index]
        save_tasks(tasks)
    else:
        print("Invalid task number.")

def show_help():
    print("Usage:")
    print("  python todo.py add \"Task name\"")
    print("  python todo.py list")
    print("  python todo.py done <task_number>")
    print("  python todo.py delete <task_number>")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) == 3:
        mark_done(int(sys.argv[2]) - 1)
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]) - 1)
    else:
        show_help()
