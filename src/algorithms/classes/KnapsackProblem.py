class KnapsackProblem:
    """
        Class to centralize the KP01 information
        
        Args:
            capacity (int): Capacity described by the problem
            values (list): List of the item's values
            weights (list): List of the item's weights
    """
    
    def __init__(self, capacity: int, values: list, weights: list):
        self.capacity = capacity
        self.values = values
        self.weights = weights
        self.num_items = len(values)

    def calculate_value(self, solution_bits: list):
        """Calculate total value of a binary solution.

        Given a list of bits (0/1) indicating which items are selected in the
        knapsack, returns the sum of the corresponding item values.

        Args:
            solution_bits (list): Binary list where `1` means the item is included
                                and `0` means it is not.

        Returns:
            int: Total value (sum of `self.values` for selected items).
        """
        # Calculates total value of a solution given as a list of bits [1, 0, 1...]
        return sum(self.values[i] for i, bit in enumerate(solution_bits) if bit == 1)

    def calculate_weight(self, solution_bits: list):
        """Calculate total weight of a binary solution.

        Given a list of bits (0/1) indicating which items are selected in the
        knapsack, returns the sum of the corresponding item weights.

        Args:
            solution_bits (list): Binary list where `1` means the item is included
                                and `0` means it is not.

        Returns:
            int: Total weight (sum of `self.weights` for selected items).
        """
        # Calculates total weight of a solution given as a list of bits [1, 0, 1...]
        return sum(self.weights[i] for i, bit in enumerate(solution_bits) if bit == 1)