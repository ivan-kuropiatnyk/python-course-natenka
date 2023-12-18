'''
Python for network engineers Natasha Samoilenko
'''
# Page range 254-278
# 10 - Полезные функции
# • print
# print(*items, sep=' ', end='\n', file=sys.stdout, flush=False)
##sep - по умолчанию используется пробел:
print(1, 2, 3)
print(1, 2, 3, sep='|')
print(1, 2, 3, sep='\n')
print(1, 2, 3, sep=f"\n{'-' * 10}\n")
items = [1, 2, 3, 4, 5]
print(*items, sep=', ')
##end - значение выведется после вывода всех элементов. По умолчанию - перевод строки:
print(1, 2, 3)
print(1, 2, 3, end='\n' + '-' * 10)
##file-  умолчанию все на стандартный поток вывода - sys.stdout.
f = open('result_p256.txt', 'w')
for num in range(10):
    print(f'Item {num}', file=f)
f.close()
##flush - По умолчанию при записи в файл или выводе на стандартный поток  вывод буфери-
##зируется. Параметр flush позволяет отключать буферизацию
import time

for num in range(10):
    print(num)
    # time.sleep(1)
import time

for num in range(10):
    print(num, end=' ', flush=True)
    # time.sleep(1)

# • range
# range(start, stop[, step])
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(0, 10, 2)))
print(list(range(10, 0, -1)))
print(list(range(10, 0, -2)))
print(list(range(0, -10, -1)))
nums = range(5)
print(3 in nums)
print(7 in nums)
print(nums[:3])
print(len(nums))
print(max(nums))
print(min(nums))
print(nums.index(0))

# • sorted
list_of_words = ['one', 'two', 'list', '', 'dict']
print(sorted(list_of_words))
tuple_of_words = ('one', 'two', 'list', '', 'dict')
print(sorted(tuple_of_words))
set_of_words = {'one', 'two', 'list', '', 'dict'}
print(sorted(set_of_words))
string_to_sort = 'long string'
print(sorted(string_to_sort))
##reverse
list_of_words = ['one', 'two', 'list', '', 'dict']
print(sorted(list_of_words))
print(sorted(list_of_words, reverse=True))
##key
list_of_words = ['one', 'two', 'list', '', 'dict']
print(sorted(list_of_words, key=len))
dict_for_sort = {
    'id': 1,
    'name': 'London',
    'IT_VLAN': 320,
    'User_VLAN': 1010,
    'Mngmt_VLAN': 99,
    'to_name': None,
    'to_id': None,
    'port': 'G1/0/11'
}
sorted(dict_for_sort, key=str.lower)
from operator import itemgetter

list_of_tuples = [('IT_VLAN', 320),
                  ('Mngmt_VLAN', 99),
                  ('User_VLAN', 1010),
                  ('DB_VLAN', 11)]
print(sorted(list_of_tuples, key=itemgetter(int(1))))

ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]
def bin_ip(ip):
    octets = [int(o) for o in ip.split(".")]
    return ("{:08b}"*4).format(*octets)
bin_ip("10.1.1.1")
print(sorted(ip_list, key=bin_ip))

# • enumerate
list1 = ['str1', 'str2', 'str3']
for position, string in enumerate(list1):
    print(position, string)
list1 = ['str1', 'str2', 'str3']
for position, string in enumerate(list1, 100):
    print(position, string)
list1 = ['str1', 'str2', 'str3']
print(list(enumerate(list1, 100)))

# • zip
a = [1, 2, 3]
b = [100, 200, 300]
print(list(zip(a, b)))
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300]
print(list(zip(a, b, c)))
d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
d_values = ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1']
list(zip(d_keys, d_values))
print(dict(zip(d_keys, d_values)))

d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
data = {
'r1': ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
'r2': ['london_r2', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.2'],
'sw1': ['london_sw1', '21 New Globe Walk', 'Cisco', '3850', '3.6.XE', '10.255.0.101']}
london_co = {}
for k in data.keys():
    london_co[k] = dict(zip(d_keys, data[k]))
print(london_co)

# • all, any
##Функция all возвращает True, если все элементы истинные (или объект пустой).
ip = '10.0.1.1'
print(all(i.isdigit() for i in ip.split('.')))
print(all(i.isdigit() for i in '10.1.1.a'.split('.')))
##Функция any возвращает True, если хотя бы один элемент истинный.
def ignore_command(command):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    '''
    ignore = ['duplex', 'alias', 'Current configuration']
    return any([word in command for word in ignore])


# • lambda
##В Python лямбда-выражение позволяет создавать анонимные функции - функции, которые не привязаны к имени.
##В анонимной функции:
##• может содержаться только одно выражение
##• могут передаваться сколько угодно аргументов
##Стандартная функция:
def sum_arg(a, b): return a + b
sum_arg(1, 2)
#Аналогичная анонимная функция, или лямбда-функция:
sum_arg = lambda a, b: a + b
sum_arg(1, 2)

list_of_tuples = [('IT_VLAN', 320),
('Mngmt_VLAN', 99),
('User_VLAN', 1010),
('DB_VLAN', 11)]
print(sorted(list_of_tuples, key=lambda x: x[int(1)]))

# • map, filter
##Функция map применяет функцию к каждому элементу последовательности и возвращает
##итератор с результатами.
list_of_words = ['one', 'two', 'list', '', 'dict']
print(list(map(str.upper, list_of_words)))

list_of_str = ['1', '2', '5', '10']
print(list(map(int, list_of_str)))

#Вместе с map удобно использовать лямбда-выражения:
vlans = [100, 110, 150, 200, 201, 202]
print(list(map(lambda x: 'vlan {}'.format(x), vlans)))

#Если функция, которую использует map(), ожидает два аргумента, то передаются два списка:
nums = [1, 2, 3, 4, 5]
nums2 = [100, 200, 300, 400, 500]
print(list(map(lambda x, y: x*y, nums, nums2)))

#List comprehension вместо map
list_of_words = ['one', 'two', 'list', '', 'dict']
print([word.upper() for word in list_of_words])

list_of_str = ['1', '2', '5', '10']
print([int(i) for i in list_of_str])

vlans = [100, 110, 150, 200, 201, 202]
print([f'vlan {x}' for x in vlans])

nums = [1, 2, 3, 4, 5]
nums2 = [100, 200, 300, 400, 500]
print([x * y for x, y in zip(nums, nums2)])

#Функция filter
list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
filter(str.isdigit, list_of_strings)
print(list(filter(str.isdigit, list_of_strings)))

#только нечетные
nechetnye = list(filter(lambda x: x % 2 == 1, [10, 111, 102, 213, 314, 515]))
print(nechetnye)
#только нечетные
chetnye = list(filter(lambda x: x % 2 == 0, [10, 111, 102, 213, 314, 515]))
print(chetnye)

#Из списка слов оставить только те, у которых количество букв больше 3:
list_of_words = ['one', 'two', 'list', '', 'dict']
print(list(filter(lambda x: len(x) > 3, list_of_words)))

#List comprehension вместо filter
list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
print([s for s in list_of_strings if s.isdigit()])

#Нечетные/четные числа:
nums = [10, 111, 102, 213, 314, 515]
print([n for n in nums if n % 2 == 1])
print([n for n in nums if n % 2 == 0])

#Из списка слов оставить только те, у которых количество букв больше 3:
list_of_words = ['one', 'two', 'list', '', 'dict']
print([word for word in list_of_words if len(word) > 3])


