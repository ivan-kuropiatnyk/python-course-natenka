'''
Python for network engineers Natasha Samoilenko
'''
# Page range 457-471
# 18
# 18.6 scrapli
### позволяет подключаться к сетевому оборудованию используя Telnet, SSH или NETCONF.
### Также как и netmiko, scrapli может использовать paramiko или telnetlib (и другие модули) для
### самого подключения, но при этом предоставляет одинаковый интерфейс работы для разных
### типов подключения и разного оборудования

### Три основные составляющие части scrapli:
### • transport - это конкретный способ подключения к оборудованию
### • channel - отвечает за отправку команд, получение вывода и другими взаимодействиями с оборудованием
### • driver - это интерфейс, который предоставляется пользователю для работы со scrapli.

### Доступные варианты транспорта:
### • system - используется встроенный SSH клиент, подразумевается использование клиента на Linux/MacOS
### • paramiko - модуль paramiko
### • ssh2 - используется модуль ssh2-python (обертка вокруг C библиотеки libssh2)
### • telnet - будет использоваться telnetlib
### • asyncssh - модуль asyncssh
### • asynctelnet - telnet клиент написанный с использованием asyncio

### Основные параметры подключения:
### • host - IP-адрес или имя хоста
### • auth_username - имя пользователя
### • auth_password - пароль
### • auth_secondary - пароль на enable
### • auth_strict_key - контролирует проверку SSH ключей сервера, а именно разрешать ли подключаться к серверам ключ которых не сохранен в ssh/known_hosts. False - разрешить подключение (по умолчанию значение True)
### • platform - нужно указывать при использовании Scrapli
### • transport - какой транспорт использовать
### • transport_options - опции для конкретного транспорта

from scrapli import Scrapli

r1 = {
    "host": "172.17.20.41",
    "auth_username": "ivankurop",
    "auth_password": "qweszxc",
    "auth_secondary": "qweszxc",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}
with Scrapli(**r1) as ssh:
    print(ssh.get_prompt())
    # ssh.open()
    # После этого можно отправлять команды:
    # ssh.get_prompt()
    # ssh.close()
# Пример подключения с использованием драйвера IOSXEDriver
from scrapli.driver.core import IOSXEDriver

r1_driver = {
    "host": "172.17.20.41",
    "auth_username": "ivankurop",
    "auth_password": "qweszxc",
    "auth_secondary": "qweszxc",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}
with IOSXEDriver(**r1_driver) as ssh:
    print(ssh.get_prompt())

### В scrapli есть несколько методов для отправки команд:
### • send_command - отправить одну show команду
### • send_commands - отправить список show команд
### • send_commands_from_file - отправить show команды из файла
### • send_config - отправить одну команду в конфигурационном режиме
### • send_configs - отправить список команд в конфигурационном режиме
### • send_configs_from_file - отправить команды из файла в конфигурационном режиме
### • send_interactive
### Все эти методы возвращают объект Response, а не вывод команды в виде строки.

reply = ssh.send_command("sh clock")
print(reply)
print(reply.result)

reply.result
# Атрибут raw_result содержит байтовую строку с полным выводом:
reply.raw_result
# Для команд, которые выполняются дольше обычных show, может быть необходимо знать время выполнения команды:
r = ssh.send_command("ping 10.1.1.1")
r.result
r.elapsed_time
r.start_time
r.finish_time
# Атрибут channel_input возвращает команду, которая была отправлена на оборудование:
r.channel_input

# Метод send_command
# Метод send_command позволяет отправить одну команду на устройство.
reply = ssh.send_command("sh clock")

### Параметры метода (все эти параметры надо передавать как ключевые):
### • strip_prompt - удалить приглашение из вывода. По умолчанию удаляется
### • failed_when_contains - если вывод содержит указанную строку или одну из строк в списке, будет считаться, что команда выполнилась с ошибкой
### • timeout_ops - максимальное время на выполнение команды, по умолчанию равно 30 секунд для IOSXEDriver

# Пример вызова метода send_command:
reply = ssh.send_command("sh clock")
reply

# Параметр timeout_ops указывает сколько ждать выполнения команды:
ssh.send_command("ping 8.8.8.8", timeout_ops=20)

# Если команда не выполнилась за указанное время, сгенерируется исключение ScrapliTimeout
ssh.send_command("ping 8.8.8.8", timeout_ops=2)

# scrapli также позволяет получить структурированный вывод, например, с помощью метода textfsm_parse_output:
reply = ssh.send_command("sh ip int br")
reply.textfsm_parse_output()

# Обнаружение ошибок
# Методы для отправки команд автоматически проверяют вывод на наличие ошибок. Для каждого вендора/типа оборудования это свои ошибки, плюс можно самостоятельно указать
ssh.failed_when_contains

reply = ssh.send_command("sh clck")
reply.result
reply
reply.failed

# Метод send_config - позволяет отправить одну команду конфигурационного режима.
r = ssh.send_config("username user1 password password1")

# scrapli удаляет команду из вывода, по умолчанию, при использовании send_config, в
# атрибуте result будет пустая строка (если не было ошибки при выполнении команды):
r.result

# Можно добавлять параметр strip_prompt=False и тогда в выводе появится приглашение:
r = ssh.send_config("username user1 password password1", strip_prompt=False)
r.result

### Методы send_commands, send_configs
### Методы send_commands, send_configs отличаются от send_command, send_config тем, что
### могут отправлять несколько команд. Кроме того, эти методы возвращают не Response, а
### MultiResponse, который можно в целом воспринимать как список Response

reply = ssh.send_commands(["sh clock", "sh ip int br"])
reply
for r in reply:
    print(r)
    print(r.result)

### При отправке нескольких команд также очень удобно использовать параметр stop_on_failed. По умолчанию он равен False, поэтому выполняются все команды, но если указать stop_on_failed=True, после возникновения ошибки в какой-то команде, следующие команды не будут выполняться:
reply = ssh.send_commands(["ping 192.168.100.2", "sh clck", "sh ip int br"], stop_on_failed=True)
reply
reply.result
for r in reply:
    print(r)
    print(r.result)