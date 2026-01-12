inventory = {}

def add_item(item, qty):
    if item not in inventory:
        inventory[item] = 0
    inventory[item] += qty
    return f"Added {qty} {item}(s)."

def get_item(item):
    return inventory.get(item, 0)

def get_all():
    if not inventory:
        return "Inventory is empty."
    return "\n".join([f"{k}: {v}" for k, v in inventory.items()])
