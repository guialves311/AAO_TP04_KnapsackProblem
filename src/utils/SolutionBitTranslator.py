def solution_bit_translator(solution, all_items):
    solution = {item['id'] for item in solution}
    bit_solution = [1 if item['id'] in solution else 0 for item in all_items]
    
    return bit_solution