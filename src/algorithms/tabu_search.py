import random

def tabu_search(problem, initial_bits, num_iterations, tabu_size):
    """
    Executa o algoritmo Tabu Search para o Knapsack Problem.
    Recebe o objeto 'problem', a solução inicial em bits e os parâmetros do algoritmo.
    """
    # 1. Inicializar o estado atual e as métricas
    current_bits = list(initial_bits)
    current_value = problem.calculate_value(current_bits)
    current_weight = problem.calculate_weight(current_bits)
    
    best_bits = list(current_bits)
    best_value = current_value

    tabu_list = []
    
    # 2. Ciclo Principal da Tabu Search
    for _ in range(num_iterations):
        # Mapeia os índices que estão dentro (1) e fora (0) da mochila atualmente
        itens_dentro = [i for i, bit in enumerate(current_bits) if bit == 1]
        itens_fora = [i for i, bit in enumerate(current_bits) if bit == 0]
        
        # Salvaguarda se não for possível realizar um swap
        if not itens_dentro or not itens_fora:
            continue
            
        # Gera um vizinho através de um Swap aleatório
        idx_remover = random.choice(itens_dentro)
        idx_adicionar = random.choice(itens_fora)
        
        # Cálculo matemático rápido do impacto do vizinho
        neighbor_weight = current_weight - problem.weights[idx_remover] + problem.weights[idx_adicionar]
        neighbor_value = current_value - problem.values[idx_remover] + problem.values[idx_adicionar]
        
        # O movimento é definido pelo par de índices (quem sai, quem entra)
        move = (idx_remover, idx_adicionar)
        
        # 3. Critério de Aceitação e Validação Tabu
        # Critério de Aspiração: se o movimento for tabu mas der um resultado melhor que o melhor global, aceitamos na mesma!
        criterio_aspiracao = neighbor_value > best_value
        movimento_permitido = move not in tabu_list or criterio_aspiracao
        
        if neighbor_weight <= problem.capacity and movimento_permitido:
            # Faz a transição para o vizinho
            current_bits[idx_remover] = 0
            current_bits[idx_adicionar] = 1
            current_value = neighbor_value
            current_weight = neighbor_weight
            
            # Atualiza a lista Tabu (adiciona ao fim)
            tabu_list.append(move)
            
            # Se a lista Tabu exceder o tamanho máximo, remove o movimento mais antigo (FIFO)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
                
        # 4. Atualizar a melhor solução global encontrada até ao momento
        if current_value > best_value:
            best_bits = list(current_bits)
            best_value = current_value
            
    return best_bits, best_value