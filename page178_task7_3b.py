'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.3b
"""
CAM_table.txt. Каждая строка, где есть MAC-адрес, должна быть обработана 
таким образом, чтобы на стандартный поток вывода была выведена таблица вида:
100 01bb.c580.7000 Gi0/1
"""
with open('CAM_table.txt', 'r', encoding='latin_1') as src, open('CAM_table_RESULT.txt', 'w', encoding='latin_1') as dest:
    all_lines_as_list = []
    vlan_list = []
    k = 0
    inserted = False
    for line in src:
        # Выделить все не пустые строки:
        if 'DYNAMIC' in line:
            line_list = line.split()
            mac_index = line_list[1].replace(".", "")
            # Проверить что в строке точно есть мак адрес
            if len(mac_index) == 12:
                vlan = int(line_list[0])
                # проверить что в строке точно есть vlan
                if vlan != 0 or vlan != None or vlan != False:
                    # Добавить первый итерируемый влан в список
                    k += 1
                    if k == 1:
                        vlan_list.append(vlan)
                        all_lines_as_list.append(line)
                    else:
                        #вычислим максимальное значение в списке и его индекс
                        max_vlan = max(vlan_list)
                        index_max_vlan = vlan_list.index(max_vlan)
                        # вычислим минимальное значение в списке и его индекс
                        min_vlan = min(vlan_list)
                        index_min_vlan = vlan_list.index(min_vlan)
                        i = -1
                        while i != len(vlan_list)-1 :
                            i += 1
                            if vlan <= vlan_list[i]:
                                vlan_list.insert(i, vlan)
                                all_lines_as_list.insert(i, line)
                                break
                            elif vlan >= vlan_list[index_max_vlan]:
                                vlan_list.insert(index_max_vlan + 1, vlan)
                                all_lines_as_list.insert(index_max_vlan + 1, line)
                                break
    input_vlan = input("Please enter vlan:")
    for j in range(0, len(vlan_list)):
        #print(all_lines_as_list[j].rstrip())
        dest.write(all_lines_as_list[j])
        if input_vlan in all_lines_as_list[j]:
            print(all_lines_as_list[j].rstrip())
