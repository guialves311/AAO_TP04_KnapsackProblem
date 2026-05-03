from DataGenerator import generate_instance
from pathlib import Path
from JSONReader import json_reader
from algorithms.relaxation_greedy import relaxation_greedy, enhanced_greedy
from algorithms.greedy import greedy
#from dotenv import load_dotenv
import os

#load_dotenv()
#data_file= str(os.getenv("DATA_FILE"))
#max_capacity= int(os.getenv("MAX_CAPACITY"), 50)
#num_items= int(os.getenv("NUM_ITEMS"), 10)

def main():
    if Path("src\\data\\test_data.json").exists():
        data = json_reader("src\\data\\test_data.json")
    else:
        data = generate_instance(10, 50, "src\\data\\test_data.json")
        
    value, items, weight, selected_item = greedy(data['items'], data['sack_capacity'])    