'''
Python for network engineers Natasha Samoilenko
'''
# Page range 435
# 18
# 18.2 pexpect  MORE- пример с постраничным выводом
import pexpect
import re
from pprint import pprint
import time
def send_show_command(ip, username, password, enable, command, prompt="#"):
    with pexpect.spawn(f"ssh {username}@{ip}", timeout=45, encoding="utf-8") as ssh:
        ssh.expect("[Pp]assword")
        ssh.sendline(password)
        enable_status = ssh.expect([">", "#"])
        if enable_status == 0:
            ssh.sendline("enable")
            ssh.expect("[Pp]assword")
            ssh.sendline(enable)
            ssh.expect(prompt)
        ssh.sendline(command)
        time.sleep(5)
        output = ""
        while True:
            match = ssh.expect(["#", "--More--", pexpect.TIMEOUT])
            page = ssh.before.replace("\r\n", "\n")
            page = re.sub(" +\x08+ +\x08+", "\n", page)
            output += page
            if match == 1:
                ssh.send(" ")
                time.sleep(5)
            else:
                print("Ошибка: timeout")
            break
            output = re.sub("\n +\n", "\n", output)
        return output
if __name__ == "__main__":
    devices = ["172.17.20.41", "172.17.20.42", "172.17.20.43"]
    for ip in devices:
        result = send_show_command(ip, "ivankurop", "qweszxc", "qweszxc", "sh run")
        with open(f"page435_18_{ip}_result.txt", "w") as f:
            f.write(result)
        pprint(result, width=120)