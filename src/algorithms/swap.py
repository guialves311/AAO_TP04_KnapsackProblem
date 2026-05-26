from algorithms.classes.KnapsackProblem import KnapsackProblem

def swap(problem: KnapsackProblem, initial_solution: list):
    
    """Solves the 0/1 Knapsack Problem using Swap Heuristic.
    
    A local search heuristic that looks to improve the initial solution provided by withdrawing an item
    from the knapsack and replacing it with an item left out, as long as the exchange increases the knapsack's
    value and doesn't go over the maximum capacity.

    Args:
        problem (KnapsackProblem): The knapsack problem instance containing items,
                                   weights, values, and capacity
        initial_solution (list): Initial binary solution

    Returns:
        tuple: A tuple containing:
            - current_solution (list): Binary solution at local optimum
            - current_value (int): Value of the local optimum
            - current_weight (int): Weight of the local optimum solution
    """
    
    # Window for the search cycles
    n = problem.num_items
    
    # Create a new list in order to not alter the original list
    current_solution = list(initial_solution)
    
    # Inserts the initial solution value and weight
    current_weight = problem.calculate_weight(current_solution)
    current_value = problem.calculate_value(current_solution)
    
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
                        
                        # DELTA: Calculate the difference
                        weight_diff = problem.weights[j] - problem.weights[i]
                        value_diff = problem.values[j] - problem.values[i]
                        
                        # Condition for improvement:
                        # 1. New weight cannot go over the capacity
                        # 2. New value has to be higher than the intial value
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
                        # Break external cycle for the same reason
                        break
                    
    return current_solution, current_value, current_weight
    
    
    
    
    
    