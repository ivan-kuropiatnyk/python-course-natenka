t1 = {
    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/2'): ('R5', 'Eth0/0')
}

t2 = {
    ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
    ('R1', 'Eth0/6'): ('R9', 'Eth0/0')
}

t3 = {}
t3.update(t1)
t3.update(t2)
print(t3)