# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 314
# Task 12.3
from tabulate import tabulate
def print_ip_table(reach_ips, unreach_ips):
    dict_all = {}
    dict_all["Reachable"] = reach_ips
    dict_all["Unreachable"] = unreach_ips
    return print(tabulate(dict_all, headers="keys"))
if __name__ == "__main__":
    reachable = ['8.8.8.8', '8.8.4.4', '172.17.20.192', '172.17.20.161', '172.17.20.167']
    unreachable = ['172.17.30.205', '172.17.30.254', '172.17.30.1']
    print_ip_table(reachable, unreachable)

