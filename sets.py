l1 = [3, 1, 2] # - list
l2 = [4, 5, 6]
#l2 = [4, 5, 6]
l2a = [str(x)+'a' for x in l2]

l3 = l1 + l2a
print(l3)
print('-------')
for x in l3:
    if type(x) == str:
        print(x)

print('-------')

l4 = l1 + l1 + [1]
print(l4)
print(sorted(l4))
print(sorted(l4, reverse=True))
print('--------')
s4 = set(l4)
print(s4)
l5 = list(s4)
print(l5)