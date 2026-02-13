# Console-Based To-Do List Application

tasks = []


# Function to display menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


# Function to add task
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added successfully!")


# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t['task']} - {t['status']}")


# Function to mark task as completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Done"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Function to delete task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# Main Program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you! Exiting To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Program
if __name__ == "__main__":
    main()
