'''
Python for network engineers Natasha Samoilenko
'''
# Page range 426-470
# 18
# 18.3 telnetlib
import telnetlib
import time
import re
from pprint import pprint

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

def send_show_command(ip, username, password, enable, command):
    with telnetlib.Telnet(ip) as telnet:
        telnet.read_until(b"Username")
        telnet.write(to_bytes(username))
        telnet.read_until(b"Password")
        telnet.write(to_bytes(password))
        index, m, output = telnet.expect([b">", b"#"])
        if index == 0:
            telnet.write(b"enable\n")
            telnet.read_until(b"Password")
            telnet.write(to_bytes(enable))
            telnet.read_until(b"#", timeout=5)
        telnet.write(b"terminal length 0\n")
        telnet.read_until(b"#", timeout=5)
        time.sleep(3)
        telnet.read_very_eager()
        telnet.write(to_bytes(command))
        result = ""
        while True:
            index, match, output = telnet.expect([b"--More--", b"#"], timeout=5)
            output = output.decode("utf-8")
            output = re.sub(" +--More--| +\x08+ +\x08+", "\n", output)
            result += output
            if index in (1, -1):
                break
            telnet.write(b" ")
            time.sleep(1)
            result.replace("\r\n", "\n")
        return result

if __name__ == "__main__":
    devices = ["172.17.20.41", "172.17.20.42", "172.17.20.43"]
    for ip in devices:
        result = send_show_command(ip, "ivankurop", "qweszxc", "qweszxc", "sh run")
        pprint(result, width=120)