# -*- coding: utf-8 -*-
"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
import ipaddress

class IPAdress:
    def __init__(self, ip_mask):
        ip, mask = ip_mask.rstrip().lstrip().split("/")
        self.ip = ip
        self.mask = mask
        self.ip_mask = ip_mask

        #MASK VERIFICATION Section
        if self.mask:
            if self.mask.isdigit() and int(self.mask) in range(8, 33):
                pass
            else:
                raise ValueError ("Incorrect Net Mask")
        else:
            raise ValueError("Incorrect Net Mask")

        # IP VERIFICATION Section
        if self.ip:
            oct1, oct2, oct3, oct4 = (self.ip).split(".")
            list_oct = [oct1, oct2, oct3, oct4]
            for oct in list_oct:
                if oct.isdigit() and int(oct) in range(256):
                    pass
                else:
                    raise ValueError("Incorrect IP address")
        else:
            raise ValueError("Incorrect IP address")

    def __str__(self):
        return f"IPAdress: {self.ip_mask}"
    def __repr__(self):
        return f"IPAdress(\"{self.ip_mask}\")"

    # Just Info section for troubleshooting
    def info(self):
        print(f"IP_Mask={self.ip_mask}")

if __name__ == "__main__":
    ip1 = IPAdress("10.10.0.255/32")
    print("IP/Mask = ", ip1.ip_mask)
    print("IP = ", ip1.ip)
    print("Mask = ", ip1.mask)
    print("STR = ", str(ip1))
    print("REPR = ", repr(ip1))