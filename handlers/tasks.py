from typing import Annotated
from fastapi import FastAPI, APIRouter, status, Depends
# from pydantic import BaseModel
from database.database import get_db_session
# from fixtures import tasks as fixtures_tasks

from dependecy import get_tasks_repository, get_tasks_cache_repository
from dependecy import get_task_service
from schema.task import TaskShema
from repository import TaskRepository, TaskCache
from service import TaskService


router = APIRouter(prefix="/task", tags=["task"])




@router.get("/all",
            response_model=list[TaskShema])
async def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)]
    ):
    return task_service.get_tasks()




@router.post("/",
            response_model=TaskShema)
async def create_fask(task: TaskShema,
                      task_repositiry: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    task_id = task_repositiry.created_task(task)
    task.id = task_id
    return task




@router.patch("/{task_id}",
              response_model=TaskShema)
async def patch_tasl(
    task_id: int, 
    name: str,
    task_repositiry: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    return task_repositiry.update_task_name(task_id, name)

    



@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    task_repositiry: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    task_repositiry.delete_task(task_id)
    return {"massege": "task deleted successfully"}

