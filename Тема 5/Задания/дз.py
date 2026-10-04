def even (i):
    if i%2==0:
        return True
    else:
        return False

count_ones_even = 0
count_zeros_odd = 0

n = 99
b = bin(n)[2:]
print(b)
for i in range (len(b)):
    if even(i+1):
        if b[i]=='1':
            count_ones_even+=1
    else:
        if b[i]=='0':
            count_zeros_odd+=1
print(count_ones_even, count_zeros_odd)





print(even(5))
print(even(2))
print(even(0))