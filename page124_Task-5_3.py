'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#TASK = 5.3, 5.3a
template_input_vlans = {
    "access": "«Введите номер VLAN:»",
    "trunk": "«Введите разрешенные VLANы:»",
}

input_mode = input("Введите режим работы интерфейса (access/trunk):")
input_inface = input("Введите тип и номер интерфейса (Fa0/6):")

template_input_vlans_print = "".join(template_input_vlans[input_mode])
input_vlans = input("{}".format(template_input_vlans_print))

#input_mode = "access"
#input_inface = "Fa0/6"
#input_vlans = "10,20,30"
access_template = [
"switchport mode access",
"switchport access vlan {}",
"switchport nonegotiate",
"spanning-tree portfast",
"spanning-tree bpduguard enable"
]
trunk_template = [
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan {}"
]

template = {"access": access_template, "trunk": trunk_template}
#interface = "interface " + input_inface
template_print = "\n".join(template[input_mode]).format(input_vlans)
print(f"interface {input_inface}")
print(template_print)


