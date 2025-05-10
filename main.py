from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data from q-vercel-python.json
with open("q-vercel-python.json", "r") as file:
    students_data = json.load(file)

@app.get("/api")
async def get_marks(name: str):
    names = name.split(",")
    marks = []
    for n in names:
        if n in students_data["students"]:
            marks.append(students_data["students"][n])
        else:
            marks.append(None)  # or any default value you prefer
    return {"marks": marks}
