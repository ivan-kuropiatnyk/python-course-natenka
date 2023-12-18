'''
Python for network engineers Natasha Samoilenko
'''
# Page range 114-118
#Ввод информации пользователем
interface = input('Enter interface type and number: ')
vlan = input('Enter VLAN number: ')
access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']
access_template = '\n'.join(access_template).format(vlan)
interface_print = 'interface {}'.format(interface)
print('\n' + '-' * 30)
print(interface_print)
print(access_template)