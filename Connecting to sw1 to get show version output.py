from netmiko import ConnectHandler
from getpass import getpass

username = input("Please provide your username: ")
password = getpass("Please provide your password: ")
secret = getpass("Please provide your secret: ")
ip_addr = input("Please specifie the IP Address: ")

sw1 = {
    "device_type": "cisco_ios",
    "ip": ip_addr,
    "username": username,
    "password": password,
    "secret": secret
}
for device in (sw1):
    net_connect = ConnectHandler(**sw1)
    command = "show version"
    output = net_connect.send_command(command)

    print(output)