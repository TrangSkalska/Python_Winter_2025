import json

my_file = 'data/my_file.json'

with open(my_file, 'r') as f:
    data = json.load(f)
    print(data)
    print(data[1][3])