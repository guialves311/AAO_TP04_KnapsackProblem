from algorithms.classes.KnapsackProblem import KnapsackProblem

def greedy(problem: KnapsackProblem):
    # Sort items by descending order of value to weight
    indices_sorted = sorted(range(problem.num_items), 
                            key=lambda i: problem.values[i] / problem.weights[i], 
                            reverse=True)
    
    total_value = 0
    total_weight = 0
    solution_bits = [0] * problem.num_items 
    
    # Try to add items in sorted order if they fit
    for i in indices_sorted:
        if total_weight + problem.weights[i] <= problem.capacity:
            solution_bits[i] = 1
            total_value += problem.values[i]
            total_weight += problem.weights[i]
        
    return solution_bits, total_value