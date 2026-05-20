def hill_climbing(problem, initial_bits, initial_value, initial_weight):
    current_bits = list(initial_bits)
    current_value = initial_value
    current_weight = initial_weight
    
    improved = True
    while improved:
        improved = False
        
        # Explore neighbors by flipping each bit at a time
        for i in range(problem.num_items):
            neighbor = list(current_bits)
            neighbor[i] = 1 - neighbor[i] # Flip bit
            
            val = problem.calculate_value(neighbor)
            weight = problem.calculate_weight(neighbor)
            
            # Accept the neighbor if improves the value and fits capacity
            if weight <= problem.capacity and val > current_value:
                current_bits = neighbor
                current_value = val
                current_weight = weight
                improved = True
                break 
                
    return current_bits, current_value, current_weight