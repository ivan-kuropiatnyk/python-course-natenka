'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#TASK = 5.1_OTVET
"""
Задание 5.1


В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1).
И вывести информацию о соответствующем устройстве на стандартный поток вывода
(информация будет в виде словаря).


Пример выполнения скрипта:
$ python task_5_1.py
Введите имя устройства: r1
{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device = input("5.1 Введите имя устройства: ")

print("5.1 result =>", london_co[device])


device = input("5.1.a Введите имя устройства: ")
parameter = input("5.1.a Введите имя параметра: ")

print("5.1.a result =>", london_co[device][parameter])

device = input("5.1.b Введите имя устройства: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"5.1.b Введите имя параметра ({params}): ")

print("5.1.b result =>", london_co[device][parameter])

device = input("5.1.c Введите имя устройства: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"5.1.c Введите имя параметра ({params}): ")

print("5.1.c result =>",london_co[device].get(parameter, "Такого параметра нет"))

device = input("5.1.d Введите имя устройства: ")
params = ", ".join(london_co[device].keys())
parameter = input(f"5.1.d Введите имя параметра ({params}): ")

print("5.1.d result =>", london_co[device].get(parameter.lower(), "Такого параметра нет"))