tasks = []
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task number.")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()