import time
import numpy as np
import csv
from algorithms.hillclimb import hill_climbing
from algorithms.relaxation_greedy import enhanced_greedy
from algorithms.tabu_search import tabu_search
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing

import time

def algorithm_time(algorithm_function, problem, num_runs=5, **kwargs):
    # Runs the given algorithm multiple times and returns a list of execution times and results.
    times = []
    results = []
    
    for _ in range(num_runs):
        start_time = time.perf_counter()
        
        #Unpack the solution and value from the algorithm function
        solucao, value = algorithm_function(problem, **kwargs)
        
        end_time = time.perf_counter()
        
        times.append(end_time - start_time)
        results.append(value)
        
    return times, results

def correr_benchmark_completo(instance_name, problem_instance):
    # Runs all algorithms on the instance and saves results to CSV
    with open('results/benchmark_geral.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        
        # 1. GREEDY (5 runs, average time)
        times_greedy, values_greedy = algorithm_time(greedy, problem_instance, num_runs=5)
        avg_time_greedy = np.mean(times_greedy)
        value_greedy = values_greedy[0] # É sempre igual
        
        writer.writerow([instance_name, "Greedy", "-", value_greedy, avg_time_greedy])
        
        # 2. SIMULATED ANNEALING (10 runs, record all) 
        times_sa, values_sa = algorithm_time(simulated_annealing, problem_instance, num_runs=10)
        
        for idx, (t, v) in enumerate(zip(times_sa, values_sa)):
            writer.writerow([instance_name, "Simulated Annealing", f"Run_{idx}", v, t])
            
        # 3. HILL CLIMB
        # times_hc, results_hc = algorithm_time(hill_climb, problem_instance, num_runs=10)
        # ... (guardar no CSV)