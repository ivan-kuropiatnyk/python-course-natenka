'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#TASK = 5.3, 5.3a
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


template = {"access": access_template, "trunk": trunk_template}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(f"interface {interface}")
print("\n".join(template[mode]).format(vlans))



template = {"access": access_template, "trunk": trunk_template}
question = {"access": "Введите номер VLAN: ", "trunk": "Введите разрешенные VLANы: "}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input(question[mode])

print("interface {}".format(interface))
print("\n".join(template[mode]).format(vlans))