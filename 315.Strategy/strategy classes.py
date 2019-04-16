from abc import ABC, abstractmethod
from typing import List


class Coord:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


class StrategyInterface(ABC):

    @abstractmethod  # the method is called within the composition and the parameters are calculated there
    def execute(self, component_count: int) -> int:
        pass


class Simple(StrategyInterface):
    def execute(self, component_count: int) -> int:
        print("Performing Simple algorithm on " + str(component_count) + " components")
        return 0


class TeX(StrategyInterface):
    def execute(self, component_count: int) -> int:
        print("Performing TeX algorithm on " + str(component_count) + " components")
        return 1


class Array(StrategyInterface):
    def execute(self, component_count: int) -> int:
        print("Performing Array algorithm on " + str(component_count) + " components")
        return 2


class DataObject:

    def __init__(self) -> None:
        self._strategy = None
        self._components: List[str] = ["Big Bear", "Mama Bear", "Baby Bear"]

    def set_alg(self, strategy: StrategyInterface):
        self._strategy = strategy

    def repair(self) -> None:
        self._strategy.execute(len(self._components))


algorithm1 = Array()  # instantiate a concrete algorithm
algorithm2 = Simple()  # instantiate a second concrete algorithm
structure = DataObject()  # instantiate a data object
structure.set_alg(algorithm1)
structure.repair()
structure.set_alg(algorithm2)
structure.repair()
