from algorithms.classes.KnapsackProblem import KnapsackProblem

def swap(problem: KnapsackProblem, weights: int, values: int, capacity: int, initial_solution: list):
    
    n = len(weights)
    
    current_solution = list(initial_solution)
    
    current_weight = sum(weights[i] for i in range(n) if current_solution(i) == 1)
    current_value = sum(values[i] for i in range(n) if current_solution(i) == 1)
    
    improved = True
    
    while improved:
        improved = False
        
        for i in range(n):
            if current_solution[i] == 1:
                
                for j in range(n):
                    if current_solution[j] == 0:
                        weight_diff = weights[j] - weights[i]
                        value_diff = values[j] - values[i]
                        
                        if current_weight + weight_diff <= capacity and value_diff > 0:
                            current_solution[i] = 0
                            current_solution[j] = 1
                            
                            improved = True
                            break
                    
                    if improved:
                        break
                    
    return current_solution, current_value, current_weight
    
    
    
    
    
    