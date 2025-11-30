def sum_it(a=10, b=60):
    r = a + b
    d = 1000
    return r

a1 = 141
b1 = 20
print(sum_it(a1, b1))
#print(f'd={d}')


if a1 > b1:
    print(a1)
    c = 100
else:
    print(b1)
    #c = 10

print(f'c={c}')

s1 = sum_it(a=435, b=78)
print(f's1={s1}')

def sum_and_multiply(a=10, b=60):
    s = a + b
    m = a * b
    return s, m

res_s, res_m = sum_and_multiply(a=6, b=5)
print(f'res_s={res_s}')
print(f'res_m={res_m}')
print('----------')
res = sum_and_multiply(a=6, b=5)
print(f'res={res}')
print(f'res_1={res[1]}')
print(f'type(res)={type(res)}')