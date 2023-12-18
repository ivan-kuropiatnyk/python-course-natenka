# -*- coding: utf-8 -*-
"""
Задание 22.1

Создать класс Topology, который представляет топологию сети.

При создании экземпляра класса, как аргумент передается словарь,
который описывает топологию. Словарь может содержать "дублирующиеся" соединения.
Тут "дублирующиеся" соединения, это ситуация когда в словаре есть два соединения:
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

Задача оставить только один из этих линков в итоговом словаре, не важно какой.

В каждом экземпляре должна быть создана переменная topology, в которой содержится
словарь топологии, но уже без "дублей". Переменная topology должна содержать словарь
без "дублей" сразу после создания экземпляра.

Пример создания экземпляра класса:
In [2]: top = Topology(topology_example)

После этого, должна быть доступна переменная topology:

In [3]: top.topology
Out[3]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""
class Topology:
    def __init__(self,dict_data):
        self.dict_data = dict_data#entered(received) topology for ex topology_example
        self.topology = {}#topology outgoing where repeated elements was deleted
    def del_repeat(self):
        for key, value in self.dict_data.items():
            if self.topology.get(key) != value and self.topology.get(value) != key:
                self.topology[key] = value
            else:
                pass
        return self.topology
if __name__ == "__main__":
    topology_example = {
        ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')
    }
    topo = Topology(topology_example)
    topo.del_repeat()
    print(topo.topology)