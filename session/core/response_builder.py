from api.api_client import get_weather;
import sqlite3;


import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "dts.db")

def build_response(intent: str, entities: dict) -> str:
    if intent == "GREETING":
        return "Hello! How can I help you?"

    if intent == "GET_WEATHER":
        data = get_weather()
        temp = data["current_weather"]["temperature"]
        return f"The current temperature is {temp}°C"

    if intent == "WHAT_IS_DTS":
        return "DTS stands for Digital Tool System."

    return "Sorry, I didn't understand that."
import sqlite3

DB_PATH = "db/dts.db"

def fetch_answer_from_db(intent: str) -> str | None:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
        SELECT answer
        FROM faq
        WHERE intent = ?
        LIMIT 1
    """

    cursor.execute(query, (intent,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None
