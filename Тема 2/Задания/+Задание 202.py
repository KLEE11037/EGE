print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x==y)<=(not(z) or w))==(not((w<=x)or(y<=z)))
                if f==1:
                    print(x,y,z,w,int(f))







answer = 'wzyx'


#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 202, answer, 'e0abee87e4ba1de22c6b8cf076c5016b'))