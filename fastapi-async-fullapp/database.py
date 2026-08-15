import os
# We import the async versions from sqlalchemy.ext.asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Update the URL scheme to use postgresql+asyncpg:// instead Of pOstgresql://
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://postgres:1@localhost/postgres"
)

# 2. Create the engine using create_async_engine
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)

# 3. session factory now using async sessionmaker with AsyncSession
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    class_=AsyncSession
)

Base = declarative_base()

# 4. Convert the dependency to an async generator using 'async with'
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            # We must await the closing of the connection
            await db.close()