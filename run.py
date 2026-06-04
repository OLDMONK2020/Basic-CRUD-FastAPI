import uvicorn
from app.main import app

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


""" 
🟢

👉 import uvicorn → brings in Uvicorn, the ASGI server that actually runs your FastAPI app.

👉 from app.main import app → imports the FastAPI instance (app = FastAPI()) defined in app/main.py. This is the object Uvicorn needs to serve.

👉 if __name__ == "__main__":

    This block ensures the code only runs when you execute python run.py directly.
    If another script imports run.py, this part won’t execute (avoids accidental server starts).

👉 uvicorn.run("app.main:app", ...)

    "app.main:app" is a module path string:
    app.main → the Python module (app/main.py).
    app → the FastAPI instance inside that file.

    Uvicorn uses this string to locate and serve your application.
    host="0.0.0.0"

    Binds the server to all network interfaces.
    This makes your app accessible not just locally (localhost), but also from other devices on the same network (useful in Docker or cloud).

    port=8000
    The port number your app listens on.

    You’ll access it at http://localhost:8000

    reload=True
    Enables auto‑reload during development.
    Every time you change code, Uvicorn restarts automatically.
    In production, you’ll set this to False for performance and stability.

👉  In Short: run.py is your entry point. 
    It tells Uvicorn: “Run the FastAPI app defined in app/main.py on port 8000, reload on changes.”
    This keeps your project clean: main.py only defines the app, while run.py handles how it’s launched.

🔴
"""
