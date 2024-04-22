"""
1. TaskManager class:

    - Attributes:
        - tasks (list of Task objects)
    - Methods:
        - add_task(task): Add a new task to the task manager.
        - get_total_tasks(): Return the total number of tasks in the task manager.
        - get_completed_tasks(): Return the number of completed tasks.
        - get_incomplete_tasks(): Return the number of incomplete tasks.
        - get_overdue_tasks(): Return the number of tasks that are overdue.
        - get_tasks_by_priority(priority): Return a list of tasks with a specific priority.
        - get_tasks_by_assignee(assignee): Return a list of tasks assigned to a specific assignee.
        - complete_task(task_id): Mark a task as completed.
        - get_task_details(task_id): Return the details of a specific task.

2. Task class:

    - Attributes:

        - task_id (integer),
        - description (string),
        - priority (string),
        - assignee (string),
        - due_date (date),
        - completed (boolean)

    - Methods: None

---

#### Your task is to implement these classes and write a program to simulate the task management system. The program
should allow the user to perform the following operations:

**Add tasks to the task manager.**

-   [ ] Retrieve and display the total number of tasks.
-   [ ] Retrieve and display the number of completed tasks. 
-   [ ] Retrieve and display the number of incomplete tasks.
-   [ ] Retrieve and display the number of tasks that are overdue.
-   [ ] Retrieve and display a list of tasks with a specific priority.
-   [ ] Retrieve and display a list of tasks assigned to a specific assignee.
-   [ ] Mark a task as completed.
-   [ ] Retrieve and display the details of a specific task.
"""
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def get_total_tasks(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return len(([tasks.task_id for tasks in self.tasks.values() if tasks.completed]))

    def get_incomplete_tasks(self):
        return len(([tasks.task_id for tasks in self.tasks.values() if not tasks.completed]))

    def get_overdue_tasks(self):
        overdue_dates = datetime.now().date()
        return sum[0]
        pass

    def get_tasks_by_priority(self, priority):
        return [task.task_id for task in self.tasks.values() if task.priority == priority]

    def get_tasks_by_assignee(self, assignee):
        return [task.task_id for task in self.tasks.values() if task.assignee == assignee]

    def complete_task(self, task_id):
        self.tasks[task_id].completed = True

    def get_task_details(self, task_id):
        task_inf = self.tasks[task_id]
        return f"task_id : {task_inf.task_id} /n" \
               f"Description :{task_inf.description}/n " \
               f"Priority : {task_inf.priority} /n" \
               f"Assignee :{task_inf.assignee} /n" \
               f"Completed :{task_inf.completed} "


class Task:
    def __init__(self, task_id, description, priority, assignee, completed):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.assignee = assignee
        # self.due_date = due_date
        self.completed = completed


if __name__ == '__main__':
    ranjan = Task(1, "code computing", "A", "ravi", "True")
    milan = Task(2, "Database", "B", "Biranwar", "False")
    obj = TaskManager()
    obj.add_task(ranjan)
    obj.add_task(milan)
    # print(obj.get_total_tasks())
    # print(obj.get_completed_tasks())
    # print(obj.get_incomplete_tasks())
    # print(obj.get_tasks_by_priority("B"))
    # print(obj.get_tasks_by_assignee("ravi"))
    # print(obj.complete_task(2000))
    print(obj.get_task_details(1))
