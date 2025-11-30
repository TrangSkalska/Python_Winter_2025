import json

l1 = [1, 2, 3, 0] # - list
l2 = [4, 5, 6, 9]
l3 = [7, 8, 9, 0]

l2D = [l1, l2, l3]

my_file = 'data/my_file.json'

with open(my_file, 'w') as f:
    json.dump(l2D, f)

