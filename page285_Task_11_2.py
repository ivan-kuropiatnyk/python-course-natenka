'''
Python for network engineers Natasha Samoilenko
'''
# Page range 286
# Task 11.2
from page285_Task_11_1 import parse_cdp_neighbors
def create_network_map(filenames):
    dict_all = {}
    i = 0
    for file in filenames:
        i += 1
        with open(file) as show_command:
            current_dict = parse_cdp_neighbors(show_command.read())
            for device_source, device_dest in current_dict.items():
                dict_all[device_source] = device_dest
    if i == len(filenames):
        return dict_all
if __name__ == "__main__":
    infiles = [
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r3.txt",
    ]
    print(create_network_map(infiles))