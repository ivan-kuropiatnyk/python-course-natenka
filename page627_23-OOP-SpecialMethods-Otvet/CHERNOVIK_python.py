dictionary = {'conf t': 'conf t\nEnter configuration commands, one per line.  End with CNTL/Z.\nr1-ansible(config)#', 'logging 10.1.1.1': 'logging 10.1.1.1\nr1-ansible(config)#', 'interface loop55': 'interface loop55\nr1-ansible(config-if)#', 'ip address 5.5.5.5 255.255.255.255': 'ip address 5.5.5.5 255.255.255.255\nr1-ansible(config-if)#', 'end': 'end\nr1-ansible#'}
for command, output in dictionary.items():
    if '\n' in output:
        count_n = output.count('\n')
part_delete = str(str(dictionary['conf t']) + str('conf t'))