a = 10
b = a % 5
print(a)
print(b)
if a % 2 == 0:
    print('even')
else:
    print('odd')

if a > 8:
    print('greater than 8')
elif a > 2:
    print('greater than 2')
else:
    print('less or equal than 2')

print('----------')
match a:
    case 8:
        print('eq 8')
    case 2:
        print('eq 2')
    case _:  # default case - matches everything left
        print('not eq 2 or 8')

s1 = 'abc'
s2 = 'a' + 'bc'
if s1 == s2:
    print('equal')
else:
    print('not equal')

if s1 != s2:
    print('not equal')