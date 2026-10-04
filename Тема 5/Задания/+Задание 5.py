for n in range(1,10000):
    r = bin(n)[2:]
    r = r.replace('0','2').replace('1','0').replace('2','1').lstrip('0')
    if r =='':
        r = '0'
    r = int(r,2)
    if n - r ==999:
        print(n)
        break







answer = 1011

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 5, answer, '7f975a56c761db6506eca0b37ce6ec87'))