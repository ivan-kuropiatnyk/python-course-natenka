# -*- coding: utf-8 -*-
import textfsm
from tabulate import tabulate
def parse_command_output(template, command_output):
    with open(template) as templ:
        fsm = textfsm.TextFSM(templ)
        header = fsm.header
        parsed = fsm.ParseText(command_output)
        result = tabulate(parsed, headers=header)
    return result

# вызов функции должен выглядеть так
if __name__ == "__main__":
    template = "templates/sh_ip_dhcp_snooping.template.txt"
    file_output = "output/sh_ip_dhcp_snooping.txt"
    output = open(file_output).read()
    print(output)
    result = parse_command_output(template, output)
    print(result)