class Task:
   def _init_(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.description} - Due: {task.due_date} - Priority: {task.priority}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task removed successfully.")
        else:
            print("Invalid task index.")

# Example usage:
todo_list = ToDoList()
todo_list.add_task(Task("Complete project", "2023-11-15", "High"))
todo_list.add_task(Task("Read a book", "2023-11-20", "Medium"))

todo_list.display_tasks()

# Mark the first task as completed
todo_list.mark_completed(1)

# Update the second task
todo_list.update_task(2, "Read two chapters", "2023-11-25", "High")

# Remove the first task
todo_list.remove_task(1)

# Display the updated tasks
todo_list.display_tasks()
