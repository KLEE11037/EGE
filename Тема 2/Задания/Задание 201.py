# Решение
print ('x y z w f1 f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y))==(w<=z)
                f2 = (x or not(y))<=(w==z)
                print(x,y,z,w,int(f1),int(f2))







answer = ...

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(2, 201, answer, '7379de4777f5748aa568b8d0bf8c3795'))