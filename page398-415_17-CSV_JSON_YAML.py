'''
Python for network engineers Natasha Samoilenko
'''
# Page range 398-415
# 17. Работа с файлами в формате CSV, JSON, YAML
# 17.1 Работа с файлами в формате CSV
import csv

with open('page398_sw_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('page398_sw_data.csv') as f:
    reader = csv.reader(f)
    print(list(reader))  # показывает список прочитанного файла
    for row in reader:
        print(row)
    print(reader)  # показывает итератор

print("заголовки отдельным объектом")
with open('page398_sw_data.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print('Headers: ', headers)
    for row in reader:
        print(row)

print("словарь ключи - это названия столбцов, а значения - значения столбцов")
import csv

with open('page398_sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row['hostname'], row['model'])

print("помощью модуля csv можно и записать файл в формате CSV")
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
with open('page398_sw_data_new.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('page398_sw_data_new.csv') as f:
    print(f.read())

print("чтобы все строки записывались в CSV-файл с кавычками")
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
with open('page398_sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)
with open('page398_sw_data_new.csv') as f:
    print(f.read())

print("Кроме метода writerow, поддерживается метод writerows")
data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]
with open('page398_sw_data_new.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)
with open('page398_sw_data_new.csv') as f:
    print(f.read())

print("С помощью DictWriter можно записать словари в формат CSV")
data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]
with open('page398_csv_write_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

print("Указание разделителя:")
with open('page398_sw_data2.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

# 17.2 Работа с файлами в формате JSON
# • json.load - метод считывает файл в формате JSON и возвращает объекты Python
# • json.loads - метод считывает строку в формате JSON и возвращает объекты Python
print("json.load")
import json

with open('page398_sw_templates.json') as f:
    templates = json.load(f)
print(templates)
for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

print("json.loads")
with open('page398_sw_templates.json') as f:
    file_content = f.read()
    templates = json.loads(file_content)
print(templates)
for section, commands in templates.items():
    print(section)
    print('\n'.join(commands))

# Запись файла в формате JSON, два метода:
# • json.dump - метод записывает объект Python в файл в формате JSON
# • json.dumps - метод возвращает строку в формате JSON
import json

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]
access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
to_json = {'trunk': trunk_template, 'access': access_template}

print("\nit is dumps method(for return line)")
with open('page398_sw_templates.json', 'w') as f:
    f.write(json.dumps(to_json))
with open('page398_sw_templates.json') as f:
    print(f.read())

print("\nit is dump method (the best one for write to file in JSON")
with open('page398_sw_templates_dump.json', 'w') as f:
    json.dump(to_json, f)
with open('page398_sw_templates_dump.json') as f:
    print(f.read())


# Дополнительные параметры методов записи
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]
access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
to_json = {'trunk': trunk_template, 'access': access_template}
with open('page398_sw_templates_param.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)
with open('page398_sw_templates_param.json') as f:
    print(f.read())

# Дополнительные параметры методов записи
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk native vlan 999', 'switchport trunk allowed vlan'
]
access_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]
to_json = {'trunk': trunk_template, 'access': access_template}
with open('page398_sw_templates_param.json', 'w') as f:
    json.dump(to_json, f, sort_keys=True, indent=2)
with open('page398_sw_templates_param.json') as f:
    print(f.read())

#Изменение типа данных
#Ограничение по типам данных
#В формат JSON нельзя записать словарь, у которого ключи - кортежи:
to_json = {('trunk', 'cisco'): trunk_template, 'access': access_template}
#with open('page398_sw_templates_limites.json', 'w') as f:
#    json.dump(to_json, f) #TypeError: key ('trunk', 'cisco') is not a string
#С помощью дополнительного параметра можно игнорировать подобные ключи:

with open('page398_sw_templates_limites.json', 'w') as f:
    json.dump(to_json, f, skipkeys=True)

#Кроме того, в JSON ключами словаря могут быть только строки. Но, если в словаре Python ис-
#пользовались числа, ошибки не будет. Вместо этого выполнится конвертация чисел в строки:
d = {1: 100, 2: 200}
print(json.dumps(d))

# 17.3 - Работа с файлами в формате YAML
import yaml
from pprint import pprint
with open('page398_info.yaml') as f:
    templates = yaml.safe_load(f)
pprint(templates)

#Запись в YAML
to_yaml = {
    'access': ['switchport mode access',
               'switchport access vlan',
               'switchport nonegotiate',
               'spanning-tree portfast',
               'spanning-tree bpduguard enable'],
    'trunk': ['switchport trunk encapsulation dot1q',
              'switchport mode trunk',
              'switchport trunk native vlan 999',
              'switchport trunk allowed vlan'],
}
with open('page398_sw_templates1.yaml', 'w') as f:
    yaml.dump(to_yaml, f)
with open('page398_sw_templates1.yaml') as f:
    print(f.read())