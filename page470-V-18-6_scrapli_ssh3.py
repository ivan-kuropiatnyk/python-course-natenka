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
    "host": "172.17.20.41",
    "auth_username": "ivankurop",
    "auth_password": "qweszxc",
    "auth_secondary": "qweszxc",
    "auth_strict_key": False,
    "platform": "cisco_iosxe"
}
def send_cfg(device, cfg_commands, strict=False):
    output = ""
    if type(cfg_commands) == str:
        cfg_commands = [cfg_commands]
    with Scrapli(**device) as ssh:
        reply = ssh.send_configs(cfg_commands, stop_on_failed=strict)
        for cmd_reply in reply:
            if cmd_reply.failed:
                print(f"При выполнении команды возникла ошибка:\n{reply.result}\n")
        output = reply.result
    return output
if __name__ == "__main__":
    output_cfg = send_cfg(r1, ["interface lo11", "ip address 11.1.1.1 255.255.255.255"], strict=True)
    print(output_cfg)