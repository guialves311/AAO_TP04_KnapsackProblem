from algorithms.classes.KnapsackProblem import KnapsackProblem

def greedy(problem: KnapsackProblem):
    """Solves the 0/1 Knapsack Problem using the Greedy algorithm.
    
    Selects items in descending order of their value-to-weight ratio, 
    greedily adding items that fit within the knapsack capacity.
    
    Args:
        problem (KnapsackProblem): The knapsack problem instance containing items,
                                   weights, values, and capacity.
    
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
    
    total_value = 0
    total_weight = 0
    
    # Initialize the solution array
    solution_bits = [0] * problem.num_items 
    
    # Try to add items in sorted order if they fit
    for i in indices_sorted:
        #If the item can be added without exceeding capacity, add it to the solution
        if total_weight + problem.weights[i] <= problem.capacity:
            # Mark the item as included in the solution
            solution_bits[i] = 1
            # Update total value and weight
            total_value += problem.values[i]
            total_weight += problem.weights[i]
        
    return solution_bits, total_value, total_weight