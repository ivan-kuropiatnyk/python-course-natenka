'''
Python for network engineers Natasha Samoilenko
'''
# Page range 252
# Task 9.4
ignore = ["duplex", "alias", "Current configuration"]
def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    '''
    Task 9.4
    :param config_filename: Cisco config file
    :return: dictionary where keys=string of config and value=list of substring for the actual key string
    '''
    with open(config_filename,'r') as read_config:
        list_key_line = []#list of string-key for a dictionary
        dict_key_val_line = {}#the dictionary which will be filled and returned by this function
        for line in read_config:
            # by function 'ignore_command' defines is this line should be showed
            ignore_stat = ignore_command(line, ignore)
            # for removing all line which ignored by function 'ignore_command'
            # which contains '!' 'end'
            # and length of which more than 2 symbols what means that this line isn't empty
            if ignore_stat == False and line[0] != '!' and len(line) > 2:
                if line[0].isalpha():
                    value_list = []#list of values
                    list_key_line.append(line)
                    dict_key_val_line[f'{list_key_line[-1]}'] = value_list
                else:
                    line = line[1:]#for removing space which is a 1st symbol
                    value_list.append(line)
                    dict_key_val_line[f'{list_key_line[-1]}'] = value_list
        return dict_key_val_line
print("=====-----OUTPUT-----=====")
print(convert_config_to_dict(config_filename='config_sw1_task93_p250.txt'))