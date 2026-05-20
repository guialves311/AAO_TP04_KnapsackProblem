from pathlib import Path
import os
from dotenv import load_dotenv
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.hillclimb import hill_climbing
from algorithms.tabu_search import tabu_search
from utils.instanceReader import instance_reader
from benchmarks.performance_comparison import run_benchmarks

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
        
    run_benchmarks("aaa", problem)
   

main()