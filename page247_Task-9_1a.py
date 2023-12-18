'''
Python for network engineers Natasha Samoilenko
'''
# Page range 247
# Task 9.1
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    {"FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    list_interfaces = []#для создания в одном списке интерфейс + список комманд
    dict_config = {}#для создания словаря интерфейс-ключ : значение=список комманд
    dict_in_dict_conf = {}#баловался с созданием словаря в словаре
    for interface, vlan in intf_vlan_mapping.items():
        list_interfaces.append(f"interface {interface}")
        if psecurity == None:
            list_commands = []
            dict_commands = {}
            for command in access_template:
                if 'vlan' in command:
                    list_commands.append(f"{command} {vlan}")
                    dict_commands.setdefault(f"{command} {vlan}")
                else:
                    list_commands.append(command)
                    dict_commands.setdefault(command)
            list_interfaces.append(list_commands)
            dict_config[f"interface {interface}"] = list_commands
            dict_in_dict_conf[f"interface {interface}"] = {}
        elif psecurity != None:
            list_commands = []
            dict_commands = {}
            for command in access_template:
                if 'vlan' in command:
                    list_commands.append(f"{command} {vlan}")
                    dict_commands.setdefault(f"{command} {vlan}")
                else:
                    list_commands.append(command)
                    dict_commands.setdefault(command)
            for psec_command in psecurity:
                list_commands.append(psec_command)
                dict_commands.setdefault(psec_command)
            list_interfaces.append(list_commands)
            dict_config[f"interface {interface}"] = list_commands
            dict_in_dict_conf[f"interface {interface}"] = dict_commands
    return dict_config
print("---------=================psecurity=================------------")
print(generate_access_config(access_config, access_mode_template, port_security_template))