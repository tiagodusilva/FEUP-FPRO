def remove_leading(ip):
    ips = ip.split(".")
    for i in range(len(ips)):
        ips[i] = str(int(ips[i]))
    return ".".join(ips)


#print(remove_leading("255.024.01.01"))
#print(remove_leading("192.168.0.24"))
