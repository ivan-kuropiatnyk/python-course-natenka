# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 24. Наследование
# ConnectSSH
# page632 -633
import paramiko
import time
class ConnectSSH:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self._MAX_READ = 10000
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=ip,
            username=username,
            password=password,
            look_for_keys=False,
            allow_agent=False)
        self._ssh = client.invoke_shell()
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self._ssh.close()
    def close(self):
        self._ssh.close()
    def send_show_command(self, command):
        self._ssh.send(command + '\n')
        time.sleep(2)
        result = self._ssh.recv(self._MAX_READ).decode('ascii')
        return result

    def send_config_commands(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        for command in commands:
            self._ssh.send(command + '\n')
            time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode('ascii')
        return result

class CiscoSSH(ConnectSSH):#создан новый класс CiscoSSH который наследует все методы и аргументы у класса ConnectSSH
    pass

if __name__ == "__main__":
    r1 = CiscoSSH('172.17.20.41', 'ivankurop', 'qweszxc')
    print(r1.ip)
    print("_MAX_READ:", r1._MAX_READ)
    print(r1.send_show_command('sh ip int br'))
    print(r1.send_show_command('enable'))
    print(r1.send_show_command('qweszxc'))
    print(r1.send_config_commands(
        ['conf t',
         'int loopback 33',
         'ip address 3.3.3.3 255.255.255.255',
         'end']
    ))
'''
    После наследования всех методов родительского класса, дочерний класс может:
        • оставить их без изменения
        • полностью переписать их
        • дополнить метод
        • добавить свои методы
'''
