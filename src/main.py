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
    if not Path(data_file).exists():
        print(f"Erro: O arquivo de instância {data_file} não foi encontrado!")
        return

    print(f"Instância: {data_file}")
    
    # 1. LEITURA DA INSTÂNCIA (Agora retorna o Objeto KnapsackProblem)
    problem = instance_reader(data_file)
    
    print(f"Numeros Itens: {problem.num_items}")
    print(f"Capacidade da mochila: {problem.capacity}")
    print("------------------------------")
        
    # 2. EXECUÇÃO DOS ALGORITMOS BASE (Retornam listas de bits [1, 0, 1...])
    greedy_bits, greedy_value = greedy(problem)  

    x_fractions, relaxed_value = relaxation_greedy(problem)
    enhanced_bits, enhanced_value, enhanced_weight = enhanced_greedy(problem, x_fractions)
    
    # =========================================================================
    # FLUXO 1: A partir do Enhanced Greedy
    # =========================================================================
    # Simulated Annealing
    sa_bits_enhanced, sa_value_enhanced = simulated_annealing(
        problem,
        enhanced_bits,
        num_iterations
    )
    
    # Tabu Search (Atualizada para usar objetos e bits!)
    tabu_bits_enhanced, tabu_value_enhanced = tabu_search(
        problem,
        enhanced_bits,
        num_iterations,
        10
    )
    
    # Hill Climbing refinando o resultado do Simulated Annealing
    hc_bits_enhanced = hill_climbing(problem, sa_bits_enhanced)
    final_value_hc_enhanced = problem.calculate_value(hc_bits_enhanced)
    final_weight_hc_enhanced = problem.calculate_weight(hc_bits_enhanced)
    
    # =========================================================================
    # FLUXO 2: A partir do Greedy Padrão
    # =========================================================================
    # Simulated Annealing
    sa_bits, sa_value = simulated_annealing(
        problem,
        greedy_bits,
        num_iterations
    )
    
    # Tabu Search (Atualizada para usar objetos e bits!)
    tabu_bits, tabu_value = tabu_search(
        problem,
        greedy_bits,
        num_iterations,
        10
    )
    
    # Hill Climbing refinando o resultado do Simulated Annealing
    hc_bits = hill_climbing(problem, sa_bits)
    final_value_hc = problem.calculate_value(hc_bits)
    final_weight_hc = problem.calculate_weight(hc_bits)

    # =========================================================================
    # PRINTS DOS RESULTADOS
    # =========================================================================
    print("Enhanced Greedy value:", enhanced_value)
    print("Enhanced greedy weight: ", enhanced_weight)
    print("Enhanced Greedy SA best value:", sa_value_enhanced)
    print("Enhanced Greedy Hillclimb final value: ", final_value_hc_enhanced)
    print("Enhanced Greedy Hillclimb final weight: ", final_weight_hc_enhanced)
    print("Enhanced Greedy Tabu Search best value:", tabu_value_enhanced)
    print("------------------------------")
    print("Greedy value:", greedy_value)
    print("Greedy SA best value:", sa_value)
    print("Greedy Hillclimb final value: ", final_value_hc)
    print("Greedy Hillclimb final weight: ", final_weight_hc)
    print("Greedy Tabu Search best value:", tabu_value)

main()