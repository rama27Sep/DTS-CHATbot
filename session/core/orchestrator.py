from core.intent_detector import detect_intent
from core.response_builder import build_response
from memory.session import SessionManager

session_manager = SessionManager()

def handle_message(message: str) -> str:
    session_manager.store(message)
    intent, entities = detect_intent(message)
    response = build_response(intent, entities)
    return response
