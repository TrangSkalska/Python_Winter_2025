#my_folder = '.venv'
import os.path

#my_folder = 'data'
my_folder = '.venv'

def compute_folder_size(my_folder):
    # with the content
    size = 0
    for f in os.listdir(my_folder):
        f_path = os.path.join(my_folder, f)
        if os.path.isfile(f_path):
            size += os.path.getsize(f_path)
        elif os.path.isdir(f_path):
            size += compute_folder_size(f_path)
    return size


    # os.path.isdir(my_folder) # if it is a directory
    # os.path.isfile(my_folder) # if it is a regular file
    # os.path.getsize(my_folder) # get the size of a file
    # os.listdir(my_folder) # get a list of files and folders in a folder
    # return

print(f'size of folder "{my_folder}": {compute_folder_size(my_folder)}')