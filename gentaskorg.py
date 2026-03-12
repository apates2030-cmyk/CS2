import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def add_task():
    task = input("Task: ").strip()

    if task == "":
        print("Enter a valid task.")
        return

    priority = input("Priority (High/Medium/Low): ")
    due = input("Due date: ")

    tasks.append({
        "task": task,
        "priority": priority,
        "due": due
    })

    print(f"{task} added!")
    save_tasks()


def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return

    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['task']} | Priority: {t['priority']} | Due: {t['due']}")


def complete_task():
    try:
        number = int(input("Task number you want to mark as complete: ")) - 1

        if 0 <= number < len(tasks):
            removed = tasks.pop(number)
            print(f"{removed['task']} is completed!")
            save_tasks()
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    load_tasks()

    while True:
        print("\n---- TASK ORGANIZER ----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        print("---------------------------")

        choice = input("Pick an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            save_tasks()
            break
        else:
            print("Only pick from numbers 1–4 :)")


if __name__ == "__main__":
    main()
