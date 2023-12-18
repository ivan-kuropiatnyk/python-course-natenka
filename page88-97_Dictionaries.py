'''
Python for network engineers Natasha Samoilenko
'''
# Page range 88 - 97
### type data
##### Page 83
#• Dictionaries (словари)
london1 = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
london2 = {
'id': 1,
'name': 'London2',
'it_vlan': 320,
'user_vlan': 1010,
'mngmt_vlan': 99,
'to_name': None,
'to_id': None,
'port': 'G1/0/11'
}
print("london1 =",london1)
print("london2 =",london2)
print("london1(name) =",london1['name'])

london2['Vendor'] = 'Cisco' #add key Vendor with value Cisco to Dict London2
print("london2 after adding vendor = \n",london2)

#In london_co used a dictionary inside dictionary:
london_co = {
    'r1': {
        'hostname': 'london_r1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
        },
    'r2': {
        'hostname': 'london_r2',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
        },
    'sw1': {
        'hostname': 'london_sw1',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101'
    }
}
print("london_co =\n",london_co)
print("london_co['r1']['ios'] =",london_co['r1']['ios'])
print("london_co['r1']['model'] =",london_co['r1']['model'])
print("london_co['sw1']['ip'] =",london_co['sw1']['ip'])
print("sorted(london1) =", sorted(london1)) #sorts keys of the variable
london_cleared = london1
london_cleared.clear()
print("london_cleared =", london_cleared)
print("id(london_cleared) =",id(london_cleared))
print("id(london1) =",id(london1))
london_copy = london1.copy()
print("id(london_copy) =",id(london_copy))
print("london_copy =", london_copy)
print("london2[] =", london2['id'])
print("london2.get() =", london2.get('ios'))#if there are no key get print None, but it is possible to change of Oops as ex
print("london2.get() =", london2.get('ios', 'Ooups'))

ios = london2.setdefault('ios')
print("london2", ios)
print("london2", london2)
#Метод setdefault заменяет такую конструкцию:
if ios in london2:
    value = london2['ios']
    print("london2['ios'] inside =", value)
else:
    london2['ios'] = 'JunOS'
    value = london2['ios']
    print("london2['ios'] created =", value)
    print("london2 =", london2)
print("outside cycle =", london2)
ios = london2.setdefault('ios')
print("ios", ios)

london3 = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
print("london3.keys() =", london3.keys())
print("london3.values() =", london3.values())
print("london3.items() =", london3.items())
london3_keys = london3.keys()
print("london3_keys =", london3_keys)
#конвертировать view в список:
london3_list_keys = list(london3.keys())
print("london3_list_keys =", london3_list_keys)

london_del = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
del london_del['name']
print("london_del after del = ", london_del)
london_del.update({'name': 'London1'})
print("london_del after update1 = ", london_del)
london_for_update = {'model': '4451', 'ios': '15.4'}
london_del.update(london_for_update)#add as dict + dict
print("london_del after update2 = ", london_del)
#Варианты создания словаря
#Литерал
r1 = {'model': '4451', 'ios': '15.4'}
#dict
r2 = dict(model='4451', ios='15.4')
r3 = dict([('model', '4451'), ('ios', '15.4')])
d_keys = ['hostname', 'location', 'vendor', 'model', 'ios', 'ip']
r4 = dict.fromkeys(d_keys)
print("r4 =",r4)
r5 = dict.fromkeys(d_keys, 0)
print('r4 with 0 =', r5)

#• Tuples (кортежи)
#• Sets (множества)
#• Boolean (логический тип данных)
#Эти типы данных можно, в свою очередь, классифицировать по нескольким признакам:
#• изменяемые (списки, словари и множества)
#• неизменяемые (числа, строки и кортежи)
#• упорядоченные (списки, кортежи, строки и словари)
#• неупорядоченные (множества)