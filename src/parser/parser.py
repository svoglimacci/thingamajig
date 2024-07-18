import json


def parse(data):

    # parse json data in a readable format
    parsed_data = json.dumps(data, indent=4)

    return parsed_data
