def hill_climbing(problem, initial_bits):
    current_bits = list(initial_bits)
    current_value = problem.calculate_value(current_bits)
    
    improved = True
    while improved:
        improved = False
        for i in range(problem.num_items):
            neighbor = list(current_bits)
            neighbor[i] = 1 - neighbor[i]
            
            val = problem.calculate_value(neighbor)
            weight = problem.calculate_weight(neighbor)
            
            if weight <= problem.capacity and val > current_value:
                current_bits = neighbor
                current_value = val
                improved = True
                break 
                
    return current_bits