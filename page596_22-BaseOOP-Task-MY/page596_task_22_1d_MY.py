# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует
"""
class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        correct_topo = {}
        for key, value in topology_dict.items():
            if correct_topo.get(key) != value and correct_topo.get(value) != key:
                correct_topo[key] = value
            else:
                pass
        return correct_topo

    def delete_link(self, link_from, link_to):
        if self.topology.get(link_from) == link_to:
            print(f"{link_from}:{link_to} will be deleted")
            del self.topology[link_from]
        elif self.topology.get(link_to) == link_from:
            print(f"{link_to}:{link_from} will be deleted")
            del self.topology[link_to]
        else:
            print("Такого соединения нет")
        return self.topology

    def delete_node(self, hostname):
        count_for = 0#count iterations in cycle_1
        count_del = 0#count deletions in cycle_1
        topo_to_delete = {}
        for link_from, link_to in self.topology.items():#this cycle_1 verifies when asked hostname in the dictionary
            count_for += 1
            if link_from[0] == hostname or link_to[0] == hostname:
                print(f"{link_from}:{link_to} will be deleted")
                topo_to_delete[link_from] = link_to
                count_del += 1
        if count_for > 0 and count_del == 0:#if after all iterations in cyle_1 any count_del was added then the hostname is not in the dictionary
            print(f"Such device {hostname} is absent")
        else:
            for link_to_del in topo_to_delete.keys():#this cycle_2 takes all keys which we have in topo_to_delete and delete it from necessary topology
                del self.topology[link_to_del]
        return self.topology

    def add_link(self, link_from, link_to):
        if self.topology.get(link_from) == link_to or self.topology.get(link_to) == link_from:
            print(f"{link_from}:{link_to} Такое соединение существует")
        elif self.topology.get(link_from) != None or self.topology.get(link_to) != None:
            print(f"{link_to}:{link_from} Cоединение с одним из портов существует")
        elif link_to in self.topology.values() or link_from in self.topology.values():
            print(f"{link_to}:{link_from} Cоединение с одним из портов существует")
        else:
            print(f"{link_to}:{link_from} - added to topology")
            self.topology[link_from] = link_to
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
    topo.add_link(('SW1', 'Eth0/1'), ('R1', 'Eth0/0'))
    topo.add_link(('R1', 'Eth0/0'), ('SW55', 'Eth0/55'))
    topo.add_link(('SW55', 'Eth0/55'), ('R4', 'Eth0/0'))
    topo.add_link(('R77', 'Eth0/4'), ('R99', 'Eth0/0'))
    print(topo.topology)