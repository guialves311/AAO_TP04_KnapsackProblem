from pathlib import Path
import os
from dotenv import load_dotenv
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.hillclimb import hill_climbing, calculate_value, calculate_weight
from utils.SolutionBitTranslator import solution_bit_translator
from utils.DataGenerator import generate_instance
from utils.JSONReader import json_reader
from utils.JSONtoArrays import json_to_arrays
from algorithms.genetic_algorithm import run_hybrid_ga

load_dotenv()
data_file= str(os.getenv("DATA_FILE"))
max_capacity= int(os.getenv("MAX_CAPACITY", 500))
num_items= int(os.getenv("NUM_ITEMS", 30))
num_iterations= int(os.getenv("NUM_ITERATIONS", 500))

def main():
    if Path(data_file).exists():
        data = json_reader(data_file)
    else:
        data = generate_instance(num_items, max_capacity, data_file)
        
    data_values, data_weights, data_ids = json_to_arrays(data)
        
    value, items, weight, selected_item = greedy(data['items'], data['sack_capacity'])

    ordered_items, relaxed_value = relaxation_greedy(data['items'], data['sack_capacity'])
    final_solution, enhanced_value, enhanced_weight = enhanced_greedy(ordered_items, data['sack_capacity'])
    
    best_solution_enhanced, best_value_enhanced = simulated_annealing(
        final_solution,
        enhanced_value,
        sum(item['weight'] for item in final_solution),
        data['items'],
        data['sack_capacity'],
        num_iterations
    )
    
    best_solution, best_value = simulated_annealing(
        items,
        value,
        sum(item['weight'] for item in final_solution),
        data['items'],
        data['sack_capacity'],
        num_iterations
    )
    
    bit_solution_input_enhanced = solution_bit_translator(best_solution_enhanced, data['items'])
    refined_bits_enhanced = hill_climbing(data['items'], data['sack_capacity'], bit_solution_input_enhanced)
    
    bit_solution_input = solution_bit_translator(best_solution, data['items'])
    refined_bits = hill_climbing(data['items'], data['sack_capacity'], bit_solution_input)
    
    testGA = run_hybrid_ga(data_values, data_weights, max_capacity, bit_solution_input)
    
    final_value_hc_enhanced = calculate_value(refined_bits_enhanced, data['items'])
    final_weight_hc_enhanced = calculate_weight(refined_bits_enhanced, data['items'])
    
    final_value_hc = calculate_value(refined_bits, data['items'])
    final_weight_hc = calculate_weight(refined_bits, data['items'])

    print("Enhanced Greedy value:", enhanced_value)
    print("Enhanced Greedy items:", [item['id'] for item in final_solution])
    print("Enhanced greedy weight: ", enhanced_weight)
    print("Enhanced Greedy SA best value:", best_value_enhanced)
    print("Enhanced Greedy SA items:", [item['id'] for item in best_solution])
    print("Enhanced Greedy Hillclimb final value: ", final_value_hc_enhanced)
    print("Enhanced Greedy Hillclimb final weight: ", final_weight_hc_enhanced)
    print("------------------------------")
    print("Greedy value:", value)
    print("Greedy items:", [item['id'] for item in items])
    print("Greedy SA best value:", best_value)
    print("Greedy SA items:", [item['id'] for item in best_solution])
    print("Greedy Hillclimb final value: ", final_value_hc)
    print("Greedy Hillclimb final weight: ", final_weight_hc)
    print("Test GA: ", testGA)

main()