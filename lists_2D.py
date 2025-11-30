l1 = [1, 2, 3, 0] # - list
l2 = [4, 5, 6, 9]
l3 = [7, 8, 9, 0]

l2D = [l1, l2, l3]
print(l2D)
print(l2D[1][2])

print('------')
for row in l2D:
    #print(row)
    for el in row:
        print(el, end='\t')
    print()

#TODO - create functions to
# sum_rows of a 2D list,
# sum_cols of a 2D list,
# sum all values

#1 exercise
def sum_rows(matrix):
    return [sum(row) for row in matrix]

row_sums = sum_rows(l2D)
print("Row sums:", row_sums)

#2 exercise
def sum_cols(matrix):
    return [sum(col) for col in zip(*matrix)]

col_sums = sum_cols(l2D)
print("Col sums:", col_sums)

#3 exercise

def sum_all(matrix):
    return sum(sum(row) for row in matrix)

all_sums = sum_all(l2D)
print("All sums:", all_sums)

