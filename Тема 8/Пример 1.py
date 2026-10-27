from itertools import product
count = 0
for s in product('НИКОЛАЙ', repeat = 4):
    line = ''.join(s)
    if line[0] != 'Й':
        if any(x in line for x in 'ИОА'):
            count+= 1
print(count)
