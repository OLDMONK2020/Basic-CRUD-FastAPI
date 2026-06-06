from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.v1.movies_api import router as movies_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie API")

# Register routers
app.include_router(movies_router, prefix="/movies", tags=["Movies"])

"""
🟢

👉 from fastapi import FastAPI

Imports the FastAPI class.
This is the core object that represents your web application.
You’ll use it to define routes, middleware, and configuration.

👉 from app.db.database import Base, engine

engine → your SQLAlchemy database connection (to MySQL).
Base → the declarative base class used to define models (Movie, User, etc.).
Together, they let you manage tables and schema.

👉 from app.api.v1.movies_api import router as movies_router

Imports the router object defined in movies_api.py.
Renames it to movies_router for clarity.
This router contains all your /movies endpoints (GET, POST, PUT, DELETE).
Explicit import avoids confusion and is the current production standard.

👉 Base.metadata.create_all(bind=engine)

Tells SQLAlchemy: “Create all tables defined in my models if they don’t exist.”
If you already created the tables manually (via SQL or Alembic migrations), this line is not strictly needed.
In production, you usually remove this line and rely on Alembic migrations to manage schema changes.
You can keep it during development for quick prototyping, but don’t rely on it long‑term.

👉 app = FastAPI(title="Movie API")

Creates the FastAPI application instance.
The title is metadata shown in the auto‑generated docs (/docs).

👉 app.include_router(movies_router)

Registers your movie endpoints with the app.
This makes /movies routes available when you run the server.
You can include multiple routers (e.g., users_router, auth_router) the same way.

🔴
"""
