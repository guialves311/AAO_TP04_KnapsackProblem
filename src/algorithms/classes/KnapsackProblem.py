class KnapsackProblem:
    """
        Class to centralize the KP01 information
        
        Args:
            capacity
    """
    
    def __init__(self, capacity: int, values: list, weights: list):
        self.capacity = capacity
        self.values = values
        self.weights = weights
        self.num_items = len(values)

    def calculate_value(self, solution_bits: list):
        # Calculates total value of a solution given as a list of bits [1, 0, 1...]
        return sum(self.values[i] for i, bit in enumerate(solution_bits) if bit == 1)

    def calculate_weight(self, solution_bits: list):
        # Calculates total weight of a solution given as a list of bits [1, 0, 1...]
        return sum(self.weights[i] for i, bit in enumerate(solution_bits) if bit == 1)