from itertools import permutations

for p in permutations('ABCDEFGH'):
    print(''.join(p))