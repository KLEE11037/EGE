count = 0
for row in open('Пример 3.CSV'):
    row = list(map(int, row.split()))
    repeats = [row.count(n) for n in row]
    repeated = [n for n in row if row.count(n) > 1]
    not_repeated = [n for n in row if row.count(n) == 1]