import time
import numpy as np
import csv
from algorithms.hillclimb import hill_climbing
from algorithms.relaxation_greedy import enhanced_greedy
from algorithms.tabu_search import tabu_search
from algorithms.greedy import greedy
from algorithms.simulated_annealing import simulated_annealing

import time

def algorithm_time(algorithm_function, problem, num_execucoes=5, **kwargs):
    """
    Corre qualquer algoritmo N vezes e devolve a lista de tempos e de valores.
    
    :param algorithm_function: A função do algoritmo (ex: greedy, simulated_annealing)
    :param problem: O objeto KnapsackProblem com os dados da instância
    :param num_execucoes: Número de vezes que o teste vai ser repetido
    :param kwargs: Argumentos extra dinâmicos (ex: initial_bits, initial_solution, tabu_size)
    """
    tempos = []
    valores = []
    
    for _ in range(num_execucoes):
        # Medição isolada de tempo
        start = time.perf_counter()
        
        # O '**kwargs' desempacota automaticamente os argumentos extras que passares.
        # Se passares 'initial_solution=sol', ele executa: algorithm_function(problem, initial_solution=sol)
        # Se não passares nada, executa apenas: algorithm_function(problem)
        solucao, valor = algorithm_function(problem, **kwargs)
        
        end = time.perf_counter()
        
        tempos.append(end - start)
        valores.append(valor)
        
    return tempos, valores

def correr_benchmark_completo(nome_instancia, dados_instancia):
    # Ficheiro único para guardar tudo ordenado
    with open('results/benchmark_geral.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        
        # --- 1. GREEDY (5 vezes e tiramos a média direto) ---
        tempos_g, valores_g = medir_algoritmo(greedy_knapsack, dados_instancia, num_execucoes=5)
        tempo_medio_g = np.mean(tempos_g)
        valor_g = valores_g[0] # É sempre igual
        
        # Guardamos apenas uma linha para o Greedy (já com o tempo médio)
        writer.writerow([nome_instancia, "Greedy", "-", valor_g, tempo_medio_g])
        
        # --- 2. SIMULATED ANNEALING (Registar todas as corridas) ---
        # Corremos mais vezes (ex: 10) porque o resultado varia com a seed
        tempos_sa, valores_sa = medir_algoritmo(simulated_annealing, dados_instancia, num_execucoes=10)
        
        for idx, (t, v) in enumerate(zip(tempos_sa, valores_sa)):
            writer.writerow([nome_instancia, "Simulated Annealing", f"Run_{idx}", v, t])
            
        # --- 3. HILL CLIMB (Igual ao SA) ---
        # tempos_hc, valores_hc = medir_algoritmo(hill_climb, dados_instancia, num_execucoes=10)
        # ... (guardar no CSV)