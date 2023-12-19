'''
Python for network engineers Natasha Samoilenko
'''
# Page range 215-243
# 9 - Функции


# создание функции
def configure_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)

# вызов функции:
# при этом результат функции нельзя сохранить в переменную
configure_intf('F0/0', '10.1.1.1', '255.255.255.0')
configure_intf('Fa0/1', '94.150.197.1', '255.255.255.248')
# Если же попытаться записать в переменную результат функции configure_intf, в переменной
# окажется значение None:
result = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
print(result)

# Чтобы функция могла возвращать какое-то значение, надо использовать оператор return.
# Оператор return
def configure_intf(intf_name, ip, mask):
    config = f'interface {intf_name}\nip address {ip} {mask}'
    return config
result = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
print(result)


# Функция может возвращать несколько значений. В этом случае, они пишутся через запятую
# после оператора return. При этом фактически функция возвращает кортеж:
def configure_intf(intf_name, ip, mask):
    '''
    Первая строка(docstring) функции где описывается, что она делает:
    Функция генерирует конфигурацию интерфейса
    '''
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip
result = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
print(result)
print(type(result))
intf, ip_addr = configure_intf('Fa0/0', '10.1.1.1', '255.255.255.0')
print(intf)
print(ip_addr)

# Локальные и глобальные переменные
# Пример ЛОКАЛЬНОЙ intf_config:
def configure_intf(intf_name, ip, mask):
    intf_config = f'interface {intf_name}\nip address {ip} {mask}'
    return intf_config

# print(intf_config)
###переменная intf_config недоступна за пределами функции. Для того
###чтобы получить результат функции, надо вызвать функцию и присвоить результат в пере
###менную:
result = configure_intf('F0/0', '10.1.1.1', '255.255.255.0')
print(result)

# Параметры и аргументы функций p224
##Параметры бывают обязательные и необязательные.
###Обязательные:
def f(a, b):
    pass


###Необязательные (со значением по умолчанию):
def f(a=None):
    pass


##Аргументы бывают позиционные и ключевые.
def summ(a, b):
    return a + b
###Позиционные:
summ(1, 2)
###Ключевые:
summ(a=1, b=2)


# Чтобы функция могла принимать входящие значения, ее нужно создать с параметрами
# обязательные параметры:
def check_passwd(username, password):
    if len(password) < 8:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
check_passwd('nata', '12345')
check_passwd('nata', '12345lsdkjflskfdjsnata')
check_passwd('nata', '12345lsdkjflskfdjs')


# Необязательные параметры:
def check_passwd(username, password, min_length=8):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
check_passwd('nata', '12345')
check_passwd('nata', '12345', 1)

# позиционные аргументы
check_passwd('nata', '12345lsdkjflskfdjsnata')
# ключевые аргументы
check_passwd(password='12345', username='nata', min_length=4)
# всегда сначала должны идти позиционные аргументы, а затем ключевые.
# Если сделать наоборот, возникнет ошибка:
# check_passwd(password='12345', username='nata', 4)
# Но в такой комбинации можно:
check_passwd('nata', '12345', min_length=3)


# Флаги (параметры со значениями True/False)
def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
check_passwd('nata', '12345nata', min_length=3)
check_passwd('nata', '12345nata', min_length=3, check_username=True)
check_passwd('nata', '12345nata', min_length=3, check_username=False)


# Аргументы переменной длины
# Позиционные аргументы переменной длины
##### Создается добавлением звездочки
##### Имя параметра может быть любым, но по договоренности чаще всего используют имя *args
##параметр a
###– если передается как позиционный аргумент, должен идти первым
###– если передается как ключевой аргумент, то порядок не важен
##• параметр *args - ожидает аргументы переменной длины
###– сюда попадут все остальные аргументы в виде кортежа
###– эти аргументы могут отсутствовать
def sum_arg(a, *args):
    print(a, args)
    return a + sum(args)
sum_arg(1, 10, 20, 30)
sum_arg(1, 10)
sum_arg(1)


