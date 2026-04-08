# schema.py

students = {
    "_id": "ObjectId",
    "name": "string",
    "class": "int",
    "section": "string"
}

teachers = {
    "_id": "ObjectId",
    "name": "string",
    "subjects": ["string"],
    "classes": ["int"]
}

attendance = {
    "_id": "ObjectId",
    "student_id": "ObjectId",
    "date": "date",
    "status": "present/absent"
}

assignments = {
    "_id": "ObjectId",
    "title": "string",
    "class": "int",
    "due_date": "date",
    "created_at": "date"
}

submissions = {
    "_id": "ObjectId",
    "assignment_id": "ObjectId",
    "student_id": "ObjectId",
    "submitted": "boolean"
}

exams = {
    "_id": "ObjectId",
    "class": "int",
    "date": "date",
    "subject": "string"
}