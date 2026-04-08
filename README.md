# GenAI Query Agent (MongoDB + Groq)

## Overview

This project is a GenAI-powered query agent that converts natural language queries into MongoDB queries, executes them, and returns user-friendly results.

It simulates a real-world ERP chatbot system where users interact with structured databases using natural language.



## Tech Stack

* Python
* FastAPI
* MongoDB
* Groq (LLaMA 3 models)



## System Workflow

User Query → LLM (Groq) → MongoDB Query → Execution → Response



##  Database Schema

Collections used:

* students
* teachers
* attendance
* assignments
* submissions
* exams

---

##  LLM Used

We use Groq (LLaMA 3 models) for:

* fast inference
* structured JSON output
* low latency

---

## Key Features

* Natural language → MongoDB query conversion
* Aggregation queries ($group, $lookup, $sort)
* Multi-collection joins
* Analytical queries (attendance %, ranking)
* Override logic for accuracy (hybrid approach)
* Error handling for invalid pipelines

---

## How to Run

### 1. Clone repo

```bash
git clone <>
cd genai-query-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add environment variable

Create `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Start MongoDB

```bash
mongod --dbpath ~/mongodb-data
```

### 5. Insert sample data

```bash
mongosh
use school
```

(Add provided dummy data)

### 6. Run server

```bash
uvicorn app:app --reload
```

### 7. Test API

Open:

```
http://127.0.0.1:8000/query?query=Show all students in class 6
```

---

## 🧪 Example Queries

### Basic

* List all students in class 6
* Show all teachers

### Filtering

* Students absent yesterday
* Assignments due this week

### Aggregation

* Count absent students today
* Assignments per class

### Multi-Collection

* Students who have not submitted assignment
* Teachers and their classes

### Analytical

* Top 5 students by attendance percentage

---

## 📊 Example Output

```json
{
  "user_query": "Count absent students today",
  "result": [
    {
      "count": 2
    }
  ]
}
```

---

## ⚠️ Challenges & Solutions

### 1. Invalid LLM Output

* Solved using JSON extraction + validation

### 2. Aggregation Errors

* Fixed using override logic

### 3. Multi-Collection Joins

* Implemented using MongoDB `$lookup`

---

## ⭐ Improvements (Optional)

* Add frontend (Streamlit / React)
* Add authentication
* Improve prompt engineering
* Add caching for performance

---

## ✅ Conclusion

This system demonstrates how LLMs can be integrated with databases to build intelligent query systems for real-world applications.

---
