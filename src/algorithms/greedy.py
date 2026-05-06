# The greedy approach to the knapsack problem

def greedy(items, capacity):
    items_sorted = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)
    
    total_value=0
    total_weight=0
    chosen_items=[]
    item_selected=False
    
    for item in items_sorted:
        if total_weight + item['weight'] <= capacity:
            chosen_items.append(item)
            total_value += item['value']
            total_weight += item['weight']
            item_selected=True
        
    return total_value, chosen_items, total_weight, item_selected