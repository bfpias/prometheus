import json


def get_data_from_multi_json_file(file_path):
    with open(file_path) as f:
        return [json.loads(line) for line in f]
