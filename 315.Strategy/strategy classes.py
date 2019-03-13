from abc import ABC, abstractmethod
from typing import List


class Coord:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


class Compositor(ABC):

    @abstractmethod              # the method is called within the composition and the parameters are calculated there
    def compose(self, component_count: int) -> int:
        pass


class Simple(Compositor):
    def compose(self, component_count: int) -> int:
        print("Performing simple algorithm on " + str(component_count) + " components")
        return 0


class TeX(Compositor):
    def compose(self, component_count: int) -> int:
        print("Performing TeX algorithm on " + str(component_count) + " components")
        return 1


class Array(Compositor):
    def compose(self, component_count: int) -> int:
        print("Performing TeX algorithm on " + str(component_count) + " components")
        return 2


class Composition:

    def __init__(self, strategy: Compositor):
        self._strategy: Compositor = strategy
        self._components: List[str] = []

    def repair(self) -> None:
        self._components = ["Big Bear", "Mama Bear", "Baby Bear"]
        self._strategy.compose(len(self._components))


alg: Compositor = TeX()
structure: Composition = Composition(alg)
structure.repair()
