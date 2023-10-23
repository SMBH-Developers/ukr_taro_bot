from ._engine import async_session
from ._models import User

from sqlalchemy.sql.expression import select, update, delete


async def registrate_if_not_exists(id_: int):
    async with async_session() as session:
        exists = (await session.execute(select(User.id).where(User.id == id_))).one_or_none()
        if exists is None:
            user = User(id=id_)
            session.add(user)
            await session.commit()


async def update_stage(id_: int, new_stage: str):
    query = update(User).where(User.id == id_).values(stage=new_stage)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()


async def delete_user(id_: int):
    query = delete(User).where(User.id == id_)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()
