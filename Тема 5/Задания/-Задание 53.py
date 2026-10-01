def to_ternare (num,base):
    res = ''
    while num>0:
        res += str(num % base)
        num//=base
    return res[::-1]

answer = 0
for n in range(1,10000):
    ternare_n = str(to_ternare(n,3))
    if n%3==0:
        r = '1' + ternare_n + '02'
    else:
        r = ternare_n + to_ternare(n%3*4,3)
    result = int(r,3)


    if result > 250:
        print(n)
        answer = n
        break







#answer = 

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 53, answer, '4e732ced3463d06de0ca9a15b6153677'))