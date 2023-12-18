'''
Python for network engineers Natasha Samoilenko
'''
# Page range 426-450
# 18
# 18.1 Ввод пароля
# ##если использовать input(), набираемый пароль будет виден
# ##getpass позволяет запрашивать пароль, не отображая вводимые символы
import getpass
#password = getpass.getpass()
#print(password)

import os
#$ export SSH_USER=ivankurop
#$ export SSH_PASSWORD=qweszxc
USERNAME = os.environ.get('SSH_USER')
PASSWORD = os.environ.get('SSH_PASSWORD')
print(USERNAME)
print(PASSWORD)
# 18.2 pexpect
import pexpect
ssh = pexpect.spawn('ssh ivankurop@172.17.20.41')
print(ssh)
print(ssh.expect('[Pp]assword'))
print(ssh.sendline('qweszxc'))
print(ssh.expect('[>#]'))
print(ssh.sendline('enable'))
print(ssh.expect('[Pp]assword'))
print(ssh.sendline('qweszxc'))
print(ssh.expect('[>#]'))
print(ssh.sendline('sh ip int br'))
print(ssh.expect('#'))
print(ssh.before)
show_output = ssh.before.decode('utf-8')
print(show_output)
print(ssh.close())

import pexpect
p = pexpect.spawn('/bin/bash -c "ls -halF | grep ivankurop"')
p.expect(pexpect.EOF)
print(p.before)
print(p.before.decode('utf-8'))
p = pexpect.spawn('/bin/bash -c "ls -halF | grep test"')
#p.expect('nattaur')
p.expect(pexpect.EOF)
print(p.before)

p = pexpect.spawn('/bin/bash -c "ls -ls | grep test"')
p.expect(['test', pexpect.TIMEOUT, pexpect.EOF])
print(p.before)
# 18.3 telnetlib
###Плюс telnetlib в том, что этот модуль входит в стандартную библиотеку Python
import telnetlib
import pprint
telnet = telnetlib.Telnet('172.17.20.42')
print("-----------------------telnetlib------------")
print(telnet)
print(telnet.read_until(b'Username'))
print(telnet.write(b'ivankurop\n'))
print(telnet.read_until(b'Password'))
print(telnet.write(b'qweszxc\n'))
print(telnet.read_until(b'>'))
print(telnet.write(b'sh ip int br\n'))
print(telnet.read_until(b'>'))

print(telnet.write(b'sh arp\n'))
print(telnet.write(b'sh clock\n'))
print(telnet.write(b'sh ip int br\n'))
print(telnet.read_until(b'>'))
print(telnet.read_until(b'>'))
print(telnet.read_until(b'>'))

print(telnet.write(b'sh arp\n'))
print(telnet.read_until(b'>'))

print(telnet.read_until(b'>', timeout=5))#Метод read_until ждет определенную строку. eсли ее нет, метод «зависнет». timeout позволяет указать сколько ждать
print(telnet.read_very_eager())#read_very_eager просто вернет пустую строку, если вывода нет

print(telnet.write(b'sh arp\n'))
print(telnet.write(b'sh clock\n'))
print(telnet.write(b'sh ip int br\n'))
all_result = telnet.read_very_eager().decode('utf-8')
print(all_result)

telnet.write(b'sh clock\n')
telnet.expect([b'[>#]'])
telnet.write(b'sh clock\n')
regex_idx, match, output = telnet.expect([b'[>#]'])
print(regex_idx)
match.group()
print(output)
print(output.decode('utf-8'))
print(telnet.close())

# 18.4 paramiko
print("-----------------------paramiko------------")
import paramiko
import time
import socket
from pprint import pprint

short_pause=1
long_pause=5
client = paramiko.SSHClient()#defined class SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#defined policy for connection AutoAddPolicy()
print("-----------------------search here1------------")
client.connect(
    hostname="172.27.20.41",
    username="ivankurop",
    password="qweszxc",
    look_for_keys=False,
    allow_agent=False
)
print("-----------------------search here2------------")
with client.invoke_shell() as ssh:
    #ssh = client.invoke_shell()#invoke_shell позволяет установить интерактивную сессию SSH с сервером
    ssh.send("enable\n")
    print("-----------------------search here3------------")
    time.sleep(short_pause)
    ssh.send("qweszxc\n")
    time.sleep(short_pause)
    ssh.send("sh ip int br\n")
    time.sleep(short_pause)
    ssh.recv(3000)#В скобках указывается максимальное значение в байтах, которое нужно получить.
    ssh.close()
client.close()

# 18.5 netmiko
# 18.6 scrapli

