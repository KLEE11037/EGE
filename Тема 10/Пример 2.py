from ipaddress import ip_network

net = ip_network('192.168.32.160/255.255.255.240', False)

count = 0
for ip in net:
    if f'{ip:b}'.count('1')%2 ==0:
        count+=1
print(count)