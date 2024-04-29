# Harsh Mannava
# This program demonstrates basic functionality to manage a list of tasks.

def add_task(task_list, new_task):
    """
    Adds a new task to the task list.

    Parameters:
    task_list (list): The list of tasks.
    new_task (str): The new task to add.

    Returns:
    None
    """
    task_list.append(new_task)

def remove_task(task_list, task):
    """
    Removes a task from the task list.

    Parameters:
    task_list (list): The list of tasks.
    task (str): The task to remove.

    Returns:
    None
    """
    if task in task_list:
        task_list.remove(task)
    else:
        print("Task not found.")

def display_tasks(task_list):
    """
    Displays all tasks in the task list.

    Parameters:
    task_list (list): The list of tasks.

    Returns:
    None
    """
    print("Tasks:")
    for task in task_list:
        print(task)

def main(choice):
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

choice = input("Enter your choice: ")
main(choice)
