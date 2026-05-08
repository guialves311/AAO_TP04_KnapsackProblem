import random
import os
import matplotlib.pyplot as plt

MUTATION_RATE = float(os.getenv("MUTATION_RATE", 0.1))

def get_solution_details(chromosome, profits, weights):
    """
    Função auxiliar para extrair o lucro e o peso total de uma solução.
    """
    total_profit = 0
    total_weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_profit += profits[i]
            total_weight += weights[i]
    return total_profit, total_weight


def calculate_fitness(chromosome, profits, weights, capacity):
    total_weight = sum(w for i, w in enumerate(weights) if chromosome[i] == 1)
    total_profit = sum(p for i, p in enumerate(profits) if chromosome[i] == 1)
    
    if total_weight <= capacity:
        return total_profit
    else:
        # Penaliza proporcionalmente ao excesso. 
        # O '10' é um fator de multa; ajuste se necessário.
        penalty = (total_weight - capacity) * 10 
        return max(0, total_profit - penalty)

def select_parents(population, fitnesses):
    """Seleção por Roleta (Roulette-wheel selection)[cite: 87]."""
    total_f = sum(fitnesses)
    if total_f == 0:
        return random.sample(population, 2)
    
    def pick_one():
        pick = random.uniform(0, total_f)
        current = 0
        for ind, f in zip(population, fitnesses):
            current += f
            if current > pick:
                return ind
        return population[-1]
    
    return pick_one(), pick_one()

def crossover(p1, p2):
    """Crossover de um ponto (Single-point crossover)."""
    point = random.randint(1, len(p1) - 1)
    offspring1 = p1[:point] + p2[point:]
    offspring2 = p2[:point] + p1[point:]
    return offspring1, offspring2

def mutate(chromosome):
    """Mutação por inversão de bits."""
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 if chromosome[i] == 0 else 0
    return chromosome

def calculate_attribute_importance(population, fitnesses):
    """
    Calcula a importância de cada gene usando uma lógica baseada em RST.
    Discretizamos o fitness em 'Bom' (1) ou 'Ruim' (0).
    """
    if not fitnesses or sum(fitnesses) == 0:
        return [0] * len(population[0])

    num_items = len(population[0])
    avg_fitness = sum(fitnesses) / len(fitnesses)
    
    # Decisão: 1 se fitness > média, senão 0
    decisions = [1 if f >= avg_fitness else 0 for f in fitnesses]
    
    importance_scores = []
    
    for i in range(num_items):
        # Calculamos a dependência: quantas vezes o valor do gene (0 ou 1)
        # coincide com a decisão de 'Bom lucro' (1)
        matches = 0
        for j in range(len(population)):
            if population[j][i] == decisions[j]:
                matches += 1
        
        importance = matches / len(population)
        importance_scores.append(importance)
        
    return importance_scores

def attribute_reduction_step(population, profits, weights, capacity):
    # 1. Identifica a importância (como fizemos antes)
    fitnesses = [sum(p for i, p in enumerate(profits) if ind[i] == 1) for ind in population]
    importances = calculate_attribute_importance(population, fitnesses)
    
    refined_population = []
    for chromo in population:
        temp_ind = list(chromo)
        
        # REPARO ATIVO: Enquanto estiver acima do peso...
        while sum(weights[i] for i, gene in enumerate(temp_ind) if gene == 1) > capacity:
            # Encontra os genes ativos (1)
            active_genes = [i for i, gene in enumerate(temp_ind) if gene == 1]
            if not active_genes: break
            
            # DESLIGA o gene que tem a MENOR importância segundo a RST
            # Isso é o GA "aprendendo" a tirar o lixo para caber o que importa
            least_important = min(active_genes, key=lambda x: importances[x])
            temp_ind[least_important] = 0
            
        refined_population.append(temp_ind)
    return refined_population

def run_hybrid_ga(profits, weights, capacity, pop_size=10, gen_limit=30, initial_solution=None):
    num_items = len(profits)
    population = []
    history = []
    
    if initial_solution:
        if len(initial_solution) == num_items:
            population.append(list(initial_solution))
    
    while len(population) < pop_size:
        population.append([random.randint(0, 1) for _ in range(num_items)])

    for _ in range(gen_limit):
        # 1. Avaliação
        fitnesses = [calculate_fitness(ind, profits, weights, capacity) for ind in population]
        
        # --- INÍCIO DA ALTERAÇÃO (ELITISMO) ---
        # Encontramos o melhor da geração ATUAL para protegê-lo
        max_fit = max(fitnesses)
        history.append(max_fit)
        
        best_idx = fitnesses.index(max_fit)
        elite = list(population[best_idx]) # Salvamos uma cópia do "Rei"
        # --- FIM DA ALTERAÇÃO ---

        new_population = []
        
        # Criamos a nova geração, mas deixamos 1 vaga livre para o elite
        while len(new_population) < (pop_size - 1): 
            p1, p2 = select_parents(population, fitnesses) 
            c1, c2 = crossover(p1, p2)
            
            # Mutamos os filhos normalmente
            new_population.append(mutate(c1))
            if len(new_population) < (pop_size - 1):
                new_population.append(mutate(c2))
        
        # 6. Passo Híbrido (RST) processa os novos indivíduos
        # Note que passamos a 'new_population' que tem (pop_size - 1) elementos
        population = attribute_reduction_step(new_population, profits, weights, capacity)
        
        # --- REINSERÇÃO DO ELITE ---
        # Agora o elite volta para a população sem ter sofrido mutação ou RST
        population.append(elite)
        # ---------------------------
        
    # Resto do código permanece igual...
    final_fitnesses = [calculate_fitness(ind, profits, weights, capacity) for ind in population]
    best_idx = final_fitnesses.index(max(final_fitnesses))
    best_chromosome = population[best_idx]
    
    profit, weight = get_solution_details(best_chromosome, profits, weights)
    
    return {
        "best_solution": best_chromosome,
        "total_profit": profit,
        "total_weight": weight,
        "history": history
    }
    
def plot_evolution(history, greedy_value):
    plt.figure(figsize=(10, 5))
    plt.plot(history, label='Evolução do GA Híbrido', color='blue', linewidth=2)
    plt.axhline(y=greedy_value, color='red', linestyle='--', label='Resultado do Greedy')
    
    plt.title('Evolução do Lucro por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Lucro (Fitness)')
    plt.legend()
    plt.grid(True)
    plt.show()
