import random

def tabu_search(initial_solution, all_items, max_capacity, num_iterations, tabu_size):
    current_solution = list(initial_solution)
    current_value = sum(item['value'] for item in current_solution)
    best_solution = list(current_solution)
    best_value = current_value
    
    tabu_list = []
    
    for iteration in range(num_iterations):
        #Neighborhood solutions (swap one item for another)
        neighbor = list(current_solution)
        item_remove = random.choice(neighbor)
        item_add = random.choice([item for item in all_items if item not in neighbor])
        neighbor.remove(item_remove)
        neighbor.append(item_add)
        
        #Choose best neighbor solution
        value_neighbor = sum(item['value'] for item in neighbor)
        weight_neighbor = sum(item['weight'] for item in neighbor)
        
        move = (item_remove['id'], item_add['id'])

        #Check if the move has already been made
        if weight_neighbor <= max_capacity and (move not in tabu_list or value_neighbor > best_value):
            current_solution = list(neighbor)
            current_value = value_neighbor
            tabu_list.append(move)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
        
        #Refresh global best solution
        if current_value > best_value:
            best_solution = list(current_solution)
            best_value = current_value
            
    return best_solution, best_value
        
    