# Можно создать и такую функцию:
def sum_arg(*args):
    print(args)
    return sum(args)
sum_arg(1, 10, 20, 30)
sum_arg()


# Ключевые аргументы переменной длины
# Cоздается добавлением перед именем параметра двух звездочек.
# чаще всего, используют имя **kwargs (от keyword arguments), но может быть любым
def sum_arg(a, **kwargs):
    print(a, kwargs)
    return a + sum(kwargs.values())
sum_arg(a=5, b=10, c=20, d=30)
sum_arg(b=10, c=20, d=30, a=5)

# Распаковка аргументов
# выражения *args и **kwargs позволяют выполнять ещё одну задачу - распаковку аргументов.
items = [1, 2, 3]
print('One: {}, Two: {}, Three: {}'.format(items[0], items[1], items[2]))
# Вместо этого, можно воспользоваться распаковкой аргументов:
items = [1, 2, 3]
print('One: {}, Two: {}, Three: {}'.format(*items))


def config_interface(intf_name, ip_address, mask):
    interface = f'interface {intf_name}'
    no_shut = 'no shutdown'
    ip_addr = f'ip address {ip_address} {mask}'
    result = [interface, no_shut, ip_addr]
    return result
print(config_interface('Fa0/1', '10.0.1.1', '255.255.255.0'))
interfaces_info = [['Fa0/1', '10.0.1.1', '255.255.255.0'],
                   ['Fa0/2', '10.0.2.1', '255.255.255.0'],
                   ['Fa0/3', '10.0.3.1', '255.255.255.0'],
                   ['Fa0/4', '10.0.4.1', '255.255.255.0'],
                   ['Lo0', '10.0.0.1', '255.255.255.255']]
for info in interfaces_info:
    print(config_interface(*info))


# Распаковка ключевых аргументов
def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
username_passwd = [{'username': 'cisco', 'password': 'cisco'},
                   {'username': 'nata', 'password': 'natapass'},
                   {'username': 'user', 'password': '123456789'}]
for data in username_passwd:
    check_passwd(**data)

# Пример использования ключевых аргументов переменной длины и распаковки аргументов
def add_user_to_users_file(user, users_filename='users.txt',
                           **kwargs):  # **kwargs заменил min_length=8, check_username=True)
    while True:
        passwd = input(f'Введите пароль для пользователя {user}: ')
        if check_passwd(user, passwd, **kwargs):  # использует предыдущую функцию
            break
        with open(users_filename, 'a') as f:
            f.write(f'{user},{passwd}\n')
add_user_to_users_file('nata', min_length=5)

# Аргументы, которые можно передавать только как ключевые
# Аргументы, которые указаны после * можно передавать только как ключевые при вызове функции.
def check_passwd(username, password, *, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True
check_passwd('nata', '12345', min_length=3)

# Распространенные проблемы/нюансы работы с функциями
###Список/словарь в который собираются данные в функции, создан за пределами функции
def func(items):
    result = []
    for i in items:
        result.append(i * 100)
    return print(result)
func([1, 2, 3])

# Значения по умолчанию в параметрах создаются во время создания функции
from datetime import datetime
import time
def print_current_datetime():
    print(f">>> {datetime.now()}")
    for i in range(3):
        print("Имитируем долгое выполнение...")
        time.sleep(1)
        print(print_current_datetime())
print_current_datetime()

# Например, использование списка в значении по умолчанию:
def add_item(item, data=None):
    if data is None:
        data = []
    data.append(item)
    return data
add_item(1)
add_item(2)

#Ошибка UnboundLocalError: local variable referenced before assignment
#обращение к переменной в функции идет до ее создания
def f():
    print(b)
    b = 55
f()

def f():
    if 5 > 8:
        b = 55
    print(b)
f()

#обращение внутри функции к глобальной переменной, но при этом внутри функции со-
#здана такая же переменная позже
a = 10
def f():
    print(a)
    a = 55
    print(a)
f()
