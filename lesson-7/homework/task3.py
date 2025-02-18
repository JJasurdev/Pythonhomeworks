import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class ToDoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks[task.task_id] = task

    def view_tasks(self):
        for task in self.tasks.values():
            print(task)

    def update_task(self, task_id, **kwargs):
        if task_id in self.tasks:
            for key, value in kwargs.items():
                setattr(self.tasks[task_id], key, value)

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def filter_tasks(self, status):
        return [task for task in self.tasks.values() if task.status == status]

    def save_tasks(self):
        self.storage.save(self.tasks)

class JSONStorage:
    FILE = 'tasks.json'

    def load(self):
        try:
            with open(self.FILE, 'r') as f:
                data = json.load(f)
                return {k: Task(**v) for k, v in data.items()}
        except FileNotFoundError:
            return {}

    def save(self, tasks):
        with open(self.FILE, 'w') as f:
            json.dump({k: v.to_dict() for k, v in tasks.items()}, f)

class CSVStorage:
    FILE = 'tasks.csv'

    def load(self):
        try:
            with open(self.FILE, 'r') as f:
                reader = csv.DictReader(f)
                return {row['task_id']: Task(**row) for row in reader}
        except FileNotFoundError:
            return {}

    def save(self, tasks):
        with open(self.FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['task_id', 'title', 'description', 'due_date', 'status'])
            writer.writeheader()
            for task in tasks.values():
                writer.writerow(task.to_dict())

if __name__ == "__main__":
    storage = JSONStorage() 
    manager = ToDoManager(storage)
    
