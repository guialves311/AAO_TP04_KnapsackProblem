import math
import random
import os
from algorithms.classes.KnapsackProblem import KnapsackProblem

def simulated_annealing(problem: KnapsackProblem, initial_bits: list, initial_value: int, initial_weight: int, num_iterations: int):
    """Solves the 0/1 Knapsack Problem using Simulated Annealing.
    
    A metaheuristic optimization algorithm that probabilistically accepts worse 
    solutions early on to escape local optima, then gradually reduces acceptance 
    probability as "temperature" cools.
    
    Args:
        problem: The knapsack problem instance
        initial_bits (list): Initial binary solution
        initial_value (int): Value of the initial solution
        initial_weight (int): Weight of the initial solution
        num_iterations (int): Number of iterations to perform
    
    Returns:
        tuple: A tuple containing:
            - best_bits (list): Best binary solution found
            - best_value (int): Best value achieved
            - current_weight (int): Weight of the best solution
    
    Note:
        Uses environment variables TEMPERATURE and COOLING_RATE for tuning
    """
    
    # Load .env variables
    temperature = float(os.getenv("TEMPERATURE", 100000.0))
    cooling_rate = float(os.getenv("COOLING_RATE", 0.995))

    # Create a new list in order to not alter the original list
    current_bits = list(initial_bits)
    
    # Inserts the initial solution value and weight
    current_value = initial_value
    current_weight = initial_weight
    
    # Keep track of the best solution found
    best_bits = list(current_bits)
    best_value = current_value


    for _ in range(num_iterations):
        # Get items inside and outside the knapsack
        items_in = [i for i, bit in enumerate(current_bits) if bit == 1]
        items_out = [i for i, bit in enumerate(current_bits) if bit == 0]

        if not items_in or not items_out:
            continue # Skip if we can't swap any items
            
        # Randomly choose a neighbor by swapping on item
        item_remove = random.choice(items_in)
        item_add = random.choice(items_out)
        
        # Calculate neighbor's weight and value
        neighbor_weight = current_weight - problem.weights[item_remove] + problem.weights[item_add]
        neighbor_value = current_value - problem.values[item_remove] + problem.values[item_add]
        
        # Accept the neighbor solution based on the acceptance probability
        if neighbor_weight <= problem.capacity:
            delta = neighbor_value - current_value 
            
            if delta > 0:
                accept = True # Always accept improvements
            else:
                # Accept worse solution with a probability depending on temperature
                probability = math.exp(delta / temperature) if temperature > 0 else 0
                accept = random.random() < probability
            
            # If accepted, switch solution bits and current information
            if accept:
                current_bits[item_remove] = 0
                current_bits[item_add] = 1
                current_value = neighbor_value
                current_weight = neighbor_weight
                
                # If the current value is higher than best value, update the best solution and best value
                if current_value > best_value:
                    best_bits = list(current_bits)
                    best_value = current_value
                    
        # Cool down the temperature
        temperature *= cooling_rate
        
    return best_bits, best_value, current_weight