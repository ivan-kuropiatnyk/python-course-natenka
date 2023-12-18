'''
Python for network engineers Natasha Samoilenko
'''
# Page range 249
# Task 9.2a
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
    all_command_dict = {}
    for interface, vlan in trunk_config.items():
        #print(f"interface {interface}")
        list_commands = []
        for command in trunk_template:
            if 'allowed vlan' not in command:
                #print(" ", command)
                list_commands.append(command)
            elif 'allowed vlan' in command:
                #print(" ", f"{command} {str(vlan).replace('[','').replace(']','').replace(' ','')}")
                list_commands.append(f"{command} {str(vlan).replace('[','').replace(']','').replace(' ','')}")
            all_command_dict[f"interface {interface}"] = list_commands
    return all_command_dict
print("=====-----OUTPUT-----=====")
print(generate_trunk_config(trunk_config, trunk_mode_template))