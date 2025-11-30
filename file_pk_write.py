import pickle

l1 = [1, 2, 3, 0] # - list
l2 = [4, 5, 6, 9]
l3 = [7, 8, 9, 0]

l2D = [l1, l2, l3]

my_file = 'data/my_file.pkl'

with open(my_file, 'wb') as f:
    pickle.dump(l2D, f)