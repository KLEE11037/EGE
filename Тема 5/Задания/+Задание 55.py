def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


c = set()
for n in range(1, 100):
    s = f(n)
    if n % 3 == 0:
        s = s + s[-2:]
    else:
        s = s + f((n % 3) * 5)
    r = int(s, 3)
    if r <= 173:
        c.add(r)
print(max(c))









answer = 162

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(5, 55, answer, '82aa4b0af34c2313a562076992e50aa3'))