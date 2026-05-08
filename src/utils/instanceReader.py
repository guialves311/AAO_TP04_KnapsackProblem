def instance_reader(file_path):
    items = []
    capacity = 0
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        
        # 1. Ignora linhas vazias ou que indicam a fonte (ex: )
        if not line or line.startswith("["):
            continue
        
        # 2. Divide a linha por espaços
        parts = line.split()
        
        # 3. Se a linha tiver 3 colunas, é um ITEM (ID, Valor, Peso)
        if len(parts) == 3:
            items.append({
                "id": int(parts[0]),
                "value": int(parts[1]),
                "weight": int(parts[2])
            })
        
        # 4. Se a linha tiver apenas 1 número e for muito grande, é a CAPACIDADE
        # (Nas instâncias da prof, a capacidade é 10000000000)
        elif len(parts) == 1:
            val = int(parts[0])
            if val > 1000: # Diferencia o N total (1000) da Capacidade (10^10)
                capacity = val
            
    return {
        "sack_capacity": capacity,
        "items": items
    }