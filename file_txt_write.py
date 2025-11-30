import tempfile

my_file = 'data\\my_data.txt'

#with open(my_file, 'a') as f: # a - append at the end
with open(my_file, 'w') as f:  # w - overwrite
    f.write('hello world')
    f.write('\n')
    f.write('2nd line\n')
    f.flush()
    f.write('3rd line\n')

my_temp_file = tempfile.NamedTemporaryFile()
with open(my_temp_file.name, 'w') as f:
    f.write('hello world')
print(my_temp_file.name)