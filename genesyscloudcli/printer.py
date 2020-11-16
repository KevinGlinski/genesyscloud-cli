import json
import yaml
import configuration

def print_data(data):
    config = configuration.Configuration()
    if config.output_type == 'yaml':
        print_yaml(data)
    else:
        print_json(data)

def print_json(data):
    print(json.dumps(data, indent=3))

def print_yaml(data):
    print(yaml.dump(data))
