'''
Python for network engineers Natasha Samoilenko
'''
# Page range 249
# Task 9.2
trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]
trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}
def generate_trunk_config(interface_vlan, trunk_template):
    all_in_one_list = []
    for interface, vlan in trunk_config.items():
        #print(f"interface {interface}")
        all_in_one_list.append(f"interface {interface}")
        for command in trunk_template:
            if 'allowed vlan' not in command:
                #print(" ", command)
                all_in_one_list.append(command)
            elif 'allowed vlan' in command:
                #print(" ", f"{command} {str(vlan).replace('[','').replace(']','').replace(' ','')}")
                all_in_one_list.append(f"{command} {str(vlan).replace('[','').replace(']','').replace(' ','')}")
    return all_in_one_list
print("=====-----OUTPUT-----=====")
print(generate_trunk_config(trunk_config, trunk_mode_template))