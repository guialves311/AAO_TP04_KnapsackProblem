import math
import random
import os

def simulated_annealing(problem, initial_bits, num_iterations):
    temperature = float(os.getenv("TEMPERATURE", 100000.0))
    cooling_rate = float(os.getenv("COOLING_RATE", 0.995))
        
    current_bits = list(initial_bits)
    current_value = problem.calculate_value(current_bits)
    current_weight = problem.calculate_weight(current_bits)
    
    best_bits = list(current_bits)
    best_value = current_value

    for _ in range(num_iterations):
        itens_dentro = [i for i, bit in enumerate(current_bits) if bit == 1]
        itens_fora = [i for i, bit in enumerate(current_bits) if bit == 0]

        if not itens_dentro or not itens_fora:
            continue
            
        idx_remover = random.choice(itens_dentro)
        idx_adicionar = random.choice(itens_fora)
        
        neighbor_weight = current_weight - problem.weights[idx_remover] + problem.weights[idx_adicionar]
        neighbor_value = current_value - problem.values[idx_remover] + problem.values[idx_adicionar]
        
        if neighbor_weight <= problem.capacity:
            delta = neighbor_value - current_value
            
            if delta > 0:
                aceitar = True
            else:
                if temperature > 0:
                    probability = math.exp(delta / temperature)
                    aceitar = random.random() < probability
                else:
                    aceitar = False
            
            if aceitar:
                current_bits[idx_remover] = 0
                current_bits[idx_adicionar] = 1
                current_value = neighbor_value
                current_weight = neighbor_weight
                
                if current_value > best_value:
                    best_bits = list(current_bits)
                    best_value = current_value
                    
        temperature *= cooling_rate
        
    return best_bits, best_value