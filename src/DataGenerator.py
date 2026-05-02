import json
import random

def generate_instance(num_items: int, max_capacity: int, data_file: str):
    items = []
    for i in range(num_items):
        weight = random.randint(1, 50)
        value = weight + random.randint(1, 20) 
        
        items.append({
            "id": i,
            "weight": weight,
            "value": value
        })
    
    data = {
        "sack_capacity": max_capacity,
        "items": items
    }
    
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)
