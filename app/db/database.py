from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


"""
🟢

👉 from sqlalchemy import create_engine

Imports the function that creates a database engine.
The engine is the core connection object that SQLAlchemy uses to talk to your database (MySQL in your case).

👉 from sqlalchemy.orm import sessionmaker, declarative_base

sessionmaker → factory for creating database sessions. A session is a short‑lived object you use to query and write data.
declarative_base → generates a base class (Base) that all your ORM models will inherit from. This is how SQLAlchemy knows which classes map to tables.

👉 from app.core.config import settings

Imports your configuration object.
settings.DATABASE_URL comes from your .env file, loaded via pydantic-settings.
Keeps credentials and DB URLs out of your code.

👉 engine = create_engine(settings.DATABASE_URL, echo=True)

Creates the database engine using the connection string from .env.
echo=True → logs all SQL statements to the console (very useful while learning/debugging).
In production, you usually set echo=False to avoid noisy logs.

👉 SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Defines a session factory bound to your engine.
autocommit=False → you control when commits happen (safer).
autoflush=False → prevents automatic flushing of changes until you explicitly commit.
You’ll use SessionLocal() inside your API routes to get a session.

👉 Base = declarative_base()

Creates the base class for your ORM models.
Every model (e.g., Movie, User) will inherit from Base.
SQLAlchemy uses this to track tables and generate schema metadata.

🔴
"""
