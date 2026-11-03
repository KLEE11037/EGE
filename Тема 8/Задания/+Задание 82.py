from itertools import product

i = 1
for p in product('АКОРСТ', repeat=5):
    line = ''.join(p)

    if line[0] != 'А' and line[0] != 'С' and line[0] != 'Т' and line.count('О') == 2:
        if i%2==0:
            print(i)
    i+=1

answer = 5058

#

from tests.conftest import result_register

if answer is not Ellipsis:
    print(result_register(8, 82, answer, '7ffb4e0ece07869880d51662a2234143'))
