tasks = []

def add_task():
    task = (input("Task: "))
    tasks.append(task)
    print(f"{task} added!")

def view_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    return ""

def complete_task():
    try:
       number = int(input("Task number you want to mark as complete: ")) - 1
    if 0 <= number < len(tasks):
       removed = tasks.pop(number)
       print(f"{removed} is completed!")
    else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n1. Add  2. View  3. Complete  4. Exit")
        choice = input("Pick one of the decisions: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            break
        else:
            print("Only pick from numbers 1-4, please.")

if __name__ == "__main__":
    main()
