#s = "hello world it's Wednesday 29th October"
s = 'hello world it\'s Wednesday 29th October'
print(f's="{s}"')
print(f's1="{s[6:]}"')
print(f's1="{s[:11]}"')
print(f's1="{s[6:11]}"')
s2 = s[6:11] + ' on' + s[16:26]
print(f's2={s2}')
a = 636
s3 = '{}={}'.format(a, a)
print(f's3={s3}')
s4 = f'a={a}'
print(f's4={s4}')

s_m = """
hello world it's Wednesday 29th October
2nd line
"""
#print(f's_m="{s_m}"')

s_m1 = 'hello \t\tworld \nit\'s Wednesday \n29th \t\tOctober'
print(s_m1)

o_a = ord('a')
print(f'o_a={o_a}')

o_A = ord('A')
print(f'o_A={o_A}')

o_L = ord('ż')
print(f'o_L={o_L}')

c = chr(97)
print(f'c={c}')

print('------------------')


print('------------------')
s_m2 = r'hello \t\tworld \nit\'s Wednesday \n29th \t\tOctober'
s_m2 = 'hello \t\tworld \nit\'s Wednesday \n29th October'
print(s_m2)

ll_i = s_m2.find('lll')
#ll_i = s_m2.index('lll')
print(f'll_i={ll_i}')
lines = s_m2.split('\n')
print(f'lines={lines}')
i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}')

print('-------------')
print(lines[2])
print('------')

print(lines[1])
print('hhtejejewjwej')

print('---------')
print(lines)
one_line = ' |||||| '.join(lines)
print(one_line)

print('---------')
li = [34535, 64637, 437 ]
print(li)
print(li[0])
print(li[1])

sli = [ str(x) for x in li ]
print(sli)
print(' | '.join(sli))