# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os
#$ python cfg_gen.py templates/for.txt data_files/for.yml
template_dir, template_file = os.path.split(sys.argv[1])

vars_file = sys.argv[2]

#Переводы строк появляются из-за блока for.
#trim_blocks удаляет первую пустую строку после блока конструкции, если его значение равно True (по умолчанию False).
#lstrip_blocks контролирует то, будут ли удаляться пробелы и табы от начала строки до начала блока (до открывающейся фигурной скобки).
#
env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True,#
    lstrip_blocks=True)#
template = env.get_template(template_file)

with open(vars_file) as f:
    vars_dict = yaml.safe_load(f)

print(template.render(vars_dict))
'''
PS D:\Literature\Python\PyMyProgNatenka1\page509-541_20-jinja2> python page514-V-20-cfg_gen.py templates/page520-V-20-va
riables.txt data_files/page520-V-20-vars.yml
hostname R3

interface Loopback0
 ip address 10.0.0.3 255.255.255.255

vlan 10

router ospf 1
 router-id 10.0.0.3
 auto-cost reference-bandwidth 10000
 network 10.0.1.0 0.0.0.255 area 0
'''