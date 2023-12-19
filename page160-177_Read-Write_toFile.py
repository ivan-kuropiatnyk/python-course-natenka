'''
Python for network engineers Natasha Samoilenko
'''
# Page range 160-177
# Чтение файлов
f = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
print(f.read())
f = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
print(f.readline())
for line in f:
    print(line)
f = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
print(f.readlines())

txt_delen_po_enteru = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
txt_delen_po_enteru = txt_delen_po_enteru.read().split('\n')
print("txt_delen_po_enteru => " + str(txt_delen_po_enteru))

bez_pust_str = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
bez_pust_str = bez_pust_str.read().rstrip().split('\n')
print("Bez pustoi stroki is => " + str(bez_pust_str))

#Переход курсора в начало файла:
kursor_nachalo = open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt")
# index position from the beginning
kursor_nachalo.seek(0)
# prints current position
print(kursor_nachalo.tell())

#page 164
# Write(append) to a file:
##• write - записать в файл одну строку
##• writelines - позволяет передавать в качестве аргумента список строк
cfg_lines = [
'!',
'service timestamps debug datetime msec localtime show-timezone year',
'service timestamps log datetime msec localtime show-timezone year',
'service password-encryption',
'service sequence-numbers',
'!',
'no ip domain lookup',
'!',
'ip ssh version 2',
'!']
write_to_file = open("D:\Literature\Python\PyMyProgNatenka1\_page_165_r2.txt", 'w')
cfg_lines_as_string = '\n'.join(cfg_lines)
#Запись строки в файл:
write_to_file.write(cfg_lines_as_string)
#Аналогично можно добавить строку вручную:
write_to_file.write("\nthis string added directly 2d time")
#Добавить список строк из переменной:
write_to_file.write("\nHERE IS TEXT ADDED FROM THE LIST OF STRING:")
write_to_file.writelines(cfg_lines)
#Добавить перевод строки можно по-разному. Например, можно просто обработать список в цикле:
cfg_lines2 = []
for line in cfg_lines:
    cfg_lines2.append(line + " \n")
write_to_file.write("\nTEXT AFTER CYCLE:")
write_to_file.writelines(cfg_lines2)
print("FILE CLOSED?:",write_to_file.closed)#проверяет открыт или нет файл
#После завершения работы с файлом, его необходимо закрыть:
write_to_file.close()
print("AND NOW THE FILE CLOSED, ISN'T IT?:",write_to_file.closed)

#конструкция with гарантирует закрытие файла автоматически
with open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt", 'r') as open_with:
    for line_open_with in open_with:
        print(line_open_with.rstrip())#rstrip убирает лишние пустые строки
print("IS IT OPEN AFTER with?:",open_with.closed)

with open("D:\Literature\Python\PyMyProgNatenka1\_page_160_r1.txt", 'r') as f:
    print("ВТОРОЙ ВАРИАНТ:\n", f.read())

#Открытие двух файлов:
with open('_page_160_r1.txt') as src, open('result1.txt', 'w') as dest:
    for line in src:
        if line.startswith('service'):
            dest.write(line)
#Это равнозначно таким двум блокам with:
with open('_page_160_r1.txt') as src:
    with open('result2.txt', 'w') as dest:
        for line in src:
            if line.startswith('service'):
                dest.write(line)

#Разбор вывода столбцами:
result = {}
with open('sh_ip_int_br.txt') as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[1][0].isdigit():#первый знак второго столбца (там где ип адреса)
            interface = line_list[0]
            address = line_list[1]
            result[interface] = address#создает ключ(interface)=>значение(address) в переменную result
print(result)

#Получение ключа и значения из разных строк вывода
with open('sh_ip_interface.txt') as int_ip_mtu:
    for line in int_ip_mtu:
        if 'line protocol' in line:
            int_int_ip_mtu = line.split()[0]
        elif 'Internet address' in line:
            ip_int_ip_mtu = line.split()[-1]
        elif 'MTU' in line:
            mtu_int_ip_mtu = line.split()[-2]
            print('{:15} {:17} {}'.format(int_int_ip_mtu, ip_int_ip_mtu, mtu_int_ip_mtu))

#Вложенный словарь
result_af = {}
with open('sh_ip_interface.txt') as af:
    for lineaf in af:
        if 'line protocol' in lineaf:
            interfaceaf = lineaf.split()[0]
            result_af[interfaceaf] = {}
        elif 'Internet address' in lineaf:
            ip_addressaf = lineaf.split()[-1]
            result_af[interfaceaf]['ip'] = ip_addressaf
        elif 'MTU' in lineaf:
            mtuaf = lineaf.split()[-2]
            result_af[interfaceaf]['mtu'] = mtuaf
            print(result_af)

#Вывод с пустыми значениями
result_ff = {}
with open('sh_ip_interface.txt') as ff:
    for lineff in ff:
        if 'line protocol' in lineff:
            interfaceff = lineff.split()[0]
        elif 'Internet address' in lineff:
            ip_addressff = lineff.split()[-1]
            result_ff[interfaceff] = {}
            result_ff[interfaceff]['ip'] = ip_addressff
        elif 'MTU' in lineff:
            mtuff = lineff.split()[-2]
            result_ff[interfaceff]['mtu'] = mtuff
            print(result_ff)