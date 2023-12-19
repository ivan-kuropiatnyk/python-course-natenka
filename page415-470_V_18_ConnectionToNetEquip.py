'''
Python for network engineers Natasha Samoilenko
'''
# Page range 426-470
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

# 18.3 telnetlib
# 18.4 paramiko
# 18.5 netmiko
# 18.6 scrapli