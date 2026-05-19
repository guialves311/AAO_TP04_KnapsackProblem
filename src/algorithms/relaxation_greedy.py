def relaxation_greedy(problem):
    indices_sorted = sorted(range(problem.num_items), 
                            key=lambda i: problem.values[i] / problem.weights[i], 
                            reverse=True)
    
    capacity_left = problem.capacity
    total_relaxed_value = 0.0
    x = [0.0] * problem.num_items
    
    for i in indices_sorted:
        if problem.weights[i] <= capacity_left:
            x[i] = 1.0
            capacity_left -= problem.weights[i]
            total_relaxed_value += problem.values[i]
        else:
            x[i] = capacity_left / problem.weights[i]
            total_relaxed_value += problem.values[i] * x[i]
            capacity_left = 0
            break
        
    return x, total_relaxed_value


def enhanced_greedy(problem, x_fractions):
    indices_sorted = sorted(range(problem.num_items), 
                            key=lambda i: problem.values[i] / problem.weights[i], 
                            reverse=True)
    
    capacity_left = problem.capacity
    total_value = 0
    total_weight = 0
    solution_bits = [0] * problem.num_items
    
    for i in indices_sorted:
        if x_fractions[i] > 0.0 and problem.weights[i] <= capacity_left:
            solution_bits[i] = 1
            capacity_left -= problem.weights[i]
            total_value += problem.values[i]
            total_weight += problem.weights[i]
            
    return solution_bits, total_value, total_weight