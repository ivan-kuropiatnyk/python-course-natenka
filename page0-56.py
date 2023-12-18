a = 7
b = 14

if a > b:
    print("A больше B")
    print(a - b)
else:
    print("B больше или равно A")
    print(b - a)
    print("Конец")

# first exemple of the function:
def open_file(TextFile1):
    print("Чтение файла", TextFile1)
    with open(TextFile1) as f:
        return f.read()
        print("Готово")

# комментарий
"""
Длинный комментарий
"""
'''
Точно такой же длинный комментарий
'''

