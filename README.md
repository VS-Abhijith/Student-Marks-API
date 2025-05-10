# 🧪 Student Marks API – Built with FastAPI

This is a simple and fast API built using **FastAPI** that helps retrieve marks of students by their names. It reads the data from a local JSON file and supports fetching data for multiple students at once. This project is perfect for small web apps, school tools, or learning how APIs work.

---

## 📌 What This Project Does

- Reads student marks from a JSON file.
- Exposes a REST API to get marks based on student names.
- Allows querying **one or more names** at a time.
- Supports frontend apps with **CORS enabled** (Cross-Origin access).

---

## 🧠 How It Works

### 📁 Data Source: `q-vercel-python.json`

Example data in the JSON file:
```json

  {"name":"4","marks":32},{"name":"z3e7J3kd","marks":6},{"name":"Lvhiq8l5kx","marks":50},{"name":"Tf3lZ0Wpf","marks":44},
  {"name":"HHxcdmfu","marks":48},{"name":"SQ","marks":44},{"name":"FYS","marks":13},{"name":"3g","marks":85},
  {"name":"prJ1","marks":35},{"name":"z6t","marks":70},{"name":"M","marks":42},{"name":"H","marks":64},
  {"name":"enw9xo","marks":45},{"name":"ztjaio","marks":62},{"name":"g0bx","marks":76},{"name":"hXvfzH","marks":87},
  {"name":"9","marks":61},{"name":"ppIjO","marks":64},{"name":"wvHvc3B0s","marks":79},{"name":"wHR5dyKyzu","marks":31},
```

This JSON holds names and corresponding marks.

---

### 🧩 Code Overview: `app.py`

| Section | Purpose |
|--------|---------|
| `FastAPI()` | Creates the web app |
| `CORSMiddleware` | Allows frontend apps to fetch data |
| `json.load()` | Loads data from the JSON file |
| `@app.get("/api")` | Defines an API endpoint to get student marks |
| Logic inside `/api` | Splits comma-separated names, checks data, and returns marks or `null` |

#### 🧪 Example Usage:
Request:
```
GET /api?name=Alice,Bob
```

Response:
```json
{
  "marks": [95, 88]
}
```

If a name is not found:
```
GET /api?name=Alice,UnknownName
```

Response:
```json
{
  "marks": [95, null]
}
```

---

## 🚀 Running This Project Locally

### ✅ Requirements
- Python 3.8 or higher
- FastAPI
- Uvicorn (ASGI server)

### 📦 Installation
```bash
pip install fastapi uvicorn
```

### ▶ Start the Server
```bash
uvicorn app:app --reload
```

Now open this URL in your browser or API tool like Postman:
```
http://127.0.0.1:8000/api?name=Alice,Bob
```

---

## 🌐 Deploying Online (e.g., Vercel)

- Works well with serverless platforms like Vercel.
- Add a `vercel.json` file if needed.
- Entry point (`app.py`) should be ASGI-compatible.

---

## 📁 Folder Structure

```
📦 student-marks-api/
 ┣ 📄 app.py                  # Main FastAPI app
 ┣ 📄 q-vercel-python.json    # Student data file
 ┗ 📄 README.md               # Project documentation
```

---

## 🔧 Future Improvements (Optional Ideas)

- Add a POST route to insert or update marks
- Store data in a real database (e.g., MongoDB)
- Build a frontend using React or plain HTML/JS
- Add authentication to protect API access

---

## 🙌 Contributing

Feel free to fork, improve, and create pull requests. All contributions are welcome!

---

## 📄 License

This project is open source and free to use under the **MIT License**.
```

---
