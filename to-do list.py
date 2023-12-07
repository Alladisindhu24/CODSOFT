class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_title, new_status):
        for task in self.tasks:
            if task.title == task_title:
                task.status = new_status
                return True
        return False

    def display_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print(f"Title: {task.title}\nDescription: {task.description}\nStatus: {task.status}\n")

def main():
    O= TodoList()

    while True:
        print("\n1. Add Task\n2. Update Task Status\n3. Display Tasks\n4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            O.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            task_title = input("Enter task title to update status: ")
            new_status = input("Enter new status (e.g., 'Complete' or 'Incomplete'): ")
            if O.update_task_status(task_title, new_status):
                print("Task status updated successfully!")
            else:
                print("Task not found.")

        elif choice == "3":
            O.display_tasks()

        elif choice == "4":
            print("Exiting the to-do list application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    print("WELCOME TO TO-DO LIST APPLICATION!")
    main()

