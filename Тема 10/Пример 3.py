from ipaddress import ip_network, ip_address

for mask_len in range(32,0,-1):
    net = ip_network(f'145.46.8.250/{mask_len}', False)
    if net.network_address==ip_address('145.46.0.0'):
        max_count = 0
        for ip in net.hosts():
            max_count = max(max_count,f'{ip:b}'.count('1'))
        print(max_count23)
