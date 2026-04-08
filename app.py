# app.py

import json
from fastapi import FastAPI
from llm import generate_mongo_query
from query_engine import execute_query

app = FastAPI()

@app.get("/query")
def ask(query: str):
    from query_engine import override_query

    override = override_query(query)

    if override:
        result = execute_query(json.dumps(override))
        mongo_query = override
    else:
        mongo_query = generate_mongo_query(query)
        result = execute_query(mongo_query)

    return {
        "user_query": query,
        "mongo_query": mongo_query,
        "result": result
    }