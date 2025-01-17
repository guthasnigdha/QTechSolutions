class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            print(f'Task "{task}" added successfully!')
        else:
            print("Invalid task. Cannot add an empty task.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed successfully!')
        else:
            print("Invalid task number. Please try again.")

    def view_tasks(self):
        if self.tasks:
            print("\nCurrent Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("\nYour task list is empty!")


def main():
    manager = ToDoListManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                task = input("Enter the task you want to add: ").strip()
                manager.add_task(task)

            elif choice == 2:
                manager.view_tasks()
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    manager.delete_task(task_number)
                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif choice == 3:
                manager.view_tasks()

            elif choice == 4:
                print("Exiting To-Do List Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
