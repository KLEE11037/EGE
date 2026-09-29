for n in range(1, 10000):
    b = bin(n)[2:]
    b_inv = b.replace('0','2').replace('1','0').replace('2','1').lstrip('0')
    count_ones_even = 0
    for i in range(0, len(b_inv),2):
        if b_inv[i]=='1':
            count_ones_even+=1
    count_zeros_odd = 0
    for i in range(1,len(b_inv),2):
        if b_inv[i] =='0':
         count_zeros_odd+=1
    r = abs(count_ones_even - count_zeros_odd)
    if r ==5:
        print(n)
        break
# Решение







answer = 512

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 52, answer, 'ce5140df15d046a66883807d18d0264b'))