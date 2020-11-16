import json
import yaml
from tabulate import tabulate
import configuration

config = configuration.Configuration()

def print_name_id_data(data):
    """Prints only the name and ids from a list of objects"""
    name_ids = []
    for o in data:
        name_ids.append({
            "id": o['id'],
            "name": o['name']
        })

    print_data(name_ids)

def print_data(data):    
    if config.output_type == 'yaml':
        print_yaml(data)
    else:
        print_json(data)

def print_json(data):
    print(json.dumps(data, indent=3))

def print_yaml(data):
    print(yaml.dump(data))


def print_table(data, headers=[]):
    print(tabulate(data, headers=headers))
