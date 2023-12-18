# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 23. Специальные методы
# Протоколы
# page614-626
#Протокол итерации
class Items:
	def __init__(self, items):
		self.items = items
	def __getitem__(self, index):
		print('Вызываю __getitem__')
		return self.items[index]
iterable_1 = Items([1, 2, 3, 4])
print(iterable_1[0])
for i in iterable_1:
    print(i)
print(list(map(str, iterable_1)))

class Items2:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        print('Вызываю __getitem2__')
        return self.items[index]
    def __iter__(self):
        print('Вызываю __iter2__')
        return iter(self.items)
iterable2_1 = Items2([1, 2, 3, 4])
print(iterable2_1[0])
for i in iterable2_1:
    print(i)
print("LIST ITER2",list(map(str, iterable2_1)))

def my_for(iterable):
    if getattr(iterable, "__iter__", None):
        print('Есть __iter__ MY_FOR')
        iterator = iter(iterable)
        while True:
            try:
                print(next(iterator))
            except StopIteration:
                break
    elif getattr(iterable, "__getitem__", None):
        print('Нет __iter__ MY_FOR, но есть __getitem__ MY_FOR')
        index = 0
        while True:
            try:
                print(iterable[index])
                index += 1
            except IndexError:
                break
print("\nMY_FOR проверка:\n", my_for([1, 2, 3, 4]))

#Создание итератора
#Пример создания экземпляра класса Network:
import ipaddress
class NetworkBezIter:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
BezIter_net1 = NetworkBezIter('10.1.1.192/30')
print("\nBezIter IP+Mask = ", BezIter_net1)
print("BezIter IP = ",BezIter_net1.addresses)
print("BezIter Mask = ",BezIter_net1.network, "\n")

#Создаем итератор из класса Network:
class Network:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
        self._index = 0
    def __iter__(self):
        print('Вызываю __iter__')
        return self
    def __next__(self):
        print('Вызываю __next__')
        if self._index < len(self.addresses):
            current_address = self.addresses[self._index]
            self._index += 1
            return current_address
        else:
            raise StopIteration
net1 = Network('10.1.1.192/30')
for ip in net1:
    print(ip)

#Создание итерируемого объекта
class NetworkItarable:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
    def __iter__(self):
        return iter(self.addresses)
net1 = NetworkItarable('10.1.3.192/30')
for ip in net1:
    print(ip)

#Протокол последовательности
'''
В самом базовом варианте, протокол последовательности (sequence) включает два мето-
да: __len__ и __getitem__. В более полном варианте также методы: __contains__, __iter__,
__reversed__, index и count. Если последовательность изменяема, добавляются еще несколько
методов.
Добавим методы __len__ и __getitem__ к классу Network:
'''
class NetworkSeq:
    def __init__(self, network):
        self.network = network
        subnet = ipaddress.ip_network(self.network)
        self.addresses = [str(ip) for ip in subnet.hosts()]
    def __iter__(self):
        return iter(self.addresses)
    def __len__(self):
        return len(self.addresses)
    def __getitem__(self, index):
        return self.addresses[index]
netSeq1 = NetworkSeq('10.1.4.192/30')
print(len(netSeq1))
print(netSeq1[0])
print(netSeq1[1])
netSeq2 = NetworkSeq('10.1.5.192/28')
print(netSeq2[0])
print(netSeq2[3:7])
print(netSeq2[3:])
#print(netSeq2[100])


#Менеджер контекста
'''
Менеджер контекста позволяет выполнять указанные действия в начале и в конце блока with.
За работу менеджера контекста отвечают два метода:
• __enter__(self) - указывает, что надо сделать в начале блока with. Значение, которое
возвращает метод, присваивается переменной после as.
• __exit__(self, exc_type, exc_value, traceback) - указывает, что надо сделать в
конце блока with или при его прерывании. Если внутри блока возникло исключение,
exc_type, exc_value, traceback будут содержать информацию об исключении, если ис-
ключения не было, они будут равны None.
Примеры использования менеджера контекста:
• открытие/закрытие файла
• открытие/закрытие сессии SSH/Telnet
• работа с транзакциями в БД
'''
#Для того чтобы класс поддерживал работу в менеджере контекста, надо добавить методы
#__enter__ и __exit__:
import time
import paramiko
class CiscoSSH:
    def __init__(self, ip, username, password, enable, disable_paging=True):
        print('Метод __init__')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False)
        self.ssh = client.invoke_shell()
        self.ssh.send('enable\n')
        self.ssh.send(enable + '\n')
        if disable_paging:
            self.ssh.send('terminal length 0\n')
        time.sleep(1)
        self.ssh.recv(1000)
    def __enter__(self):
        print('Метод __enter__')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('Метод __exit__')
        self.ssh.close()
    def send_show_command(self, command):
        self.ssh.send(command + '\n')
        time.sleep(2)
        result = self.ssh.recv(5000).decode('ascii')
        return result

#Проверяем
with CiscoSSH('172.17.20.41', 'ivankurop', 'qweszxc', 'qweszxc') as r1:
    print(r1.send_show_command('sh clock'))

with CiscoSSH('172.17.20.41', 'ivankurop', 'qweszxc', 'qweszxc') as r1:
    print(r1.send_show_command('sh bclock'))