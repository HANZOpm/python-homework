class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Task ID: {self.task_id}\n" \
               f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Due date: {self.due_date}\n" \
               f"Status: {self.status}"

class TaskManager:
    statuses = ["pending", "in progress", "completed"]
    def __init__(self):
        self.tasks = []

    def get_task_by_id(self, task_id):
        found = False
        for i in self.tasks:
            if i.task_id == task_id:
                found = True
                return i
        return found
    def get_tasks_by_status(self, status):
        filtered_tasks = []
        for i in self.tasks:
            if i.status == status:
                filtered_tasks.append(i)
        return filtered_tasks
    def add_new_task(self, task_id, title, description, due_date, status):
        if task_id.isdigit():
            if not self.get_task_by_id(task_id):
                if title and description:
                    if len(due_date) == 10 and due_date[:4].isdigit() and due_date[4] == "-" and due_date[7] == "-" and \
                            due_date[5:7].isdigit() and due_date[-2:].isdigit():
                        if status.lower() in self.statuses:
                            new_task = Task(task_id, title, description, due_date, status)
                            self.tasks.append(new_task)
                            print("New task added successfully.")
                        else:
                            print("Choose one of the statuses given.")
                    else:
                        print("Please enter date format correct as given.")
                else:
                    print("Please something to the title and description.")
            else:
                print("Given task ID is already in use. Please enter another ID.")
        else:
            print("Please enter task ID in numbers only.")

    def view_all_tasks(self):
        for i in self.tasks:
            print(f"{i.task_id}, {i.title}, {i.description}, {i.due_date}, {i.status}")

    def update_task_by_id(self, task_id, title, description, due_date, status):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            task.task_id = task_id
            task.title = title
            task.description = description
            task.due_date = due_date
            task.status = status
            self.tasks.append(task)
            print("Task updated.")
        else:
            print("Task not found.")

    def delete_task_by_id(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print("Task deleted")
        else:
            print("Task not found")

    def filter_tasks_by_status(self):
        pending_tasks = self.get_tasks_by_status("pending")
        in_progress_tasks = self.get_tasks_by_status("in progress")
        completed_tasks = self.get_tasks_by_status("completed")
        self.tasks.clear()
        self.tasks.extend(pending_tasks)
        self.tasks.extend(in_progress_tasks)
        self.tasks.extend(completed_tasks)
        print("Tasks filtered by status")

    def save_tasks(self):
        data = ""
        for task in self.tasks:
            data += f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}\n"
        with open("tasks.txt", "w") as f:
            f.write(data)
        print("Tasks saved")

    def load_tasks(self):
        with open("tasks.txt") as f:
            data = f.readlines()
        self.tasks.clear()
        for i in data:
            task_info = i.split(", ")
            if len(task_info) == 5:
                if task_info[0].isdigit() and len(task_info[3]) == 10 and task_info[3][:4].isdigit() and task_info[3][4] \
                        == "-" and task_info[3][7] == "-" and task_info[3][5:7].isdigit() and task_info[3][-2:].isdigit():
                    status = task_info[4]
                    if task_info[4][-1] == "\n":
                        status = task_info[4][:-1]
                    task = Task(task_info[0], task_info[1], task_info[2], task_info[3], status)
                    self.tasks.append(task)
        print("Tasks loaded")


task_manager = TaskManager()

print("""Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit""")

run = True
while run:
    try:
        option = input("\nEnter your choice: ")
        if option == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (pending/in progress/completed): ")
            task_manager.add_new_task(task_id, title, description, due_date, status)
        elif option == "2":
            task_manager.view_all_tasks()
        elif option == "3":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (pending/in progress/completed): ")
            task_manager.update_task_by_id(task_id, title, description, due_date, status)
        elif option == "4":
            task_id = input("Enter Task ID: ")
            task_manager.delete_task_by_id(task_id)
        elif option == "5":
            task_manager.filter_tasks_by_status()
        elif option == "6":
            task_manager.save_tasks()
        elif option == "7":
            task_manager.load_tasks()
        elif option == "8":
            run = False
        else:
            print("Please enter one of the options above!")
    except Exception as er:
        print(f"Error occured: {er}")