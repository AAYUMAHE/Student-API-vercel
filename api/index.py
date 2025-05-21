from fastapi import FastAPI, Query
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
data_path = os.path.join(os.path.dirname(__file__), '..', 'data.json')
with open(data_path) as f:
    students = json.load(f)

@app.get("/api")
def get_marks(name: List[str] = Query(default=[])):
    name_to_marks = {s["name"]: s["marks"] for s in students}
    result = [name_to_marks.get(n, None) for n in name]
    return {"marks": result}
