import json


def write_to_json(path: str, file_name: str, data: json):
    file_path = './' + path + '/' + file_name

    with open(file_path, 'w') as file:
        json.dump(data, file)


def read_json_file(file_name: str):
    json_file = open(file_name, 'r')
    json_data = json_file.read()

    # parse
    return json.loads(json_data)
