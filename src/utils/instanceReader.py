from algorithms.classes.KnapsackProblem import KnapsackProblem

def instance_reader(file_path):
    values = []
    weights = []
    capacity = 0
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("["):
                continue
            
            parts = line.split()
            if len(parts) == 3:
                values.append(int(parts[1]))
                weights.append(int(parts[2]))
            elif len(parts) == 1:
                val = int(parts[0])
                if val > 1000: 
                    capacity = val
                    
    return KnapsackProblem(capacity, values, weights)