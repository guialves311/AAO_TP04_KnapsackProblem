from pathlib import Path
import os
from dotenv import load_dotenv
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.hillclimb import hill_climbing, calculate_value, calculate_weight
from algorithms.tabu_search import tabu_search
from utils.SolutionBitTranslator import solution_bit_translator
from utils.instanceReader import instance_reader

load_dotenv()
data_file= str(os.getenv("DATA_FILE"))
num_iterations= int(os.getenv("NUM_ITERATIONS"))

def main():
    if not Path(data_file).exists():
        print(f"Erro: O arquivo de instância {data_file} não foi encontrado!")
        return

    print(f"Instância: {data_file}")
    
    # LEITURA DA INSTÂNCIA NOVA
    data = instance_reader(data_file)
    
    print(f"Numeros Itens: {len(data['items'])}")
    print(f"Capacidade da mochila: {data['sack_capacity']}")
    print("------------------------------")
        
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
        sum(item['weight'] for item in items),
        data['items'],
        data['sack_capacity'],
        num_iterations
    )
    
    best_solution_tabu, best_value_tabu = tabu_search(
        items,
        data['items'],
        data['sack_capacity'],
        num_iterations,
        tabu_size=10
    )
    
    best_solution_tabu_enhanced, best_value_tabu_enhanced = tabu_search(
        final_solution,
        data['items'],
        data['sack_capacity'],
        num_iterations,
        tabu_size=10
    )
    
    
    bit_solution_input_enhanced = solution_bit_translator(best_solution_enhanced, data['items'])
    refined_bits_enhanced = hill_climbing(data['items'], data['sack_capacity'], bit_solution_input_enhanced)
    
    bit_solution_input = solution_bit_translator(best_solution, data['items'])
    refined_bits = hill_climbing(data['items'], data['sack_capacity'], bit_solution_input)
    
    final_value_hc_enhanced = calculate_value(refined_bits_enhanced, data['items'])
    final_weight_hc_enhanced = calculate_weight(refined_bits_enhanced, data['items'])
    
    final_value_hc = calculate_value(refined_bits, data['items'])
    final_weight_hc = calculate_weight(refined_bits, data['items'])

    print("Enhanced Greedy value:", enhanced_value)
    #print("Enhanced Greedy items:", [item['id'] for item in final_solution])
    print("Enhanced greedy weight: ", enhanced_weight)
    print("Enhanced Greedy SA best value:", best_value_enhanced)
    #print("Enhanced Greedy SA items:", [item['id'] for item in best_solution])
    print("Enhanced Greedy Hillclimb final value: ", final_value_hc_enhanced)
    print("Enhanced Greedy Hillclimb final weight: ", final_weight_hc_enhanced)
    print("Ehanced Greedy Tabu Search best value:", best_value_tabu_enhanced)
    #print("Enhanced Greedy Tabu items:", [item['id'] for item in best_solution_tabu])
    print("------------------------------")
    print("Greedy value:", value)
    #print("Greedy items:", [item['id'] for item in items])
    print("Greedy SA best value:", best_value)
    #print("Greedy SA items:", [item['id'] for item in best_solution])
    print("Greedy Hillclimb final value: ", final_value_hc)
    print("Greedy Hillclimb final weight: ", final_weight_hc)
    print("Greedy Tabu Search best value:", best_value_tabu)
    #print("Greedy Tabu items:", [item['id'] for item in best_solution_tabu])

main()