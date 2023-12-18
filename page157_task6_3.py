'''
Python for network engineers Natasha Samoilenko
'''
# Page range 157
# TASK 6.3
access_template = [
"switchport mode access",
"switchport access vlan",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]
trunk_template = [
"switchport trunk encapsulation dot1q",
"switchport mode trunk",
"switchport trunk allowed vlan",
]
access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

# FOR ACCESS:
for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

# FOR TRUNK:
trunk_values = list(trunk.values())
i = 0
print(trunk_values)
for interf in trunk.keys():
    i += 1
    chosen_mode_list = trunk_values[i-1]
    chosen_mode = chosen_mode_list[0]
    vlans = chosen_mode_list[1:]
    print("interface FastEthernet" + interf)
    print("---> chosen mode =", str(chosen_mode))
    print("---> vlans for this interface =>", str(vlans))
    write = " " + str(vlans).replace("[","").replace("]","").replace("'","").replace(" ","")
    if chosen_mode == "only":
        write = write
    elif chosen_mode == "del":
        write = " remove" + write
    elif chosen_mode == "add":
        write = " add" + write
    j = 0
    for trunk_write in trunk_template:
        j += 1
        if j < 3:
            print(" " + trunk_write)
        elif j == 3:
            print(" " + trunk_write + write)