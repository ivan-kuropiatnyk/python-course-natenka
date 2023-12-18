# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 23. Специальные методы
# Методы __str__, __repr__
# page609 -610
class IPAddress:
    def __init__(self, ip):
        self.ip = ip
ip1 = IPAddress('10.1.1.1')
ip2 = IPAddress('10.2.2.2')
#После создания экземпляров класса, у них есть строковое представление по умолчанию,
print("\nString 1:\n", str(ip1))
print("String 2:\n", str(ip2))
'''
было бы лучше, если бы отоб-
ражалась информация о том, какой именно адрес представляет этот экземпляр. За отобра-
жение информации при применении функции str, отвечает специальный метод __str__ - как
аргумент метод ожидает только экземпляр и должен возвращать строку
'''
class IPAddressForStr:
    def __init__(self, ip):
        self.ip = ip
    def __str__(self):
        return f"IPAddressForStr: {self.ip}"
ip1ForStr = IPAddressForStr('10.1.1.1')
ip2ForStr = IPAddressForStr('10.2.2.2')
print("\nString 3:\n", str(ip1ForStr))
print("String 4:\n", str(ip2ForStr))

"""
Второе строковое представление, которое используется в объектах Python, отображается
при использовании функции repr, а также при добавлении объектов в контейнеры типа спис-
ков:
"""
ip_addresses = [ip1ForStr, ip2ForStr]
print("\nREPR LIST:\n", ip_addresses)
print("REPR 1:\n", repr(ip1ForStr))
print("REPR 2:\n", repr(ip2ForStr))
"""
За это отображение отвечает метод __repr__, он тоже должен возвращать строку, но при этом
принято, чтобы метод возвращал строку, скопировав которую, можно получить экземпляр
класса:
"""
class IPAddressForRepr:
    def __init__(self, ip):
        self.ip = ip
    def __str__(self):
        return f"IPAddressForRepr: {self.ip}"
    def __repr__(self):
        return f"IPAddressForRepr('{self.ip}')"
ip1ForRepr = IPAddressForRepr('10.1.1.1')
ip2ForRepr = IPAddressForRepr('10.2.2.2')
ip_addressesForRepr = [ip1ForRepr, ip2ForRepr]
print("\nREPR LIST2:\n", ip_addressesForRepr)
print("REPR IP1:\n", repr(ip1ForRepr))
print("REPR IP2:\n", repr(ip1ForRepr))