#!/usr/bin/python3
"""
    5-save_to_json_file: save_to_json_file()
"""


import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file using JSON rep.
        Args:
            my_obj (object): object to be serialized.
            filename (str): name of file where string is stored.
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)


filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': ["San Francisco", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = {132, 3}
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
