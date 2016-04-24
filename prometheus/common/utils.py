import json

UNKNOWN_VALUE = "Unknown"
MISSING_VALUE = "Missing"


def get_data_from_multi_json_file(file_path):
    with open(file_path) as f:
        return [json.loads(line) for line in f]


def soft_wrangle_data(data_set):
    """ Receive a panda Series object and substitute None values for 'Missing' and empty values for 'Unknown' """
    data_set.fillna(MISSING_VALUE)
    data_set.loc[data_set == ""] = UNKNOWN_VALUE
    return data_set
