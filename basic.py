# device provisioning - automate devices configuration files

def greeting(name):
    print("Hello", name)

greeting(input("What is your name: \n"))


if_name = input("Please provide the interface name: \n")

if_name = if_name.lower()

print(if_name)

# ip_addr = '10.1.10.254'
# vrf = 'lab'

# ping = 'ping {} vrf {} '.format(ip_addr, vrf)
# print(ping)

ip_addr = input("Please provide the IP Address: \n")
vrf = input("Please provide the VRF name: \n")
ping = "ping {} vrf {}"
tracer = "traceroute {} vrf {}"
ping_command = ping.format(ip_addr, vrf)
tracer_command = tracer.format(ip_addr, vrf)
print(ping_command)
print(tracer_command)

# ping = 'ping' + ' ' + ip_addr + ' ' + 'vrf' + vrf

hostnames = ["X1", "X2", "X3", "X4", "X66"]

for devices in hostnames:
    print(devices)

print(ip_addr.startswith('10'))
print(ip_addr.startswith('192'))
print(ip_addr.endswith('254'))
print(ip_addr.split('.'))

a = int(input("How old are you ? \n"))

print(a)

print(ip_addr.isdigit())

first_octet = '01101101'
print(first_octet.count('1'))
print(first_octet.count('0'))



