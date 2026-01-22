from core.orchestrator import handle_message

def main():
    print("🤖 Chatbot started. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting chatbot. Goodbye!")
            break
        
        response = handle_message(user_input)
        print(f"Bot: {response}\n")



    import re
from inventory import add_item, get_item, get_all

print("🤖 Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        print("Exiting chatbot. Goodbye!")
        break

    if user_input in ["hi", "hello"]:
        print("Bot: Hello! How can I help you?")
        continue

    # ---- GIVE ME 5 HAMMERS ----
    match = re.search(r"give me (\d+) (\w+)", user_input)
    if match:
        qty = int(match.group(1))
        item = match.group(2)
        result = add_item(item, qty)
        print("Bot:", result)
        continue

    # ---- HOW MANY HAMMERS ----
    match = re.search(r"how many (\w+)", user_input)
    if match:
        item = match.group(1)
        count = get_item(item)
        print(f"Bot: You have {count} {item}(s).")
        continue

    # ---- SHOW INVENTORY ----
    if "inventory" in user_input or "stock" in user_input:
        print("Bot:\n" + get_all())
        continue

    print("Bot: Sorry, I didn't understand that.")
    
if __name__ == "__main__":
    main()