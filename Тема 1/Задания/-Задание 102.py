# Решение
from itertools import permutations
table = '13 14 16 23 24 27 28 31 32 34 38 41 42 43 46 56 57 58 61 64 65 67 72 75 76 78 82 83 85 87'
graph = 'АБ БА БИ ИБ ИЖ ЖИ ЖА АЖ АГ ГА ГЖ ЖГ ЖЕ ЕЖ ЕИ ИЕ ИД ДИ ДБ БД БВ ВБ ВД ДВ ДЕ ЕД ЕГ ГЕ ВА АВ'

for p in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(1,9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)




answer = 8


#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(1, 102, answer, 'aab3238922bcc25a6f606eb525ffdc56'))