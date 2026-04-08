# GenAI Query Agent (MongoDB + Groq)

## Overview

This project is a **GenAI-powered query agent** that converts natural language questions into MongoDB queries, executes them, and returns user-friendly responses.

It simulates a real-world ERP chatbot system where users can query structured databases using natural language.

---

## System Workflow

User Query
⬇
LLM (Groq) → MongoDB Query Generation
⬇
Query Execution (MongoDB)
⬇
Result Processing
⬇
API Response

---

## Tech Stack

* **Backend:** Python, FastAPI
* **Database:** MongoDB
* **LLM:** Groq (LLaMA 3 models)
* **Libraries:** pymongo, python-dotenv

---

## Database Schema

Collections used:

* **students** → student details
* **teachers** → teacher info + classes
* **attendance** → daily attendance
* **assignments** → assignment details
* **submissions** → assignment submissions
* **exams** → exam schedule

---

## LLM Integration (Groq)

We use Groq for:

* Fast inference
* Low cost
* Structured JSON output

Model used:

```
llama-3.3-70b-versatile
```

---

##  Key Features

###  Natural Language → MongoDB Query

* Converts user queries into valid MongoDB queries dynamically

###  Aggregation Queries

* Supports `$group`, `$sort`, `$limit`, `$match`

###  Multi-Collection Queries

* Uses `$lookup` for joins

###  Analytical Queries

* Attendance percentage calculation
* Ranking (Top students)

### Hybrid Architecture

* LLM + Rule-based overrides
* Ensures accuracy for complex queries

### Error Handling

* Handles invalid JSON / pipelines gracefully

---

##  How to Run

### 1. Clone repository

```bash
git clone https://github.com/Shantanu366/genai-query-agent.git
cd genai-query-agent
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup environment variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4. Start MongoDB

```bash
mongod --dbpath ~/mongodb-data
```

---

### 5. Insert sample data

```bash
mongosh
use school
```

(Add dummy data provided in project)

---

### 6. Run FastAPI server

```bash
uvicorn app:app --reload
```

---

### 7. Test API

Open in browser:

```
http://127.0.0.1:8000/query?query=Show all students in class 6
```

---

##  Supported Queries

###  Level 1 – Basic

* List students in a class
* Show attendance of a student
* List teachers
* Assignments created today

---

###  Level 2 – Filtering

* Students absent yesterday
* Assignments due this week
* Section-wise filtering
* Exams this month

---

###  Level 3 – Aggregation

* Count absent students
* Assignments per class
* Class with highest absentees

---

###  Level 4 – Multi-Collection

* Students who have not submitted assignments
* Teachers and their classes
* Attendance percentage per student

---

###  Level 5 – Analytical

* Top 5 students with highest attendance

---

## Example Query & Output

### Query:

```
Show students who were absent today
```

### Output:

```json
{
  "result": [
    { "name": "Bob" },
    { "name": "Charlie" }
  ]
}
```

---

## Challenges & Solutions

### 1. Invalid LLM JSON Output

* Solved using JSON extraction and validation

### 2. Incorrect Aggregation Pipelines

* Fixed using rule-based overrides

### 3. Multi-Collection Joins

* Implemented using MongoDB `$lookup`

---

## Improvements (Optional)

* Add UI (Streamlit / React)
* Add authentication & security layer
* Improve prompt engineering
* Add caching for performance

---

## Conclusion

This project demonstrates how LLMs can be integrated with databases to build intelligent, production-ready query systems.

---

## Author

Shantanu Rao
