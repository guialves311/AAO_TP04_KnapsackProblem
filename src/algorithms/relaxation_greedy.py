from algorithms.classes.KnapsackProblem import KnapsackProblem

def relaxation_greedy(problem: KnapsackProblem):
    """Solves the fractional relaxation of the 0/1 Knapsack Problem.
    
    Selects items in descending order of their value-to-weight ratio, 
    allowing fractional items to be included in the knapsack.
    
    Args:
        problem (KnapsackProblem): The knapsack problem instance containing items,
                                   weights, values, and capacity.
    
    Returns:
        tuple: A tuple containing:
            - x (list): Fractional array where values range from 0.0 to 1.0
            - total_relaxed_value (float): Total value of items (including fractions)
    """
    
    # Sort items by descending order value to weight
    indices_sorted = sorted(range(problem.num_items), 
                            key=lambda i: problem.values[i] / problem.weights[i], 
                            reverse=True)
    
    # Insert the problem's initial capacity
    capacity_left = problem.capacity
    total_relaxed_value = 0.0
    
    # Initialize the solution array
    x = [0.0] * problem.num_items
    
    # Try to add items in sorted order, adding fractions if they don't fit
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


def enhanced_greedy(problem: KnapsackProblem, x_fractions: list):
    """Constructs an integer solution from fractional relaxation results.
    
    Uses the fractional solution from relaxation_greedy to guide selection of 
    items in descending order of value-to-weight ratio, prioritizing items 
    that were included in the relaxed solution.
    
    Args:
        problem (KnapsackProblem): The knapsack problem instance
        x_fractions (list): Fractional values from relaxation_greedy indicating
                           which items should be prioritized
    
    Returns:
        tuple: A tuple containing:
            - solution_bits (list): Binary array where 1 indicates item is included
            - total_value (int): Total value of items in the knapsack
            - total_weight (int): Total weight of items in the knapsack
    """
    
    # Sort items by descending order of value to weight
    indices_sorted = sorted(range(problem.num_items), 
                            key=lambda i: problem.values[i] / problem.weights[i], 
                            reverse=True)
    
    capacity_left = problem.capacity
    total_value = 0
    total_weight = 0
    solution_bits = [0] * problem.num_items
    
    # Try to add items in sorted order 
    # If they were in the relaxed solution and fit in the remaining capacity
    for i in indices_sorted:
        if x_fractions[i] > 0.0 and problem.weights[i] <= capacity_left:
            solution_bits[i] = 1
            capacity_left -= problem.weights[i]
            total_value += problem.values[i]
            total_weight += problem.weights[i]
            
    return solution_bits, total_value, total_weight