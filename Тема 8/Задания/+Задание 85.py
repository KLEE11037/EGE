from itertools import product

i = 1
for p in product('АГМНСТУ', repeat = 6):
    line = ''.join(p)

    if line[0] != 'У' and line.count('М') == 2 and line.count('Г')<=1:
        print(i)
    i+=1







answer = 100810

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 85, answer, '4f41663a6f277ab55c6b626aff28784a'))