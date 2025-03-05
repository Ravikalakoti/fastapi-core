from fastapi import FastAPI
from app.api.routes import users, auth
from app.db.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def home():
    return {"message": "FastAPI Industry-Standard Project"}
