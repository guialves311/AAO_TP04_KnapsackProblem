# The relaxation with improved greedy algorithm approach to the knapsack problem

def relaxation_greedy(items, capacity):
    for item in items:
        item['density'] = item['value'] / item['weight']
    
    ordered_items = sorted(items, key=lambda x: x['density'], reverse = True)
    
    capacity_left = capacity
    total_relaxed_value = 0
    
    for item in ordered_items:
        if item['weight'] <= capacity_left:
            item['x'] = 1.0
            capacity_left -= item['weight']
            total_relaxed_value += item['value']
        else:
            item['x'] = capacity_left / item['weight']
            total_relaxed_value += item['value'] * item['x']
            capacity_left = 0
            
    return ordered_items, total_relaxed_value

def enhanced_greedy(relaxed_items, capacity):
    capacity_left = capacity
    value = 0
    weight = 0
    final_solution = []
    
    for item in relaxed_items:
        if item['weight'] <= capacity_left:
            capacity_left -= item['weight']
            value += item['value']
            weight += item['weight']
            final_solution.append(item)

    return final_solution, value, weight