from models import Task
from db_setup import AsyncSessionLocal
from sqlalchemy import select

async def create_task(description, deadline, roles):
    async with AsyncSessionLocal() as session:
        task = Task(description=description, deadline=deadline, roles=",".join(roles))
        session.add(task)
        await session.commit()
        return task.id

async def list_tasks():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Task).order_by(Task.deadline))
        return result.scalars().all()
