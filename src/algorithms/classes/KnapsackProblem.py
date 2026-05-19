class KnapsackProblem:
    def __init__(self, capacity, values, weights):
        self.capacity = capacity
        self.values = values
        self.weights = weights
        self.num_items = len(values)

    def calculate_value(self, solution_bits):
        """Calcula o valor total de uma lista de bits [1, 0, 1...]"""
        return sum(self.values[i] for i, bit in enumerate(solution_bits) if bit == 1)

    def calculate_weight(self, solution_bits):
        """Calcula o peso total de uma lista de bits [1, 0, 1...]"""
        return sum(self.weights[i] for i, bit in enumerate(solution_bits) if bit == 1)