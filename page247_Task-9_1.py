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

access_config = {
                "FastEthernet0/12": 10,
                "FastEthernet0/14": 11,
                "FastEthernet0/16": 17
                }

access_config_2 = {
                    "FastEthernet0/03": 100,
                    "FastEthernet0/07": 101,
                    "FastEthernet0/09": 107,
                    }

def generate_access_config(intf_vlan_mapping, access_template):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
    {"FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    for interface, vlan in intf_vlan_mapping.items():
        print(f"interface {interface}")
        for command in access_template:
            if 'vlan' in command:
                print(f"{command} {vlan}")
            else:
                print(command)
print("---------access_config------------")
generate_access_config(access_config, access_mode_template)
print("---------access_config_2------------")
generate_access_config(access_config_2, access_mode_template)