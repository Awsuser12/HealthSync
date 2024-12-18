from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from psycopg2 import OperationalError

# Replace these with your Redshift credentials
REDSHIFT_HOST = "healthsync-metrics.c9oyzhxa9puz.eu-north-1.redshift.amazonaws.com"
REDSHIFT_PORT = "5439"
REDSHIFT_USER = "awsuser"
REDSHIFT_PASSWORD = "Admin$100"
REDSHIFT_DB = "dev"

SYNC_DATABASE_URL = (
    f"redshift+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}"
)
ASYNC_DATABASE_URL = (
    f"redshift+asyncpg://{REDSHIFT_USER}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}"
)

# Sync Engine for initial operations
sync_engine = create_engine(SYNC_DATABASE_URL, echo=True)

try:
    with sync_engine.connect() as conn:
        # Replace with Redshift-compatible statements
        conn.execute(text("SELECT 1"))
        print("Connected to Redshift successfully!")
except OperationalError as e:
    print(f"Error connecting to Redshift: {e}")

# Async Engine for asynchronous queries
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,
    pool_size=100,
    max_overflow=100,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()
