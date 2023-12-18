# -*- coding: utf-8 -*-
"""
Задание 23.1
В этом задании необходимо создать класс IPAddress.
При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно
Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).
Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.
Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')
Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')
In [3]: ip1.ip
Out[3]: '10.1.1.1'
In [4]: ip1.mask
Out[4]: 24
Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address
Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask
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

    # Just Info section for troubleshooting
    def info(self):
        print(f"IP_Mask={self.ip_mask}")

if __name__ == "__main__":
    #ip1 = IPAdress("10.10.0.987/30")
    #ip1 = IPAdress("10.10.0./30")
    ip1 = IPAdress("10.10.0.A/30")
    print("IP = ", ip1.ip)
    print("Mask = ", ip1.mask)
    print("IP/Mask = ", ip1.ip_mask)