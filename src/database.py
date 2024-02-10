from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession #async connections
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase#sync connection
from sqlalchemy import create_engine, text, URL

from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
    
)
async_engine = create_async_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
    
)


session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    ...