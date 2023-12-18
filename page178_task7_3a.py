'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.3a.v1
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
        #Выделить все не пустые строки:
        if 'DYNAMIC' in line:
            line_list = line.split()
            mac_index = line_list[1].replace(".","")
            # Проверить что в строке точно есть мак адрес
            if len(mac_index) == 12:
                vlan = int(line_list[0])
                #проверить что в строке точно есть vlan
                if vlan != 0 or vlan != None or vlan != False:
                    #Добавить первый итерируемый влан в список
                    k += 1
                    if k == 1:
                        vlan_list.append(vlan)
                        all_lines_as_list.append(line)
                    # Если это не первый влан в списке тогда рассмотрим условие:
                    elif k > 1:
                        #вычислим максимальное значение в списке и его индекс
                        max_vlan = max(vlan_list)
                        index_max_vlan = vlan_list.index(max_vlan)
                        # вычислим минимальное значение в списке и его индекс
                        min_vlan = min(vlan_list)
                        index_min_vlan = vlan_list.index(min_vlan)
                        #print("Iteration =", k, " Max =", max_vlan," Index max =", index_max_vlan," Min =", min_vlan, " Index min =", index_min_vlan, " iterated Vlan =", vlan)
                        #Если это влан больше максимального то вставим его в список на индекс выше индекса максимального
                        # noinspection LanguageDetectionInspection
                        if vlan >= max_vlan:
                            vlan_list.insert(index_max_vlan + 1, vlan)
                            all_lines_as_list.insert(index_max_vlan + 1, line)
                        # Если же это влан меньше минимального то вставим его в список вместо минимального
                        elif vlan <= min_vlan:
                            vlan_list.insert(index_min_vlan, vlan)
                            all_lines_as_list.insert(index_min_vlan, line)
                        # Если же он равен элементу в списке то вставим его вместо первого такого же элемента
                        elif vlan in vlan_list:
                            index_vlan = vlan_list.index(vlan)
                            vlan_list.insert(index_vlan, vlan)
                            all_lines_as_list.insert(index_vlan, line)
                        #Иначе же пока i не сравняется с индексом максимального влана в списке:
                        else:
                            i = 0
                            while i != index_max_vlan:
                                i += 1
                                #поочередно сравниваем действующий влан с вланами в списке от 1го до того который будет больше
                                # как только находится влан больше записываем текущий влан на место большего,
                                # сдвигая больший на индекс выше и разрываем цикл
                                if vlan < vlan_list[i]:
                                    vlan_list.insert(i, vlan)
                                    all_lines_as_list.insert(i, line)
                                    break
    for j in range(0,len(vlan_list)):
        print(all_lines_as_list[j].rstrip())
        dest.write(all_lines_as_list[j])