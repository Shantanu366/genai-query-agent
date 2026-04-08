from dotenv import load_dotenv
from groq import Groq
import re
import os
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"),)
def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group(0) if match else None
def generate_mongo_query(user_query):
    prompt = f"""
    STRICT JSON ONLY.

    Rules:
    - Use MongoDB aggregation when needed
    - Each stage must be separate
    - Allowed stages: $match, $group, $lookup, $project, $sort, $limit
    - NEVER nest stages inside each other

    Aggregation examples:

    Count:
    [
    {{ "$match": {{ "status": "absent" }} }},
    {{ "$group": {{ "_id": null, "count": {{ "$sum": 1 }} }} }}
    ]

    Group:
    [
    {{ "$group": {{ "_id": "$class", "count": {{ "$sum": 1 }} }} }}
    ]

    Top:
    [
    {{ "$group": {{ "_id": "$class", "count": {{ "$sum": 1 }} }} }},
    {{ "$sort": {{ "count": -1 }} }},
    {{ "$limit": 1 }}
    ]

    Schema:
    {{
    "collection": string,
    "operation": "find" | "aggregate" | "count",
    "filter": object,
    "pipeline": array
    }}

    Query: {user_query}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  
        messages=[
            {"role": "system", "content": "You generate MongoDB queries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
)

    raw = response.choices[0].message.content.strip()

    json_text = extract_json(raw)

    if not json_text:
        raise ValueError(f"Invalid LLM output: {raw}")

    return json_text