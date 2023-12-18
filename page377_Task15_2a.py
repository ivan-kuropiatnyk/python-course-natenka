# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 377
# Task 15.2a
def convert_to_dict(list_headers,tuple_values):
    list_all = []
    for n in tuple_values:
        x = 0
        dict_local = {}
        local_list_value = list(n)
        while x != len(list_headers):
            x += 1
            key = list_headers[x-1]
            value = local_list_value[x-1]
            dict_local[key] = value
        list_all.append(dict_local)
    return list_all
if __name__ == "__main__":
    headers = ["hostname", "ios", "platform"]
    data = [
        ("R1", "12.4(24)T1", "Cisco 3825"),
        ("R2", "15.2(2)T1", "Cisco 2911"),
        ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
    ]
    print(convert_to_dict(headers,data))