p = False
q = False

if p:   # if p==True:
    print('p')
if q==True:
    print('q')
print(f'p={p}')
print(f'q={q}')

print('---------')
if p and q:
    print('p and q')
else:
    print('not p or not q')

print('---------')
if p or q:
    print('p or q')
else:
    print('not p and not q')

print('---------')
if p and not q:
    print('p and not q')
else:
    print('not (p and not q)')
print('---------')

if p ^ q:  # XOR
    print('p XOR q')
else:
    print('not p XOR q')