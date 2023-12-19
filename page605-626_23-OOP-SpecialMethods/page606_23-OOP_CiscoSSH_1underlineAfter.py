# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 23. Специальные методы
# Подчеркивание в именах
# Одно подчеркивание перед именем
# page605 - Для начала импортируем класс clitable
'''
    После создания экземпляра класса, доступен не только метод send_show_command, но и ат-
рибуты client и ssh
    Если же необходимо указать, что client и ssh являются внутренними атрибутами, которые
нужны для работы класса, но не предназначены для пользователя, надо поставить нижнее
подчеркивание перед именем: file => page606

    '''
import time
import paramiko

class CiscoSSH:
    def __init__(self, ip, username, password, enable, disable_paging=True):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False)
        self._ssh = self._client.invoke_shell()
        self._ssh.send('enable\n')
        self._ssh.send(enable + '\n')
        if disable_paging:
            self._ssh.send('terminal length 0\n')
        time.sleep(1)
        self._ssh.recv(1000)

    def send_show_command(self, command):
        self._ssh.send(command + '\n')
        time.sleep(2)
        result = self._ssh.recv(5000).decode('ascii')
        return result

if __name__ == "__main__":
    r1 = CiscoSSH('172.17.20.41', 'ivankurop', 'qweszxc', 'qweszxc')
    print("\nCLIENT\n", r1._client)
    print("\nSH COMMAND\n",r1.send_show_command('sh clock'))
    print("\nSSH\n",r1._ssh)