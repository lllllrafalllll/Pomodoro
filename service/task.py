from repository import TaskRepository, TaskCache
from schema.task import TaskShema
from dataclasses import dataclass



@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache


    def get_tasks(self):
        if cache_task := self.task_cache.get_tasks():
            return cache_task
        else:
            tasks = self.task_repositiry.get_tasks()
            tasks_schema = [TaskShema.model_validate(task) for task in tasks]
            self.task_cache.set_tasks(tasks_schema)
            return tasks_schema
