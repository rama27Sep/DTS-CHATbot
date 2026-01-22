def detect_intent(message: str):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "GREETING", {}

    if "what is dts?" in message:
        return "WHAT_IS_DTSS", {}
    
    if "placing order" in message:
        return "GET_ORDER",{}
    
    if "news" in message:
        return "GET_NEWS",{}


    return "UNKNOWN", {}
