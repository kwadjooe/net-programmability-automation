hostname = 'Router_1'
print(hostname)

banner = "\n\n AUTHORIZED ACCESS ONLY \n\n"
print(banner)

a = hostname.upper()

print(a)
vendors = ["cisco","juniper", "arista","hp"]

print(vendors[0])
print(vendors[1])
vendors.append("Palo Alto")
print("\n")
print(vendors, "\n")
facts = {"vendor":"cisco", "platform":"catalyst", "os":"ios"}

b = facts.items()
print(b)
print("\n", facts.keys())
print("\n", facts.values())
print("\n", facts, "\n")

ip_address = ("10.1.1.1", "24")

c = type(ip_address)

print("\n", c, "\n")

d = ip_address.__len__

print(d)
e = set(vendors)

print("\n", e)