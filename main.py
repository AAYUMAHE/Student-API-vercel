from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the JSON data once when app starts
with open("data.json", "r") as f:
    students = json.load(f)

# Create a dict for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in students}

@app.get("/api")
def get_marks(name: List[str] = []):
    return {"marks": [marks_dict.get(n, -1) for n in name]}
