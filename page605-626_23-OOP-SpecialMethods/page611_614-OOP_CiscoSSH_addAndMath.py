# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 23. Специальные методы
# Поддержка арифметических операторов
# page611 -614
'''
За поддержку арифметических операций также отвечают специальные методы, например,
за операцию сложения отвечает метод __add__:
__add__(self, other)
Добавим к классу IPAddress поддержку суммирования с числами, но чтобы не усложнять ре-
ализацию метода, воспользуемся возможностями модуля ipaddress
'''
import ipaddress

ipaddress1 = ipaddress.ip_address('10.1.1.1')
print("Integer IP=", int(ipaddress1))
print("IP from integer=", ipaddress.ip_address(167837953))


# here we create class IPAddress with support of __add__ method of ip addresses
class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"IPAddress: {self.ip}"

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __add__(self, other):
        ip_int = int(ipaddress.ip_address(self.ip))
        sum_ip_str = str(ipaddress.ip_address(ip_int + other))
        return IPAddress(sum_ip_str)
#Теперь экземпляры класса IPAddress должны поддерживать операцию сложения с числом. В
#результате мы получаем новый экземпляр класса IPAddress
ip1 = IPAddress('10.1.1.1')
print("ip1 + 5 = ", ip1 + 5)
print("ip1= ",ip1)


#Так как внутри метода используется модуль ipaddress, а он поддерживает создание IP-адреса
#только из десятичного числа, надо ограничить метод на работу только с данными типа int.
class IPAddressLimited:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f"IPAddress: {self.ip}"

    def __repr__(self):
        return f"IPAddress('{self.ip}')"

    def __add__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"unsupported operand type(s) for +:"
                            f" 'IPAddress' and '{type(other).__name__}'")
        ip_int = int(ipaddress.ip_address(self.ip))
        sum_ip_str = str(ipaddress.ip_address(ip_int + other))
        return IPAddressLimited(sum_ip_str)
ipLimited1 = IPAddressLimited('10.1.2.1')
print("ip1Limited + 5 = ", ipLimited1 + 5)
print("ip1Limited = ",ipLimited1)
print("ip1Limited + 5.0 = ", ipLimited1 + 5.0)
print("ip1Limited = ",ipLimited1)