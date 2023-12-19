'''
Python for network engineers Natasha Samoilenko
'''
# Page range 479 - 500
# 19
### 19.1 Измерение времени выполнения скрипта
###
from datetime import datetime
import time
start_time = datetime.now()
#Тут выполняются действия
time.sleep(5)
print(datetime.now() - start_time)

### 19.2 Процессы и потоки в Python (CPython)
###

### 19.3 Количество потоков
###

### 19.4 Потоковая безопасность
###

### 19.5 Модуль logging
###
#Самый простой вариант настройки логирования в скрипте, использовать logging.basicConfig:
import logging
logging.basicConfig(
format='%(threadName)s %(name)s %(levelname)s: %(message)s',
level=logging.INFO)
#В таком варианте настройки:
#• все сообщения будут выводиться на стандартный поток вывода,
#• будут выводиться сообщения уровня INFO и выше,
#• в каждом сообщении будет информация о потоке, имя логера, уровень сообщения и само сообщение.
#Теперь, чтобы вывести log-сообщение в этом скрипте, надо написать так logging.info("тест").
logging.info('msg')

### 19.6 Модуль concurrent.futures
#• ThreadPoolExecutor - для работы с потоками
#• ProcessPoolExecutor - для работы с процессами
#Создание объекта Executor на примере ThreadPoolExecutor:
executor = ThreadPoolExecutor(max_workers=5)
#После создания объекта Executor, у него есть три метода: shutdown, map и submit. Метод
#shutdown отвечает за завершение потоков/процессов, а методы map и submit за запуск функций в разных потоках/процессах.
#shutdown указывает, что объекту Executor надо завершить работу. При этом, если ме-
#тоду shutdown передать значение wait=True (значение по умолчанию), он не вернет резуль-
#тат пока не завершатся все функции, которые запущены в потоках. Если же wait=False, ме-
#тод shutdown завершает работу мгновенно, но при этом сам скрипт не завершит работу пока
#все функции не отработают.
#Как правило, метод shutdown не используется явно, так как при создании объекта Executor в
#менеджере контекста, метод shutdown автоматически вызывается в конце блока with c wait
#равным True.
#with ThreadPoolExecutor(max_workers=5) as executor:
#Так как методы map и submit запускают какую-то функцию в потоках или процессах, в коде
#должна присутствовать, как минимум, функция которая выполняет одно действие и которую
#надо запустить в разных потоках с разными аргументами функции.

#Метод map
#Синтаксис метода:
#map(func, *iterables, timeout=None)