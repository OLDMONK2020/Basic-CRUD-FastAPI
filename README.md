# Basic-CRUD-FastAPI
# Commands

# pip list
-> to display all the Python packages currently installed in your environment (both system-wide and virtual environment-specific), along with their versions.

# mkdir Basic-CRUD-FastAPI
# cd Basic-CRUD-FastAPI
-> Create the project folder named 'Basic-CRUD-FastAPI'

# python -m venv venv
-> Create a virtual environment

# venv\Scripts\activate.bat
-> Activate the virtual environment (Windows)

# pip install fastapi uvicorn
-> Install FastAPI and a server (like Uvicorn)

# uvicorn main:app --reload
-> To start your FastAPI application with Uvicorn

# uvicorn main:app --reload --port 8080
->To specify a port:

🔑 Explanation
main → the filename of your Python script (main.py).

app → the FastAPI instance inside that file (app = FastAPI()).

--reload → enables auto-reload, so the server restarts whenever you change your code (great for development).

immediately after running this command  folder (__pycache__) and the file inside (main.cpython-313.pyc) gets created. When Python runs a .py file, it compiles the source code into bytecode. That bytecode is stored in the __pycache__ folder as .pyc files. 
Add __pycache__/ to your .gitignore so they don’t get pushed to GitHub.
They’ll be regenerated automatically whenever you run your app.

# ------------------------------------------------------
# When we run 'python -m venv venv' to create the Virtual environment, a folder named 'venv' gets created with few folders & files. Here are the details ->

🗂️ Key Virtual Environment Folders
🔹 Scripts/
    Holds the activation scripts and executables.

    Use this to activate your environment (venv\Scripts\activate) and run the isolated python.exe and pip.exe.

🔹 Lib/site-packages/
    Contains all the third‑party libraries you install (FastAPI, Uvicorn, etc.).

    This is the “toolbox” of your project — if you delete it, you lose your installed packages.

🔹 pyvenv.cfg
    A small config file at the root.

    Records which Python version created the environment and links it to your base installation.

# Why activated (venv) is not showing after running 'venv\Scripts\activate.bat' command?
The .bat script is designed for Command Prompt (CMD), not PowerShell. In CMD, you would immediately see your prompt change to something like: 
(venv) C:\Users\duovi\OneDrive\Documents\Ankur\Study\FastAPI\Basic-CRUD-FastAPI>

But In PowerShell, the correct activation script is:
venv\Scripts\Activate.ps1
    
    ✅ How to Confirm It’s Active ->
    run 'Get-Command python'  (in powershell)
    If it points to your venv\Scripts\python.exe, then the virtual environment is active.


#---------------------------------------------------------------------------------


## 🏗️ Production‑Grade FastAPI Folder Structure

```text
BASIC-CRUD-FASTAPI/
│
├── app/                            # Main application package
│   ├── __init__.py
│   ├── main.py                     # FastAPI app instance and startup logic
│   │
│   ├── api/                        # Routers grouped by feature
│   │   ├── __init__.py
│   │   ├── v1/                     # Versioned API routes
│   │   │   ├── __init__.py
│   │   │   ├── movies.py
│   │   │   ├── users.py
│   │   │   └── auth.py
│   │   └── dependencies.py         # Common dependencies (auth, DB session)
│   │
│   ├── core/                       # Core configuration and startup
│   │   ├── __init__.py
│   │   ├── config.py               # Settings, environment variables
│   │   ├── logging_config.py       # Logging setup
│   │   └── security.py             # JWT, password hashing, etc.
│   │
│   ├── models/                     # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── movie.py
│   │   └── user.py
│   │
│   ├── schemas/                    # Pydantic models for request/response
│   │   ├── __init__.py
│   │   ├── movie_schema.py
│   │   └── user_schema.py
│   │
│   ├── repositories/               # Database access layer
│   │   ├── __init__.py
│   │   ├── movie_repository.py
│   │   └── user_repository.py
│   │
│   ├── services/                   # Business logic layer
│   │   ├── __init__.py
│   │   ├── movie_service.py
│   │   └── user_service.py
│   │
│   ├── db/                         # Database connection and session
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── utils/                      # Helper functions (pagination, validation)
│   │   ├── __init__.py
│   │   └── helpers.py
│   │
│   └── tests/                      # Unit and integration tests
│       ├── __init__.py
│       ├── test_movies.py
│       └── test_users.py
│
├── .env                            # Environment variables
├── .gitignore
├── requirements.txt                # Dependencies
├── README.md
└── run.py                          # Entry point for running the app
