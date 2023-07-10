from typing import List
from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        task_counter = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {task_counter} tasks."

    def view_section(self):
        tasks_data = "\n".join([el.details() for el in self.tasks])
        return f"Section {self.name}:\n" + \
               f"{tasks_data}"
