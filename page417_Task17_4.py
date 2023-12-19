# -*- coding: utf-8 -*-
'''
Python for network engineers Natasha Samoilenko
'''
# Page range 417
# Task 17.4
import csv
import datetime

def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")

def write_last_log_to_csv(source_log, output = 'None'):
    with open(source_log, 'r') as src_log_file:#открываем файл csv для чтения
        final_list_logs = []#список куда складывается итоговый результат
        list_src_log_file = list(csv.reader(src_log_file))#все строки считанного файла вкладываются в единый список
        final_list_logs.append(list_src_log_file[0])#первый элемент является заголовками, его и добавим в итоговый список
        list_logs = list_src_log_file[1:]#все элементы кроме первого - это логи, которые сохраняем в новый список для дальнейшей обработки
        list_logs.sort(key=lambda row_inside_list: convert_str_to_datetime(row_inside_list[-1]), reverse=True)#с помощью лямбда выражения по датам сортируем список с логами, row_inside_list-это каждый элемент списка list_logs где row_inside_list[-1] - это последний элемент списка(дата), convert_str_to_datetime()-выше написанная функция, в данном случае она преобразует элемент в datatime, далее элменты сортируются но в итоговом списке остаются непреобразованными(первоначальными)
        for list_log in list_logs:#берем каждый элемент отсортированного по времени списка list_logs
            comparison = False#изначально совпадения не найдено
            for row_list in final_list_logs:#взятый элемент list_log будет сравниваться каждым уже добавленным элементом в итоговом списке
                if list_log[1] == row_list[1]:#если эмейл во взятом элемента равен эмейлу одного из уже добавленных элементов в конечном списке
                    comparison = True#совпадение найдено
            if comparison == False:#Если после всех сравниваний совпадения нет
                final_list_logs.append(list_log)#добавляем текущий элемент в итоговый список
    if output:#проверяем задан ли файл на запись, если да то:
        with open(output, 'w') as dst_log_file:#открываем файл на запись
            writer = csv.writer(dst_log_file)
            writer.writerows(final_list_logs)#записываем в файл сразу весь список, а не каждый элемент списка по очереди
    return final_list_logs#в любом случае функция возвращает итоговый отсортированный список с удаленными элементами, если у них был эмейл с более ранней датой записи

if __name__ == "__main__":
    print(write_last_log_to_csv('page417_mail_log.csv','page417_MY_mail_log_OUTPUT.csv' ))