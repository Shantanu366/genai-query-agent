import json
from db import *

def override_query(user_query):
    query = user_query.lower()

    # Count absent today
    if "count" in query and "absent" in query and "today" in query:
        return {
            "collection": "attendance",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$match": {
                        "status": "absent",
                        "date": "2026-04-08"
                    }
                },
                {
                    "$group": {
                        "_id": None,
                        "count": { "$sum": 1 }
                    }
                }
            ]
        }

    # assignments per class
    if "assignments" in query and "per class" in query:
        return {
            "collection": "submissions",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$lookup": {
                        "from": "assignments",
                        "localField": "assignment_id",
                        "foreignField": "_id",
                        "as": "assignment"
                    }
                },
                {"$unwind": "$assignment"},
                {
                    "$group": {
                        "_id": "$assignment.class",
                        "total_submissions": { "$sum": 1 }
                    }
                }
            ]
        }

    # highest absentees
    if "highest" in query and "absent" in query:
        return {
            "collection": "attendance",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$match": {
                        "status": "absent",
                        "date": "2026-04-08"
                    }
                },
                {
                    "$lookup": {
                        "from": "students",
                        "localField": "student_id",
                        "foreignField": "_id",
                        "as": "student"
                    }
                },
                {"$unwind": "$student"},
                {
                    "$group": {
                        "_id": "$student.class",
                        "absent_count": { "$sum": 1 }
                    }
                },
                {"$sort": { "absent_count": -1 }},
                {"$limit": 1}
            ]
        }
    if "not submitted" in query:
        return {
            "collection": "students",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$lookup": {
                        "from": "submissions",
                        "localField": "_id",
                        "foreignField": "student_id",
                        "as": "submissions"
                    }
                },
                {
                    "$match": {
                        "submissions.submitted": False
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "name": 1,
                        "class": 1
                    }
                }
            ]
        }

    
    if "teachers" in query and "classes" in query:
        return {
            "collection": "teachers",
            "operation": "find",
            "filter": {}
        }

 
    if "attendance percentage" in query:
        return {
            "collection": "attendance",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$group": {
                        "_id": "$student_id",
                        "total_days": { "$sum": 1 },
                        "present_days": {
                            "$sum": {
                                "$cond": [
                                    { "$eq": ["$status", "present"] },
                                    1,
                                    0
                                ]
                            }
                        }
                    }
                },
                {
                    "$lookup": {
                        "from": "students",
                        "localField": "_id",
                        "foreignField": "_id",
                        "as": "student"
                    }
                },
                {"$unwind": "$student"},
                {
                    "$project": {
                        "_id": 0,
                        "name": "$student.name",
                        "attendance_percentage": {
                            "$multiply": [
                                { "$divide": ["$present_days", "$total_days"] },
                                100
                            ]
                        }
                    }
                }
            ]
        }
    if "top" in query and "attendance" in query:
        return {
            "collection": "attendance",
            "operation": "aggregate",
            "pipeline": [
                {
                    "$group": {
                        "_id": "$student_id",
                        "total_days": { "$sum": 1 },
                        "present_days": {
                            "$sum": {
                                "$cond": [
                                    { "$eq": ["$status", "present"] },
                                    1,
                                    0
                                ]
                            }
                        }
                    }
                },
                {
                    "$lookup": {
                        "from": "students",
                        "localField": "_id",
                        "foreignField": "_id",
                        "as": "student"
                    }
                },
                { "$unwind": "$student" },
                {
                    "$project": {
                        "_id": 0,
                        "name": "$student.name",
                        "attendance_percentage": {
                            "$multiply": [
                                { "$divide": ["$present_days", "$total_days"] },
                                100
                            ]
                        }
                    }
                },
                {
                    "$sort": { "attendance_percentage": -1 }
                },
                {
                    "$limit": 5
                }
            ]
        }

    return None


def execute_query(query_json):
    query = json.loads(query_json)

    collection_name = query["collection"]
    operation = query["operation"]

    collection = globals()[collection_name]

    if operation == "find":
        return list(collection.find(query.get("filter", {})))

    elif operation == "aggregate":
        try:
            result = list(collection.aggregate(query.get("pipeline", [])))
            return result
        except Exception as e:
            return {
                "error": "Aggregation failed",
                "details": str(e),
                "pipeline": query.get("pipeline")
            }

    elif operation == "count":
        return collection.count_documents(query.get("filter", {}))
    
    return {"error": "Unsupported operation"}