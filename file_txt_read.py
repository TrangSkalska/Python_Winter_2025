import os

my_file = 'data\\my_data.txt'
#my_file = 'C:\\Users\\prubac\\PycharmProjects\\Python_Winter_2025_Wed_950\\data\\my_data.txt'
#my_file = '..\\..\\..\\..\\Temp\\my_data.txt'
#my_file = 'C:\\Temp\\my_data.txt'

print(f'cwd={os.getcwd()}')

f = open(my_file, 'r')
i = 0
for line in f:
    i = i + 1
    print(f'{i}: {line}', end='')
f.close()

print('-----------')

with open(my_file, 'r') as f:
    i = 0
    for line in f:
        i = i + 1
        print(f'{i}: {line}', end='')