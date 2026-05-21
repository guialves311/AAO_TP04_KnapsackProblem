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

# Loads .env variables
load_dotenv()
data_folder= str(os.getenv("DATA_FILE"))
num_iterations= int(os.getenv("NUM_ITERATIONS"))

def main():
    # Gets the folder with the problems loaded
    path = Path(data_folder)

    # Does not proceed if no designated folder is found  
    if not path.exists():
        print(f"Error: Instance file {data_folder} not found!")
        return

    # Gets each .txt extension file inside the folder
    for file_path in path.glob("*.txt"):
        print(f"Instância: {file_path}")
        # Creates a KnapsackProblem class
        problem = instance_reader(file_path)
        
        print(f"Number of items: {problem.num_items}")
        print(f"Knapsack capacity: {problem.capacity}")
        print("------------------------------")
        
        # Runs benchmarks
        run_benchmarks(f"{file_path}", problem, num_iterations)
main()