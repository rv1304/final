from models import inventory

def sync_inventory(new_data):
    for item in new_data:
        for inv in inventory:
            if inv["id"] == item["id"]:
                inv["quantity"] = item["quantity"]
    return {"message": "Inventory synced successfully!", "inventory": inventory}
