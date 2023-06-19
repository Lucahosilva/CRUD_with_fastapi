from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from datetime import datetime
from fastapi import HTTPException

from database.models import User
from database.connection import async_session


class UserService:
    async def create_user(name: str, phone_number: str, email: str, cpf: str):
        stmt = User(
            name=name,
            cpf=cpf,
            phone_number=phone_number,
            email=email,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        async with async_session() as session:
            session.add(stmt)
            await session.commit()

    async def delete_user(user_id: int):
        stmt = delete(User).where(User.id == user_id)
        async with async_session() as session:
            await session.execute(stmt)
            await session.commit()

    async def list_user():
        stmt = select(User)
        async with async_session() as session:
            result = await session.execute(stmt)
            return result.scalars().all()

    async def get_by_id(user_id: int):
        stmt = select(User).where(User.id == user_id)
        async with async_session() as session:
            result = await session.execute(stmt)
            response = result.scalar()
            if response is None:
                raise HTTPException(status_code=404, detail="Id not found.")
        return response

    async def alter_user(
        user_id: int, name: str, phone_number: str, email: str, cpf: str
    ):
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(
                name=name,
                cpf=cpf,
                phone_number=phone_number,
                email=email,
                updated_at=datetime.now(),
            )
        )
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
