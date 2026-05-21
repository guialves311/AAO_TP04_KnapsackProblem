from algorithms.classes.KnapsackProblem import KnapsackProblem

def hill_climbing(problem: KnapsackProblem, initial_bits: list, initial_value: int, initial_weight: int):
    """Solves the 0/1 Knapsack Problem using Hill Climbing.
    
    A local search algorithm that iteratively explores neighboring solutions by 
    flipping one bit at a time, accepting only improvements until a local optimum 
    is reached.

    Args:
        problem (KnapsackProblem): The knapsack problem instance containing items,
                                   weights, values, and capacity
        initial_bits (list): Initial binary solution
        initial_value (int): Value of the initial solution
        initial_weight (int): Weight of the initial solution

    Returns:
        tuple: A tuple containing:
            - current_bits (list): Binary solution at local optimum
            - current_value (int): Value of the local optimum
            - current_weight (int): Weight of the local optimum solution
    """
    
    # Create a new list in order to not alter the original list
    current_bits = list(initial_bits)
    
    # Inserts the initial solution value and weight
    current_value = initial_value
    current_weight = initial_weight
    
    # To track if an improvement was made in the current iteration
    improved = True
    # Continue searching until no improvement is found
    while improved:
        improved = False
        
        # Explore neighbors by flipping each bit at a time
        for i in range(problem.num_items):
            # Create a neighbor solution by flipping the 0/1 bit at position i  
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