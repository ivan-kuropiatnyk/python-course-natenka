'''
Python for network engineers Natasha Samoilenko
'''
# Page range 251
# Task 9.3a
def get_int_vlan_map(config_filename):
    k = 0#count of lines where 'interface' is present
    list_intf = []#list  interfaces in config
    access_list_intf_vlan = []#list access interface,vlan
    trunk_list_intf_vlan = []#list trunk interface,vlans
    with open(config_filename, 'r') as read_config_file:
        for line in read_config_file:
            if 'interface' in line:
                list_intf.append(line.split()[-1])
                k += 1
            elif 1 <= k <= len(list_intf) and "mode access" in line:
                access_list_intf_vlan.append(list_intf[k - 1])
                access_list_intf_vlan.append(int(1))
            elif 1 <= k <= len(list_intf) and "access vlan" in line:
                access_list_intf_vlan.remove(access_list_intf_vlan[-1])
                access_list_intf_vlan.append(int(line.split()[-1]))
            elif 1 <= k <= len(list_intf) and "allowed vlan" in line:
                trunk_list_intf_vlan.append(list_intf[k - 1])
                trunk_list_intf_vlan.append(line.split()[-1].split(","))
    access_dict = dict(zip(access_list_intf_vlan[::2], access_list_intf_vlan[1::2]))
    trunk_dict = dict(zip(trunk_list_intf_vlan[::2], trunk_list_intf_vlan[1::2]))
    return access_dict, trunk_dict
print("=====-----OUTPUT-----=====")
print(get_int_vlan_map(config_filename = 'config_sw2_task93_p250.txt'))