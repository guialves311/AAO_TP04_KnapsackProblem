import json
def json_reader(file_name: str) -> str:
    with open(file_name, "r") as data_file:
        data: str = json.load(data_file)
        return data