from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine("postgresql+asyncpg://lucas:@localhost:5432/fastapi")
async_session = sessionmaker(engine, class_=AsyncSession)
