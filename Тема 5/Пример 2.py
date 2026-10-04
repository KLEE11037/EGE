"""
for n in range(10, 1000):
    b = bin(n)[2:]
    b += bin(n % 4)[2:]
    print(n, int(b, 2), int(b, 2) // n)
"""
count = 0
for n in range(1000000000, 1789456123+1, 2):
    if (n % 2 == 0 and n % 4 != 0) or (n % 4 == 0):
        count += 1
print(count)