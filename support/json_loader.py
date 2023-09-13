import json


def json_load(path):
    with open(path, 'r') as file:
        json_content = json.load(file)
    return json_content
