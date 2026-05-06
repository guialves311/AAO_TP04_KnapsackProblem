def calculate_value(solution_bits, all_items):
    return sum(item['value'] for i, item in enumerate(all_items) if solution_bits[i] == 1)

def calculate_weight(solution_bits, all_items):
    return sum(item['weight'] for i, item in enumerate(all_items) if solution_bits[i] == 1)

def hill_climbing(all_items, capacity, initial_bits):
    current_bits = list(initial_bits)
    current_value = calculate_value(current_bits, all_items)
    
    improved = True
    while improved:
        improved = False
        
        for i in range(len(all_items)):
            neighbor = list(current_bits)
            neighbor[i] = 1 - neighbor[i]
            
            val = calculate_value(neighbor, all_items)
            weight = calculate_weight(neighbor, all_items)
            
            if weight <= capacity and val > current_value:
                current_bits = neighbor
                current_value = val
                improved = True
                break 
                
    return current_bits