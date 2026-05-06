from DataGenerator import generate_instance
from pathlib import Path
from JSONReader import json_reader
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.hillclimb import hill_climbing, calculate_value, calculate_weight  # Adicionado o teu import[cite: 1, 2]
from dotenv import load_dotenv
import os

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
        
    value, items, weight, selected_item = greedy(data['items'], data['sack_capacity'])  

    ordered_items, relaxed_value = relaxation_greedy(data['items'], data['sack_capacity'])
    final_solution, value = enhanced_greedy(ordered_items, data['sack_capacity'])
    best_solution, best_value = simulated_annealing(
        final_solution,
        value,
        sum(item['weight'] for item in final_solution),
        data['items'],
        data['sack_capacity'],
        num_iterations
    )
    
    ids_no_sa = {item['id'] for item in best_solution}
    bit_solution_input = [1 if item['id'] in ids_no_sa else 0 for item in data['items']]
    
    refined_bits = hill_climbing(data['items'], data['sack_capacity'], bit_solution_input)
    
    final_value_hc = calculate_value(refined_bits, data['items'])
    final_weight_hc = calculate_weight(refined_bits, data['items'])

    print("Greedy value:", value)
    print("Greedy items:", [item['id'] for item in final_solution])
    print("SA best value:", best_value)
    print("SA items:", [item['id'] for item in best_solution])
    print("Hillclimb final value: ", final_value_hc)
    print("Hillclimb final weight: ", final_weight_hc)

main()