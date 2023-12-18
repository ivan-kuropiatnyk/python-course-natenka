# -*- coding: utf-8 -*-

"""
Задание 22.1c

Изменить класс Topology из задания 22.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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
    topo.delete_node('SWASD1')
    topo.delete_node('SW1')
    topo.delete_node('R2')
    print(topo.topology)