'''
Python for network engineers Natasha Samoilenko
'''
# Page range 469
# 18
# 18.6 scrapli
### Подключение telnet - Для подключения к оборудовани по Telnet надо указать transport равным telnet и обязательно указать параметр port равным 23 :
from pprint import pprint
from scrapli import Scrapli

r1 = {
    "host": "172.17.20.4",
    "auth_username": "ivankurop",
    "auth_password": "qweszxc",
    "auth_secondary": "qweszxc",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}
def send_show(device, show_commands):
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    with Scrapli(**device) as ssh:
        for cmd in show_commands:
            reply = ssh.send_command(cmd)
    cmd_dict[cmd] = reply.result
    return cmd_dict

if __name__ == "__main__":
    print("show".center(20, "#"))
    output = send_show(r1, ["sh ip int br", "sh ver | i uptime"])
    pprint(output, width=120)