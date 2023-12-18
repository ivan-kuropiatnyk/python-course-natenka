# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 314
# Task 12.2
## convert_ranges_to_ip_list
## ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
## ['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
## '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']
import ipaddress
def find_n_ip(ip_from_range1,range1,range2):
    ipfirst_r1, iplast_r1 = range1.strip().split("-")
    ipfirst_r2, iplast_r2 = range2.strip().split("-")
    ipfirst_r1 = ipaddress.ip_address(ipfirst_r1)
    iplast_r1 = ipaddress.ip_address(iplast_r1)
    ipfirst_r2 = ipaddress.ip_address(ipfirst_r2)
    iplast_r2 = ipaddress.ip_address(iplast_r2)
    ip_from_range1 = ipaddress.ip_address(ip_from_range1)
    i = 0
    j = 0
    while ipfirst_r1 != ip_from_range1:
        i += 1
        ipfirst_r1 += 1
    while j != i:
        j += 1
        ipfirst_r2 += 1
    ip_new = str(ipfirst_r2)
    return print(ip_new)

if __name__ == "__main__":
    ip1_range1 = "10.1.1.1-10.1.2.30"
    ip1_range2 = "50.1.1.1-50.1.2.20"
    ip1_from_range1 = "10.1.2.17"
    ip1_from_range2 = "50.1.2.17"
    find_n_ip(ip1_from_range1,ip1_range1,ip1_range2)

    ip2_from_range1 = "10.1.1.127"
    ip2_range1 = "10.1.1.100-10.1.2.200"
    ip2_range2 = "50.1.1.110-50.1.2.210"
    ip2_from_range2 = "50.1.1.137"
    find_n_ip(ip2_from_range1, ip2_range1, ip2_range2)