import pickle

my_file = 'data/my_file.pkl'

with open(my_file, 'rb') as f:
    data = pickle.load(f)
    print(data)
    print(data[1][3])