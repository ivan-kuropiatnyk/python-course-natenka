'''
Python for network engineers Natasha Samoilenko
'''
# Page range 178
# TASK 7.1
p_keys = [
    'Prefix',
    'AD/Metric',
    'Next-Hop',
    'Last update',
    'Outbound Interface',
    ]
file_read = open('ospf.txt',mode='r',encoding='latin_1')
file_read.readline()
#filter(str.isalnum, file_read)
i = 0
dict_all = {}
for line in file_read:
    if 'O' in line:
        i += 1
        num = f"Pref_{i}"
        #dict_all[num] = None
        line = list(line.replace("[","").replace("]","").replace("via","").replace("O","").split())
        dict_key = dict(zip(p_keys,line))
        dict_all[num] = dict_key
        for key, value in dict_key.items():
            print(key, "=", value)
        print("\n".strip())
        #print(dict_all[num])
#print(dict_all)
file_read.close()