print('x y z w u')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                for u in range(2):
                    f = ((x<=y) and (z == (not w))) <= (u == (x or z))
                    if f == 0:
                        print(x,y,z,w,u,int(f))





answer = 'xzywu'

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 203, answer, 'b83215ff76ddd410e32571919b78d0eb'))