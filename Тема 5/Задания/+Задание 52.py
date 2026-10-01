for n in range(1, 10000):
    b = bin(n)[2:]
    count_zeros_odd = 0
    count_ones_even = 0
    for i in range(len(b)):
        if (i+1)%2==0:
            if b[i]=='1':
                count_ones_even+=1
        else:
            if b[i] == '0':
                count_zeros_odd += 1


    r = abs(count_ones_even - count_zeros_odd)
    if r ==5:
        print(n)
        break
# Решение







answer = 1023

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))