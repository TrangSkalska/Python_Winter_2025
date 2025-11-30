for i in range(2, 10, 2): # start at 2 and go until 10 with a step of 2
    #print(i)
    print(i, end='\t')
print('\n--------')
for i in reversed(range(10)):
    print(i, end='\t')

print('\n--------')
li = [33, 67, 47 ]
for el in li:
    print(el, end='\t')

print('\n--------')

j = 0
summ = 0
while j < len(li):
    summ = summ + li[j]
    print(summ, end='\t')
    j = j + 1  # j += 1
#print(summ)
print('\n--------')

j = 0
while j < 10:
    j += 1
    if j % 2 == 0:
        continue
    if j >= 8:
        break
    print(j, end='\t')