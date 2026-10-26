from itertools import product
count = 0
for s in product('ГЕПАРД', repeat = 5):
    line = ''.join(s)
    if line[0] != 'А' and line[-1] != 'Е' and line.count('Г') == 1:
        count+= 1
print(count)







answer = 2200

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(8, 8, answer, '5249ee8e0cff02ad6b4cc0ee0e50b7d1'))