#!/usr/bin/env python3

# 6. Write a Python program that creates a list. One of the elements of the list should be a 
#    dictionary with at least two keys. Write this list out to a file using both YAML and JSON 
#    formats. The YAML file should be in the expanded form.

import yaml
import json

def main():

    yaml_file = 'my_yaml.yml'
    json_file = 'my_json.json'
    
    # create a dict
    my_dict = {
        'vendor': 'HP',
        'model': 'Precision',
        'os': 'Windows 7',
        'ip_addr': '10.0.0.15'
    }
        
    # create a list
    my_list = [
        1,
        2,
        3,
        4,
        'hello',
        my_dict,
        'goodbye'
    ]

    with open("yaml_file", "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open("json_file", "w") as f:
        f.write

if __name__ == "__main__":
    main()

