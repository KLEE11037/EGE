from ipaddress import ip_network

print(ip_network(f'98.81.154.195/255.252.0.0', False)[-2])