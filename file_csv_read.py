import os

#my_file = '..\\..\\desktop\\rates.csv'
#my_file = 'data/rates.csv'
my_file = os.path.join('data', 'rates.csv')

with open(my_file, 'r') as f:
    i = 0
    for line in f:
        i = i + 1
        print(f'{i}: {line}', end='')

# How much is 100 EUR in PLN - practice at home

