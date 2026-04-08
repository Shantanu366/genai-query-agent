from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]

students = db["students"]
teachers = db["teachers"]
attendance = db["attendance"]
assignments = db["assignments"]
submissions = db["submissions"]
exams = db["exams"]