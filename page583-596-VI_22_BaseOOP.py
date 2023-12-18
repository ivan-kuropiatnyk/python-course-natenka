'''
Python for network engineers Natasha Samoilenko
'''
# Page range 583-596
# VI - OOP
# 22 Основы OOP
# 22.1 Основы ООП
'''
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
ssh = ConnectHandler(**device)
print(type(ssh))
ssh.host
ssh.send_command("sh clock")
'''
s = 'string'
s.upper()
s.center(20, '=')
print(type(s))

# 22.2 Создание класса
class Switch:
    pass
sw1 = Switch()
print(sw1)
print(type(sw1))
print(type(Switch))
sw1.hostname = 'sw1'
sw1.model = 'Cisco 3850'

sw2 = Switch()
sw2.hostname = 'sw2'
sw2.model = 'Cisco 3750'
print(sw2.hostname)
print(type(sw2.hostname))
print(sw2.model)
print(type(sw2.model))
print(type(sw2))

# 22.3 Создание метода
class Switch:
    #pass
    def info(self, sw_obj):
        print('Hostname: {}\nModel: {}'.format(sw_obj.hostname, sw_obj.model))
sw1 = Switch()
sw1.hostname = 'sw1'
sw1.model = 'Cisco 3850'
#print(sw1.info())
#print(Switch.info(sw1))

a = [1,2,3]
a.append(4)
print(a)
list.append(a, 5)
print(a)

# 22.4 Параметр self
class Switch:
    def info(sw_object):
        print(f'Hostname: {sw_object.hostname}\nModel: {sw_object.model}')
sw1 = Switch()
sw1.hostname = 'sw1'
sw1.model = 'Cisco 3850'
print(sw1.info())

###Для начала, вариант создания обычно переменной внутри метода:
class Switch:
    def generate_interfaces(self, intf_type, number_of_intf):
        interfaces = [f"{intf_type}{number}" for number in range(1, number_of_intf + 1)]
sw1 = Switch()
sw1.generate_interfaces('Fa', 10)
#print(sw1.interfaces)#error
### Этой переменной нет, потому что она существует только внутри метода, а область видимости
### у метода такая же, как и у функции. Даже другие методы одного и того же класса, не видят
### переменные в других методах.
### Чтобы список с интерфейсами был доступен как переменная в экземплярах, надо присвоить
### значение в self.interfaces:
class Switch:
    def info(self):
        print(f"Hostname: {self.hostname}\nModel: {self.model}")

    def generate_interfaces(self, intf_type, number_of_intf):
        interfaces = [f"{intf_type}{number}" for number in range(1, number_of_intf + 1)]
        self.interfaces = interfaces
### Теперь, после вызова метода generate_interfaces, в экземпляре создается
### переменная interfaces:
sw3 = Switch()
sw3.generate_interfaces('Fa', 10)
print(sw3.interfaces)

# 22.5 Метод __init__
### В Python эти начальные данные про объект указываются в методе __init__. Метод __init__
### выполняется после того как Python создал новый экземпляр и, при этом, методу __init__
### передаются аргументы с которыми был создан экземпляр:
class SwitchInitExampleClass:
    def __init__(self, hostname, model):
        self.hostname = hostname
        self.model = model

    def info(self):#Это метод класса
        print(f'Hostname: {self.hostname}\nModel: {self.model}')
### Теперь, при создании экземпляра класса Switch, обязательно надо указать hostname и model:
sw1 = SwitchInitExampleClass('sw1', 'CiscoKisko 3850')
print(sw1.info())
### Метод __init__ иногда называют конструктором класса, хотя технически в
### Python сначала выполняется метод __new__, а затем __init__. В большинстве случаев, метод
### __new__ использовать не нужно.
### Важной особенностью метода __init__ является то, что он не должен ничего возвращать.

# 22.6 Пример класса
# Пример класса, который описывает сеть:
import ipaddress
class Network:
    def __init__(self, network):
        self.network = network
        self.hosts = tuple(str(ip) for ip in ipaddress.ip_network(network).hosts())
        self.allocated = []

    def allocate(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
            else:
                raise ValueError(f"IP-адрес {ip} уже находится в allocated")
        else:
            raise ValueError(f"IP-адрес {ip} не входит в сеть {self.network}")
#Использование класса:
net1 = Network("10.1.1.0/29")
net1.allocate("10.1.1.1")
net1.allocate("10.1.1.2")
print(net1.allocated)
#net1.allocate("10.1.1.100")#ValueError: IP-адрес 10.1.1.100 не входит в сеть 10.1.1.0/29

# 22.7 Область видимости
'''
У каждого метода в классе своя локальная область видимости. Это значит, что один метод
класса не видит переменные другого метода класса. Для того чтобы переменные были до-
ступны, надо присваивать их экземпляру через self.name. По сути метод - это функция при-
вязанная к объекту. Поэтому все нюансы, которые касаются функций, относятся и к методам.
'''
class SwitchZoneSeen:
    def __init__(self, hostname, model):
        self.hostname = hostname
        self.model = model

    def info(self):
        print('Hostname: {}\nModel: {}'.format(self.hostname, self.model))
SW_22_7 = SwitchZoneSeen('SW_22_7', 'Model 22.7')
print(SW_22_7.info())

# 22.8 Переменные класса
class Network22_8:
    all_allocated_ip = []

    def __init__(self, network):
        self.network = network

        self.hosts = tuple(
            str(ip) for ip in ipaddress.ip_network(network).hosts()
        )
        self.allocated = []

    def allocate(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
                type(self).all_allocated_ip.append(ip)
            else:
                raise ValueError(f"IP-адрес {ip} уже находится в allocated")
        else:
            raise ValueError(f"IP-адрес {ip} не входит в сеть {self.network}")
'''
К переменным класса можно обращаться по-разному:
• self.all_allocated_ip #Минус -если в методе написать self.all_allocated_ip = ..., вместо изменения переменной класса, будет создана переменная экземпляра.
• Network.all_allocated_ip #Минус -имя класса прописано вручную.
• type(self).all_allocated_ip #Принято использовать этот
'''
#Теперь у класса есть переменная all_allocated_ip в которую записываются все IP-адреса, ко-
#торые выделены в сетях:
net1 = Network22_8("10.1.1.0/29")
net1.allocate("10.1.1.1")
net1.allocate("10.1.1.2")
net1.allocate("10.1.1.3")
print("net1_1", net1.allocated)
net2 = Network22_8("10.2.2.0/29")
net2.allocate("10.2.2.1")
net2.allocate("10.2.2.2")
print("net2_1", net2.allocated)

print("all_allocated_ip in class Network22_8 by Class\n", Network22_8.all_allocated_ip)

#Переменная доступна не только через класс, но и через экземпляры:
print("Network22_8.all_allocated_ip by E =>",Network22_8.all_allocated_ip)
print("net2_1 by E =>",net1.all_allocated_ip)
print("net2_1 by E =>",net2.all_allocated_ip)
