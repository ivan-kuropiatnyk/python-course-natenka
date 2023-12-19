'''
Python for network engineers Natasha Samoilenko
'''
# Page range 156
#task 6.2a
ip_address = input("Enter ip address in a format 10.1.1.1: ")
#ip_address = "256.1.1.1"
try:
    ip_list = list(ip_address.split("."))
    for ip in ip_list:
        ip = int(ip)
        if ip > 255:
            raise ValueError
        elif ip < 0:
            raise ValueError
        else:
            ip_list = list(ip_address.split("."))
            ip_1oct = int(ip_list[0])
            ip_2oct = int(ip_list[1])
            ip_3oct = int(ip_list[2])
            ip_4oct = int(ip_list[3])
            unicast = "unicast"
            multicast = "multicast"
            local_broadcast = "local broadcast"
            unassigned = "unassigned"
            unused = "unused"
            if ip_1oct in range(1, 224):
                print(f"IP address {ip_address} is {unicast}")
                break
            elif ip_1oct in range(224, 240):
                print(f"IP address {ip_address} is {multicast}")
                break
            elif ip_1oct == 255 and ip_2oct == 255 and ip_3oct == 255 and ip_4oct == 255:
                print(f"IP address {ip_address} is {local_broadcast}")
                break
            elif ip_1oct == 0 and ip_2oct == 0 and ip_3oct == 0 and ip_4oct == 0:
                print(f"IP address {ip_address} is {unassigned}")
                break
            else:
                print(f"IP address {ip_address} is {unused}")
                break
except ValueError:
    print("Неправильный IP-адрес")


