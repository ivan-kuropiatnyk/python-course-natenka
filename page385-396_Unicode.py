'''
Python for network engineers Natasha Samoilenko
'''
# Page range 346-375
# 16. Unicode
# 16.1 Стандарт Юникод
# 16.2 Юникод в Python 3
print("Вывод символа по имени юникода:","\N{LATIN SMALL LETTER O WITH DIAERESIS}")
print("Вывод символа по коду юникода:","\u00F6")
hi1 = 'привет'
hi2 = '\u043f\u0440\u0438\u0432\u0435\u0442'
print("Строка как последовательность кодов Юникод:", hi2)
print(hi1 == hi2)
print(len(hi2))
#Функция ord возвращает значение кода Unicode для символа:
print(ord('ö'))
#Функция chr возвращает символ Юникод, который соответствует коду:
print(chr(246))
#Тип bytes - это неизменяемая последовательность байтов.
#Байты обозначаются так же, как строки, но с добавлением буквы «b» перед строкой
b1 = b'\xd0\xb4\xd0\xb0'
b2 = b"\xd0\xb4\xd0\xb0"
print(type(b1))
print(len(b1))
print(b1)
#В Python байты, которые соответствуют символам ASCII, отображаются как эти символы, а не как соответствующие им байты.
bytes1 = b'hello'
print(bytes1)
print(len(bytes1))
print(bytes1.hex())
bytes2 = b'\x68\x65\x6c\x6c\x6f'
print(bytes2)
#bytes3 = b'привет'#will be error bytes can only contain ASCII literal characters
#print(bytes3)

#16.3 Конвертация между байтами и строками
#Для преобразования строки в байты используется метод encode:
hi = 'привет'
print(hi.encode('utf-8'))
hi_bytes = hi.encode('utf-8')
#Чтобы получить строку из байт, используется метод decode:
print(hi_bytes)
print(hi_bytes.decode('utf-8'))
#str.encode, bytes.decode
#Метод encode есть также в классе str (как и другие методы работы со строками):
print(str.encode(hi, encoding='utf-8'))
print(bytes.decode(hi_bytes, encoding='utf-8'))
print(bytes.decode(hi_bytes, 'utf-8'))

#простое правило Оно называется «Юникод-сэндвич»:
#• байты, которые программа считывает, надо как можно раньше преобразовать в Юникод(строку)
#• внутри программы работать с Юникод
#• Юникод надо преобразовать в байты как можно позже, перед передачей

#16.4 Примеры конвертации между байтами и строками
#Модуль subprocess возвращает результат команды в виде байт:
import subprocess
#result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.PIPE)
#print(result.stdout)# в виде байт
#output = result.stdout.decode('utf-8')
#print(output)
#result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
#                        stdout=subprocess.PIPE, encoding='utf-8')
#print(result.stdout)
import telnetlib
import time
t = telnetlib.Telnet('192.168.100.1')
t.read_until(b'Username:')
t.write(b'cisco\n')
t.read_until(b'Password:')
t.write(b'cisco\n')
t.write(b'sh ip int br\n')
time.sleep(1)
output = t.read_very_eager().decode('utf-8')
print(output)

import pexpect
output = pexpect.run('ls -ls')
output
output.decode('utf-8')
output = pexpect.run('ls -ls', encoding='utf-8')

#Работа с файлами
with open(filename, encoding='utf-8') as f:
    for line in f:
        print(line)

#16.5 Ошибки при конвертации
#Параметр errors в encode По умолчанию strict - при возникновении ошибок кодировки генерируется исключение UnicodeError.
#Вместо этого режима можно использовать replace, чтобы заменить символ знаком вопроса:
de_hi_unicode = 'grüezi'
de_hi_unicode.encode('ascii', 'replace')
#Или namereplace, чтобы заменить символ именем:
de_hi_unicode = 'grüezi'
#Или namereplace, чтобы заменить символ именем:
de_hi_unicode.encode('ascii', 'namereplace')
#Кроме того, можно полностью игнорировать символы, которые нельзя закодировать:
de_hi_unicode.encode('ascii', 'ignore')
#Параметр errors в decode - по умолчанию тstrict и генерируется исключение UnicodeDecodeError.
#Если изменить режим на ignore, как и в encode, символы будут просто игнорироваться:
de_hi_unicode = 'grüezi'
de_hi_utf8 = de_hi_unicode.encode('utf-8')
de_hi_utf8.decode('ascii', 'ignore')
#Режим replace заменит символы:
de_hi_utf8.decode('ascii', 'replace')