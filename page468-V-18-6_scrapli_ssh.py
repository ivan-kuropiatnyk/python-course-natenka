'''
Python for network engineers Natasha Samoilenko
'''
# Page range 450-471
# 18
# 18.6 scrapli
### Подключение telnet - Для подключения к оборудовани по Telnet надо указать transport равным telnet и обязательно указать параметр port равным 23 :
from scrapli.driver.core import IOSXEDriver
from scrapli.exceptions import ScrapliException
import socket
r1 = {
    "host": "172.17.20.4",
    "auth_username": "ivankurop",
    "auth_password": "qweszxc",
    "auth_secondary": "qweszxc",
    "auth_strict_key": False,
    "timeout_socket": 5, # timeout for establishing socket/initial connection
    "timeout_transport": 10, # timeout for ssh|telnet transport
}

def send_show(device, show_command):
    try:
        with IOSXEDriver(**device) as ssh:
            reply = ssh.send_command(show_command)
            return reply.result
    except socket.timeout as error:
        print(error)
    except ScrapliException as error:
        print(error, device["host"])
if __name__ == "__main__":
    output = send_show(r1, "sh ip int br")
    print(output)