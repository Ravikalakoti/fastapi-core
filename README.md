# FastAPI Beginner Project 

This is my first FastAPI project for learning and practice. It includes user authentication, database operations with SQLite, and follows an industry-standard project structure.

## 📌 Features:
- User Registration & Authentication ✅
- Password Hashing using `bcrypt` 🔐
- JWT Token-Based Authentication 🔑
- Database Integration with SQLAlchemy & SQLite 🛢️
- FastAPI's built-in interactive API docs 📄 (`/docs`)


## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/Ravikalakoti/fastapi-beginner-project.git
cd fastapi-project

### 2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Set Up Environment Variables
Create a .env file in the root directory and add the following:

SECRET_KEY="your_secret_key_here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

DATABASE_URL="sqlite:///./app.db"

### 5️⃣ Run Database Migrations (if using SQLAlchemy)
alembic upgrade head

### 6️⃣ Run the FastAPI Application
uvicorn app.main:app --reload

Your API will be available at http://127.0.0.1:8000
API documentation can be accessed at:
Swagger UI: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc


