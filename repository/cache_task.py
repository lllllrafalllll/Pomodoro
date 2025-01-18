from redis import Redis
import json
from schema.task import TaskShema

class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis



    def get_tasks(self) -> list[TaskShema]:
        with self.redis as redis:
            tasks_json = redis.lrange("tasks", 0, -1)
            return [TaskShema.model_validate(json.loads(task)) for task in tasks_json]



    def set_tasks(self, tasks: TaskShema):
        tasks_json = [task.json() for task in tasks]
        with self.redis as redis:
            redis.lpush("tasks", *tasks_json)

