from abc import ABC, abstractmethod
from typing import List


class Equipment(ABC):

    def __init__(self, name: str)->None:
        self._name = name
        self._parent: "Equipment" = None

    def add(self, component: "Equipment")->None:
        raise Exception("Cannot add components to leaves")

    def remove(self, component: "Equipment")->None:
        raise Exception("Cannot remove components from leaves")

    def name(self)->str:
        return self._name

    def set_parent(self, parent: "Equipment")->None:
        self._parent: "Equipment" = parent

    def clear_parent(self)->None:
        self._parent = None

    def get_parent(self)->"Equipment":
        return self._parent

    @abstractmethod
    def power(self)->int:
        pass

    @abstractmethod
    def net_price(self)->int:
        pass


class EquipGroup(Equipment):

    def __init__(self, name: str)->None:
        super().__init__(name)
        self._equip_list: List[Equipment] = []

    def add(self, component: "Equipment")->None:
        self._equip_list.append(component)
        component.set_parent(self)

    def remove(self, component: "Equipment")->None:
        self._equip_list.remove(component)
        component.clear_parent()

    def power(self)->int:
        power_sum: int = 0
        for i in self._equip_list:
            power_sum += i.power()
        return power_sum

    def net_price(self)->int:
        net_sum: int = 0
        for i in self._equip_list:
            net_sum += i.net_price()
        return net_sum


class Floppy(Equipment):
    _power = 15
    _net_price = 10

    def power(self)->int:
        return self._power

    def net_price(self)->int:
        return self._net_price


comp1 = Floppy("floppy1")
comp2 = Floppy("floppy2")
comp3 = Floppy("floppy3")
comp4 = Floppy("floppy4")
comp5 = Floppy("floppy5")
chassis1 = EquipGroup("chassis1")
chassis2 = EquipGroup("chassis2")

chassis1.add(comp1)
chassis1.add(comp2)
chassis1.add(chassis2)
chassis2.add(comp3)
chassis2.add(comp4)
chassis2.add(comp5)

print(comp1.net_price())
print(comp4.net_price())
print(chassis2.net_price())
print(chassis1.net_price())
print("")

try:
    comp1.add(comp2)
except Exception as err:
    print(err)
chassis2.remove(comp3)

print(comp1.net_price())
print(comp4.net_price())
print(chassis2.net_price())
print(chassis1.net_price())

print(comp5.get_parent().name())
print(chassis2.get_parent().name())

chassis2.remove(comp5)
try:
    print(comp5.get_parent().name())
except Exception as err:
    print(err)
    



