def instance_reader(file_path):
    items = []
    
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("[")]

    if not lines:
        return {"sack_capacity": 0, "items": []}

    # 1. LER O NÚMERO DE ITENS (Sempre a primeira linha útil)
    try:
        num_items_header = int(lines[0])
    except ValueError:
        num_items_header = 0

    # 2. LER A CAPACIDADE (Sempre a última linha útil)
    try:
        capacity = int(lines[-1])
    except ValueError:
        capacity = 0

    # 3. LER OS ITENS
    for line in lines:
        parts = line.split()
        if len(parts) == 3:
            items.append({
                "id": int(parts[0]),
                "value": int(parts[1]),
                "weight": int(parts[2])
            })
            
    return {
        "sack_capacity": capacity,
        "items": items
    }