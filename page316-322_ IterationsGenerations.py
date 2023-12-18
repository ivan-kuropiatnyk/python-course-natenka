'''
Python for network engineers Natasha Samoilenko
'''
# Page range 290 - 313
# 13 -Итераторы, итерируемые объекты и генераторы
## • итерируемые объекты (iterable)
## • итераторы (iterator)
lista = [1, 2, 3]
print(iter(lista))

numbers = [1, 2, 3]
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
#print(next(i))

f = open('page316_r1.txt')
print(f.__next__())
print(f.__next__())

with open('page316_r1.txt') as f:
    for line in f:
        print(line.rstrip())

## • генераторные выражения (generator expression)
###Обычная функция завершает работу, если:
###• встретилось выражение return
###• закончился код функции (это срабатывает как выражение return None)
###• возникло исключение
###Генератор же генерирует значения. При этом значения возвращаются по запросу, и после
###возврата одного значения выполнение функции-генератора приостанавливается до запроса
###следующего значения. Между запросами генератор сохраняет свое состояние.
###Python позволяет создавать генераторы двумя способами:
###• генераторное выражение
###• функция-генератор
genexpr = (x**2 for x in range(10000))
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))
print(next(genexpr))