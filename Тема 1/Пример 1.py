from itertools import permutations

table = '14 17 18 23 25 26 32 34 38 41 43 47 48 52 56 58 62 65 71 74 81 83 84 85'
graph = 'АБ БА БВ ВБ ВГ ГВ ГД ДГ ДЕ ЕД ЕЖ ЖЕ ЖИ ИЖ АИ ИА ИБ БИ БЖ ЖБ ЖВ ВЖ ГЕ ЕГ'

for p in permutations('АБВГДЕЖИ'):
    new_graph = table
    for i in range(1,9):
        new_graph = new_graph.replace(str(i), p[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(p)