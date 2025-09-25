inventory = {"Apple": 30, "Banana": 24, "Kiwi": 40, "Mango": 15, "Papaya": 10}


def add_item(item, quantity: int):
    item = item.capitalize()
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"Added {quantity} of {item}. New stock: {inventory[item]}")


def remove_item(item, quantity: int):
    item = item.capitalize()
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"Removed {quantity} of {item}. New stock: {inventory[item]}")
    elif item not in inventory:
        print(f"the {item} not present in inventory")
    else:
        print(f"Not enough {item} in stock. Available: {inventory[item]}")


def display_inventory():
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


add_item("Watermelon", 10)
remove_item("Papaya", 5)
display_inventory()
