l1 = [1, 2, 3] # - list
l2 = [4, 5, 6]
l3 = (7, 8, 9) # - tuple

print(l1)
l1.append(4)
print(l1)
l1.insert(3, 1)  # - index, value
print(l1)
l1.remove(1) # - remove the value 1 - works once only
#l1.remove(1) # - remove the value 1 - works once only
print(l1)
l1.pop(2) # - remove at 3rd position
print(l1)

print('--------------')

l4 = ['Monday', 'Tuesday', 'Wednesday']
print(l4)
print(l4[2])

s1 = ' | '.join(l4)
print(s1)

l5 = s1.split('|')
print(f'l5={l5}')

l6 = []
for item in l5:
    l6.append(item.strip())  # strip() - cut off any whitespaces around
print(f'l6={l6}')

l7 = [ x.strip() for x in l5 if x.find('es') != -1 ]
print(f'l7={l7}')
#print(l1[1])
#print(l3[1])
#l3.append(10)
#print(l3)