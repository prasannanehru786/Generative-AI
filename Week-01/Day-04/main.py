from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Student FastAPI Assignment",
    description="Gen AI Architect Program - Assignment 4",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI Application",
        "timestamp": datetime.now()
    }


@app.get("/greet/{name}")
def greet(name: str):
    return {
        "name": name,
        "message": f"Hello {name}!"
    }


@app.get("/marks/{score}")
def grade(score: int):
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "Fail"

    return {
        "score": score,
        "grade": grade
    }