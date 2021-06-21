from netmiko import ConnectHandler
from getpass import getpass

device = ConnectHandler(device_type='cisco_ios', ip=input("Please provide IP Address: "),username=input("Please provide Username: "),
                        password=getpass("Please provide Password"), secret=getpass("Please Provide Secret: "))
output = device.send_command('show ip int brief')

print(output)