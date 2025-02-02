import json
from datetime import datetime
from tabulate import tabulate


def display_menu():
    print("\n--To Do List--")
    print("1. View All Tasks")
    print("2. Add New Task")
    print("3. Mark Task as Completed")
    print("4. Delete Tasks")
    print("5. Save and Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nThe to do list is empty!")
    else:
        table_data = []
        for index, task in enumerate(tasks, start = 1):
            status = "Completed" if task["completed"] else "Not Completed"
            table_data.append([
                index,
                task["name"],
                task["start_date"],
                task["start_time"],
                task["due_date"],
                task["due_time"],
                status
            ])
        headers = ["#", "Task Name", "Start Date", "Start Time", "Due Date", "Due Time", "Status"]
        print("\nYour To-Do List:")
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


def add_task(tasks):
    name = input("Input Task Name:")
    now = datetime.now()
    start_date = now.strftime("%Y-%m-%d")
    start_time = now.strftime("%H:%M")
    due_date = input("Enter due date using format (YYYY-MM-DD):")
    due_time = input("Enter due time using format (HH:MM):")

    try:
        due_datetime = datetime.strptime(due_date + " " + due_time, "%Y-%m-%d %H:%M")
        start_datetime = datetime.strptime(start_date + " " + start_time, "%Y-%m-%d %H:%M")

        if due_datetime <= start_datetime:
            print("Due date and time must be later than the start date and time. Please try again.")
            return
    except ValueError:
        print("Invalid date or time, please try again.")
        return

    task = {
        "name": name,
        "start_date": start_date,
        "start_time": start_time,
        "due_date": due_date,
        "due_time": due_time,
        "completed": False
    }
    tasks.append(task)
    print(f"Task" '{name}' "added!")

def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Please input task number to mark as completed:"))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"Task '{tasks[task_num - 1]['name']}' completed!")
        else:
            print("Invalid Task Number")
    except ValueError:
        print("Enter Valid Number")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Please input task number to mark as completed:"))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(F"Task '{removed_task['name']}' Removed!")
        else:
            print("Invalid Task Number")
    except ValueError:
        print("Enter Valid Number")



def save_tasklist(tasks, filename = "todo.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file)
        print("To do List Saved")

def load_tasklist(filename = "todo.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        return[]


def main():
    tasks = load_tasklist()
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasklist(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
