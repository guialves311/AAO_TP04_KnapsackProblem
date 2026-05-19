from pathlib import Path
import os
from dotenv import load_dotenv
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.hillclimb import hill_climbing
from algorithms.tabu_search import tabu_search
from utils.instanceReader import instance_reader

load_dotenv()
data_file= str(os.getenv("DATA_FILE"))
num_iterations= int(os.getenv("NUM_ITERATIONS"))

def main():
    # Check if the instance file exists
    if not Path(data_file).exists():
        print(f"Error: Instance file {data_file} not found!")
        return

    print(f"Instância: {data_file}")
    
    # ----------------------------
    # Load instance data
    # ----------------------------
    problem = instance_reader(data_file)
    
    print(f"Number of items: {problem.num_items}")
    print(f"Knapsack capacity: {problem.capacity}")
    print("------------------------------")
        
    # ----------------------------
    # Base algorithms
    # ----------------------------
    greedy_bits, greedy_value = greedy(problem)  

    x_fractions, relaxed_value = relaxation_greedy(problem)
    enhanced_bits, enhanced_value, enhanced_weight = enhanced_greedy(problem, x_fractions)
    
    # =========================================================================
    # FLOW 1: Starting from standard Greedy
    # =========================================================================
    # Simulated Annealing
    sa_bits, sa_value = simulated_annealing(
        problem,
        greedy_bits,
        num_iterations
    )
    
    # Tabu Search 
    tabu_bits, tabu_value = tabu_search(
        problem,
        greedy_bits,
        num_iterations,
        10
    )
    
    # Hill Climbing
    hc_bits = hill_climbing(problem, greedy_bits)
    final_value_hc = problem.calculate_value(hc_bits)
    final_weight_hc = problem.calculate_weight(hc_bits)
    
    # =========================================================================
    # FLOW 2: Starting from Enhanced Greedy
    # =========================================================================
    # Simulated Annealing
    sa_bits_enhanced, sa_value_enhanced = simulated_annealing(
        problem,
        enhanced_bits,
        num_iterations
    )
    
    # Tabu Search 
    tabu_bits_enhanced, tabu_value_enhanced = tabu_search(
        problem,
        enhanced_bits,
        num_iterations,
        10
    )
    
    # Hill Climbing 
    hc_bits_enhanced = hill_climbing(problem, enhanced_bits)
    final_value_hc_enhanced = problem.calculate_value(hc_bits_enhanced)
    final_weight_hc_enhanced = problem.calculate_weight(hc_bits_enhanced)
    

    # =========================================================================
    # Print results
    # =========================================================================
    print("Greedy value:", greedy_value)
    print("Greedy SA best value:", sa_value)
    print("Greedy Hillclimb final value: ", final_value_hc)
    #print("Greedy Hillclimb final weight: ", final_weight_hc)
    print("Greedy Tabu Search best value:", tabu_value)
    print("------------------------------")
    print("Enhanced Greedy value:", enhanced_value)
    #print("Enhanced greedy weight: ", enhanced_weight)
    print("Enhanced Greedy SA best value:", sa_value_enhanced)
    print("Enhanced Greedy Hillclimb final value: ", final_value_hc_enhanced)
    #print("Enhanced Greedy Hillclimb final weight: ", final_weight_hc_enhanced)
    print("Enhanced Greedy Tabu Search best value:", tabu_value_enhanced)
   

main()