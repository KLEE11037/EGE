for n in range(1,10000):
    r = bin(n)[2:]
    r_inv = ''
    for c in r:
        if c == '0':
            r_inv+='1'
        else:
            r_inv+='0'
    r_inv = r_inv.lstrip('0')
    if r_inv =='':
        r_inv = '0'
    r = int(r_inv,2)
    if n - r ==999:
        print(n)
        break







answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))