from algorithms.classes.KnapsackProblem import KnapsackProblem

def instance_reader(file_path):
    values = []
    weights = []
    capacity = 0
    
    # Open the file to read
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("["): # Skip empty lines and lines starting with "[" (e.g., "Knapsack Problem Instance [ID: 1]")
                continue
            
            parts = line.split()
            # Line has 3 parts = index_value_weight
            if len(parts) == 3:
                values.append(int(parts[1]))
                weights.append(int(parts[2]))
            # Line has 1 part = capacity
            elif len(parts) == 1:
                val = int(parts[0])
                if val > 1000: 
                    capacity = val
                    
    return KnapsackProblem(capacity, values, weights)