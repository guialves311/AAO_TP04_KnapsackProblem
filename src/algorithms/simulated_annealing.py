import math
import random
import os

def simulated_annealing(initial_solution, initial_value, initial_weight, all_items, max_capacity, num_iterations):
    current_solution = initial_solution
    current_value = initial_value
    current_weight = initial_weight
    best_solution = list(current_solution)
    best_value = current_value
    
    #SA Parameters
    temperature = int(os.getenv("TEMPERATURE", 500))
    cooling_rate = float(os.getenv("COOLING_RATE", 0.99))
               
    #SA Loop            
    for _ in range(num_iterations):
        #Create neighbor solution
        neighbor_solution = list(current_solution)
    
        item_to_remove = random.choice(neighbor_solution)
        item_to_add = random.choice([item for item in all_items if item not in neighbor_solution])
            
        neighbor_solution.remove(item_to_remove)
        neighbor_solution.append(item_to_add)
                
        neighbor_value = sum(item['value'] for item in neighbor_solution) 
        neighbor_weight = sum(item['weight'] for item in neighbor_solution)    
        
        #Accept or reject neighbor solution
        if neighbor_weight <= max_capacity:
            delta = neighbor_value - current_value
            probability = math.exp(delta / temperature)    
            if delta > 0 or random.random() < probability:
                current_solution = list(neighbor_solution)
                current_value = neighbor_value
                current_weight = neighbor_weight
                if current_value > best_value:
                    best_solution = list(current_solution)
                    best_value = current_value
        temperature *= cooling_rate
        
    return best_solution, best_value