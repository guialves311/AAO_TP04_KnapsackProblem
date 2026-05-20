import math
import random
import os

def simulated_annealing(problem, initial_bits, initial_value, initial_weight, num_iterations):
    temperature = float(os.getenv("TEMPERATURE", 100000.0))
    cooling_rate = float(os.getenv("COOLING_RATE", 0.995))

    current_bits = list(initial_bits)
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
            
        # Randomly choose a neighbor by swappinf on item
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
            
            if accept:
                current_bits[item_remove] = 0
                current_bits[item_add] = 1
                current_value = neighbor_value
                current_weight = neighbor_weight
                
                if current_value > best_value:
                    best_bits = list(current_bits)
                    best_value = current_value
                    
        # Cool down the temperature
        temperature *= cooling_rate
        
    return best_bits, best_value, current_weight