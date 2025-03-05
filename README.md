# FastAPI Beginner Project 🚀

This is my first FastAPI project for learning and practice. It includes user authentication, database operations with SQLite, and follows an industry-standard project structure.

## 📌 Features:
- User Registration & Authentication ✅
- Password Hashing using `bcrypt` 🔐
- JWT Token-Based Authentication 🔑
- Database Integration with SQLAlchemy & SQLite 🛢️
- FastAPI's built-in interactive API docs 📄 (`/docs`)

## 📂 Project Structure:
fastapi_project/ │── app/ │ ├── api/ │ │ ├── routes/ │ │ │ ├── auth.py # Authentication routes (login, register) │ │ │ ├── users.py # User-related API routes │ │ ├── dependencies.py # Common dependencies │ ├── core/ │ │ ├── config.py # App configurations │ │ ├── security.py # JWT token and password hashing │ ├── models/ │ │ ├── user.py # SQLAlchemy User model │ ├── schemas/ │ │ ├── user.py # Pydantic User schemas │ ├── services/ │ │ ├── user_service.py # Business logic for user management │ ├── db/ │ │ ├── database.py # Database connection │ ├── main.py # FastAPI app entry point │── tests/ │ ├── test_auth.py # Authentication tests │── .env # Environment variables │── requirements.txt # Python dependencies │── README.md # Project documentation │── run.sh # Script to start the app │── .gitignore # Files to ignore in Git

