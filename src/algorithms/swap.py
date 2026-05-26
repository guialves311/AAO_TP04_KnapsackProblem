from algorithms.classes.KnapsackProblem import KnapsackProblem

def swap(problem: KnapsackProblem, initial_bits: list, initial_value: int, initial_weight: int):
    
    """Improves a Knapsack solution using Swap Heuristic.
    
    A local search heuristic that looks to improve the initial solution provided by removing an item
    from the knapsack and replacing it with an item outside the knapsack, as long as the exchange 
    increases the knapsack's value and doesn't go over the maximum capacity.
    
    A First-Improvement strategy is used, the search stops at the first improving swap 
    found and restarts from the updated solution.

    Args:
        problem (KnapsackProblem): The knapsack problem instance containing items,
                                   weights, values, and capacity
        initial_bits (list): Initial binary solution
        initial_value (int): Value of the initial solution
        initial_weight (int): Weight of the initial solution

    Returns:
        tuple: A tuple containing:
            - current_solution (list): Binary solution at local optimum
            - current_value (int): Value of the local optimum
            - current_weight (int): Weight of the local optimum solution
    """
    
    # Number of items
    n = problem.num_items
    
    # Create a new list in order to not alter the original list
    current_solution = list(initial_bits)

    # Initialize current value and weight with the initial solution's value and weight
    current_value = initial_value
    current_weight = initial_weight
    
    # To track if an improvement was made in the current iteration
    improved = True
    
    # Continue searching until no improvement is found
    while improved:
        improved = False
        
        # Iterate over all items inside the knapsack
        for i in range(n):
            if current_solution[i] == 1:
                
                # Iterate over all items outside the knapsack
                for j in range(n):
                    if current_solution[j] == 0:
                        
                        # Caclculate value and weight differences if we swap item i with item j
                        weight_diff = problem.weights[j] - problem.weights[i]
                        value_diff = problem.values[j] - problem.values[i]
                        
                        # Condition for improvement:
                        # 1. New weight cannot go over the capacity
                        # 2. New value must improve the current solution
                        if current_weight + weight_diff <= problem.capacity and value_diff > 0:
                            
                            # Execute swap
                            current_solution[i] = 0
                            current_solution[j] = 1
                            
                            # Update total weight and value
                            current_weight += weight_diff
                            current_value += value_diff
                            
                            improved = True
                            
                            # Break internal cycle to restart search with the new improved solution (First-Improvement)
                            break
                    
                    if improved:
                        # Restart search from the improved solution
                        break
                    
    return current_solution, current_value, current_weight
    
    
    
    
    
    