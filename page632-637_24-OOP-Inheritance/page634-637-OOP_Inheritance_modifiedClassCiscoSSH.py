# -*- coding: utf-8 -*-
# Natasha Samoilenko
# IV OOP
# 24. Наследование
# ConnectSSH
# page634-637
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


class CiscoSSH(ConnectSSH):
    '''
    3 вариантa вызова родительского метода, например, все эти варианты вызовут метод
    send_show_command родительского класса из дочернего класса CiscoSSH:

        command_result = ConnectSSH.send_show_command(self, command)
            command_result = super(CiscoSSH, self).send_show_command(command)
                command_result = super().send_show_command(command)

    Метод __init__ в классе CiscoSSH добавил параметры enable_password и disable_paging, и
    использует их соответственно для перехода в режим enable и отключения постраничного вывода
    '''

    def __init__(self, ip, username, password, enable_password,
                 disable_paging=True):
        super().__init__(ip, username, password)
        self._ssh.send('enable\n')
        self._ssh.send(enable_password + '\n')
        if disable_paging:
            self._ssh.send('terminal length 0\n')
        time.sleep(1)
        self._ssh.recv(self._MAX_READ)
        '''
        Еще один метод, который стоит доработать - метод send_config_commands: так как класс
        CiscoSSH предназначен для работы с Cisco, можно добавить в него переход в конфигураци-
        онный режим перед командами и выход после
        '''

    def config_mode(self):
        self._ssh.send('conf t\n')
        time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode('ascii')
        return result

    def exit_config_mode(self):
        self._ssh.send('end\n')
        time.sleep(0.5)
        result = self._ssh.recv(self._MAX_READ).decode('ascii')
        return result

    def send_config_commands(self, commands):
        result = self.config_mode()
        result += super().send_config_commands(commands)
        result += self.exit_config_mode()
        return result


if __name__ == "__main__":
    r1 = CiscoSSH('172.17.20.41', 'ivankurop', 'qweszxc', 'qweszxc')
    print(r1.send_show_command('sh clock'))
    print(r1.send_config_commands(
        ['interface loopback 33',
         'ip address 3.3.3.3 255.255.255.255']
    ))
