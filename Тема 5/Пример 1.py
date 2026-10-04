for n in range(100,1000):
    r = bin(n)[2:]
    for _ in range(3):
        if r.count('0')==r.count('1'):
            r = r + r[-1]
        elif r.count('0')<r.count('1'):
            r = r + '0'
        else:
            r = r + '1'
    R = int(r,2)

    if R%4==0:
        print(n,R)
        break