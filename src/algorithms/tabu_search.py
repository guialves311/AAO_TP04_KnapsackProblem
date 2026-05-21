import random
from algorithms.classes.KnapsackProblem import KnapsackProblem

def tabu_search(problem: KnapsackProblem, initial_bits: list, initial_value: int, initial_weight: int, num_iterations: int, tabu_size: int):
    """Solves the 0/1 Knapsack Problem using Tabu Search.
    
    A metaheuristic optimization algorithm that maintains a tabu list of recent moves
    to avoid cycling and escape local optima. Allows moves to worse solutions unless 
    they improve the global best.
    
    Args:
        problem: The knapsack problem instance
        initial_bits (list): Initial binary solution
        initial_value (int): Value of the initial solution
        initial_weight (int): Weight of the initial solution
        num_iterations (int): Number of iterations to perform
        tabu_size (int): Maximum size of the tabu list
    
    Returns:
        tuple: A tuple containing:
            - best_bits (list): Best binary solution found
            - best_value (int): Best value achieved
            - best_weight (int): Weight of the best solution
    """
    
    # Create a new list in order to not alter the original list
    current_bits = list(initial_bits)
    current_value = initial_value
    current_weight = initial_weight
    
    best_bits = list(current_bits)
    best_value = current_value
    best_weight = current_weight

    tabu_list = []
    
    for _ in range(num_iterations):
        # Identify item current in and out of knapsack
        items_in = [i for i, bit in enumerate(current_bits) if bit == 1]
        items_out = [i for i, bit in enumerate(current_bits) if bit == 0]
    
        if not items_in or not items_out:
            continue # Skip if no swaps possible
            
        # Geerate neighbor by swapping one item in with one item out
        item_remove = random.choice(items_in)
        item_add = random.choice(items_out)
        
        neighbor_weight = current_weight - problem.weights[item_remove] + problem.weights[item_add]
        neighbor_value = current_value - problem.values[item_remove] + problem.values[item_add]
        
        # Represent the swap
        move = (item_remove, item_add)
        
        # Accept move if valid (doesn't exceed capacity) and not tabu (if it improves global best)
        aspiration_criterion = neighbor_value > best_value
        move_allowed = move not in tabu_list or aspiration_criterion
        
        if neighbor_weight <= problem.capacity and move_allowed:
            current_bits[item_remove] = 0
            current_bits[item_add] = 1
            current_value = neighbor_value
            current_weight = neighbor_weight
            
            # Update tabu list
            tabu_list.append(move)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
                
        # Update global best solution 
        if current_value > best_value:
            best_bits = list(current_bits)
            best_value = current_value
            best_weight = current_weight
            
    return best_bits, best_value, best_weight