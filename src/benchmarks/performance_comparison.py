import time
import numpy as np

# Importações dos teus algoritmos
from algorithms.greedy import greedy
from algorithms.hillclimb import hill_climbing
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.simulated_annealing import simulated_annealing
from algorithms.tabu_search import tabu_search

def algorithm_time(algorithm_function, problem, num_runs=1, **kwargs):
    times = []
    results = []
    weights = []
    for _ in range(num_runs):
        start_time = time.perf_counter()
        solution, value, weight = algorithm_function(problem, **kwargs)
        end_time = time.perf_counter()
        
        times.append(end_time - start_time)
        results.append(value)
        weights.append(weight)
    return times, results, weights

def run_benchmarks(instance_name, problem_instance, num_iterations=1000):
    print("\n" + "="*80)
    print(f" EXECUÇÃO DE BENCHMARK: {instance_name}")
    print(f" NÚMERO DE ITENS: {problem_instance.num_items} | CAPACIDADE: {problem_instance.capacity}")
    print("="*80)
    
    # Table results header 
    print(f"{'Algoritmo':<25} | {'Origem':<18} | {'Nº De Voltas':<15} | {'Melhor Valor':<15} | {'Valor Médio':<15} | {'Tempo Médio (s)':<15}")
    print("-"*80)

    # =========================================================================
    # 1. ALGORITMOS BASE (Soluções Iniciais)
    # =========================================================================
    
    # --- GREEDY NORMAL ---
    t_greedy, v_greedy, w_greedy = algorithm_time(greedy, problem_instance)
    greedy_bits, greedy_val, greedy_weight = greedy(problem_instance) 
    print(f"{'Greedy Normal':<25} | {'N/A':<18} | {'5':<15} | {greedy_val:<15} | {np.mean(v_greedy):.2f} | {np.mean(t_greedy):.6f}")

    # --- ENHANCED GREEDY ---
    x_fractions, _ = relaxation_greedy(problem_instance)
    t_enhanced, v_enhanced, w_enhanced = algorithm_time(enhanced_greedy, problem_instance, x_fractions=x_fractions)
    enhanced_bits, enhanced_val, enhanced_weight = enhanced_greedy(problem_instance, x_fractions)
    print(f"{'Enhanced Greedy':<25} | {'N/A':<18} | {'5':<15} | {enhanced_val:<15} | {np.mean(v_enhanced):.2f} | {np.mean(t_enhanced):.6f}")
    
    print("-"*80)

    # =========================================================================
    # 2. Algorithms with origem in Greedy Normal
    # =========================================================================
    
    # --- Simulated Annealing ---
    t_sa, v_sa, w_sa = algorithm_time(simulated_annealing, problem_instance, initial_bits=greedy_bits, initial_value=greedy_val, initial_weight=greedy_weight, num_iterations=num_iterations)
    print(f"{'Simulated Annealing':<25} | {'Greedy':<18} | {'5':<15} | {max(v_sa):<15} | {np.mean(v_sa):.2f} | {np.mean(t_sa):.6f}")

    # --- Tabu Search ---
    t_tabu, v_tabu, w_tabu = algorithm_time(tabu_search, problem_instance, initial_bits=greedy_bits, initial_value=greedy_val, initial_weight=greedy_weight, num_iterations=num_iterations, tabu_size=10)
    print(f"{'Tabu Search':<25} | {'Greedy':<18} | {'5':<15} | {max(v_tabu):<15} | {np.mean(v_tabu):.2f} | {np.mean(t_tabu):.6f}")

    # --- Hill Climbing (Garante que devolve tuplo (bits, valor) no teu ficheiro) ---
    t_hc, v_hc, w_hc = algorithm_time(hill_climbing, problem_instance, initial_bits=greedy_bits, initial_value=greedy_val, initial_weight=greedy_weight)
    print(f"{'Hill Climbing':<25} | {'Greedy':<18} | {'5':<15} | {v_hc[0]:<15} | {np.mean(v_hc):.2f} | {np.mean(t_hc):.6f}")

    print("-"*80)

    # =========================================================================
    # 3. Algorithms with origem in Enhanced Greedy
    # =========================================================================
    
    # --- Simulated Annealing ---
    t_sa_eg, v_sa_eg, w_sa_eg = algorithm_time(simulated_annealing, problem_instance, initial_bits=enhanced_bits, initial_value=enhanced_val, initial_weight=enhanced_weight, num_iterations=num_iterations)
    print(f"{'Simulated Annealing':<25} | {'Enhanced Greedy':<18} | {'5':<15} | {max(v_sa_eg):<15} | {np.mean(v_sa_eg):.2f} | {np.mean(t_sa_eg):.6f}")

    # --- Tabu Search ---
    t_tabu_eg, v_tabu_eg, w_tabu_eg = algorithm_time(tabu_search, problem_instance, initial_bits=enhanced_bits, initial_value=enhanced_val, initial_weight=enhanced_weight, num_iterations=num_iterations, tabu_size=10)
    print(f"{'Tabu Search':<25} | {'Enhanced Greedy':<18} | {'5':<15} | {max(v_tabu_eg):<15} | {np.mean(v_tabu_eg):.2f} | {np.mean(t_tabu_eg):.6f}")

    # --- Hill Climbing ---
    t_hc_eg, v_hc_eg, w_hc_eg = algorithm_time(hill_climbing, problem_instance, initial_bits=enhanced_bits, initial_value=enhanced_val, initial_weight=enhanced_weight)
    print(f"{'Hill Climbing':<25} | {'Enhanced Greedy':<18} | {'5':<15} | {v_hc_eg[0]:<15} | {np.mean(v_hc_eg):.2f} | {np.mean(t_hc_eg):.6f}")

    print("="*80 + "\n")