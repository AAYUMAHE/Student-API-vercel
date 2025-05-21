from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load data.json
with open(os.path.join(os.path.dirname(__file__), '..', 'data.json')) as f:
    students = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = []):
    name_to_marks = {s["name"]: s["marks"] for s in students}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
