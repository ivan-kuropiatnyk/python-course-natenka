'''
Python for network engineers Natasha Samoilenko
'''
# Page range 142 - 146
#break, continue, pass
i = 0
for num in range(1,10):
    i += 1
    if num <= 7:
        print(num)
    else:
        break

i = 0
j = []
while i < 10:
    if i == 5:
        print(j)
        break
    else:
        i += 1
        j.append(i)

#break:
'''
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
while True:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        # завершает цикл while
        break
    password = input('Введите пароль еще раз: ')
'''

'''
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
a = 0
b = 3
while True:
    if a < 3:
        if len(password) < 4:
            print('Пароль слишком короткий\n')
        elif username in password:
            print('Пароль содержит имя пользователя\n')
        else:
            print('Пароль для пользователя {} установлен'.format(username))
            # завершает цикл while
            break
        password = input('Введите пароль еще раз: ')
        a += 1
        b -= 1
        print(f'You have {b} attempts')
    else:
        print('password entered more than 3 times')
        break
'''
#Оператор continue
for num in range(5):
    if num == 3:
        continue
    else:
        print("Оператор Continue", num)

i = 0
while i < 6:
    i += 1
    if i == 3:
        print("Пропускаем 3")
        continue
        print("Это никто не увидит")
    else:
        print("Текущее значение: ", i)

'''
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
password_correct = False
while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
    else:
        print('Пароль для пользователя {} установлен'.format(username))
        password_correct = True
        continue
    password = input('Введите пароль еще раз: ')
'''

#Оператор pass
for num in range(5):
    if num < 3:
        pass
    else:
        print(num)

# for/else
for num in range(5):
    print(num)
else:
    print("Числа for/else")

for num in range(5):
    if num == 3:
        break
    else:
        print(num)
else:
    print("Числа for/else(2)")

for num in range(5):
    if num == 3:
        continue
    else:
        print(num)
else:
    print("Числа закончились")

# while/else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Конец")

i = 0
while i < 5:
    if i == 3:
        break
    else:
        print(i)
        i += 1
else:
    print("Конец")