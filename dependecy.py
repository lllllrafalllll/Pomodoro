from fastapi import Depends

from repository import TaskRepository, TaskCache
from database import get_db_session
from cache import get_redis_connecton
from service import TaskService


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)



def get_tasks_cache_repository() -> TaskCache:
    redis_connecton = get_redis_connecton()
    return TaskCache(redis_connecton)



def get_task_service(
        task_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: TaskCache = Depends(get_tasks_cache_repository)
) -> TaskService:
    return TaskService (
        task_repository=task_repository,
        task_cache=task_cache
        )