** start of main.py **

def update_inventory(inventory, shipment):
    # Map to a dictionary
    inventoryMap = {}

    for items in inventory:
        inventoryMap[items[1]] = items[0]
    
    # Check and add shipment if needed
    for shipItems in shipment:
        if shipItems[1] in inventoryMap:
            inventoryMap[shipItems[1]] += shipItems[0]
        else:
            inventoryMap[shipItems[1]] = shipItems[0]

    inventory = [[value, key] for key, value in inventoryMap.items()]

    print(inventory)
    return inventory

update_inventory(
    [[2, "apples"], [5, "bananas"]], 
    [[1, "apples"], [3, "bananas"]]
)
update_inventory(
    [[2, "apples"], [5, "bananas"]], 
    [[1, "apples"], [3, "bananas"], [4, "oranges"]]
)
update_inventory(
    [], 
    [[10, "apples"], [30, "bananas"], [20, "oranges"]]
)
update_inventory(
    [[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], 
    [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]
)



** end of main.py **

