'''
Python for network engineers Natasha Samoilenko
'''
# Page range 493
# 19
### 19.6
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
from datetime import datetime
import time
import logging
import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException
logging.getLogger("paramiko").setLevel(logging.WARNING)
logging.basicConfig(
    format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
    level=logging.INFO)

def send_show(device_dict, command):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    ip = device_dict['host']
    logging.info(start_msg.format(datetime.now().time(), ip))
    if ip == '172.17.20.41': time.sleep(5)
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
        logging.info(received_msg.format(datetime.now().time(), ip))
    return {ip: result}

with open('page485_19_devices.yaml') as f:
    devices = yaml.safe_load(f)
with ThreadPoolExecutor(max_workers=2) as executor:
    future_list = []
    for device in devices:
        future = executor.submit(send_show, device, 'sh clock')
        future_list.append(future)
    for f in future_list:
        print(f.result())