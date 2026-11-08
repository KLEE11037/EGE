count = 0
for row in open('Пример 2.txt'):
    row = list(map(int, row.split()))
    repeats = [row.count(n) for n in row]
    repeated = [n for n in row if row.count(n) > 1]
    not_repeated = [n for n in row if row.count(n) == 1]
    """    
    for col in row:
        repeats.append(row.count(col))
        if row.count(col) > 1:
            repeated.append(col)
        else:
            not_repeated.append(col)
    """
    condition_1 = sorted(repeats)[-1] > 2
    condition_2 = sorted(repeats)[0] == 1
    condition_3 = False
    if len(repeated) > 0 and len(not_repeated) > 0:
        condition_3 = (sum(repeated) / len(repeated)) > (sum(not_repeated) / len(not_repeated))
    if condition_1 and condition_2 and condition_3:
        count += 1
print(count)