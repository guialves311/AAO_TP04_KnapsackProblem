class KnapsackProblem:
    def __init__(self, capacity, values, weights):
        self.capacity = capacity
        self.values = values
        self.weights = weights
        self.num_items = len(values)

    def calculate_value(self, solution_bits):
        # Calculates total value of a solution given as a list of bits [1, 0, 1...]
        return sum(self.values[i] for i, bit in enumerate(solution_bits) if bit == 1)

    def calculate_weight(self, solution_bits):
        # Calculates total weight of a solution given as a list of bits [1, 0, 1...]
        return sum(self.weights[i] for i, bit in enumerate(solution_bits) if bit == 1)