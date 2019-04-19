from abc import ABC, abstractmethod
from typing import List

"Defines the encapsulated quack behavior"


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("Can't make noise!")


"Defines the encapsulated flying behavior"


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Flying with its wings!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("Can't fly!!")


class Duck(ABC):

    def __init__(self):
        self._quack_behavior = None
        self._fly_behavior = None

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    @abstractmethod
    def info(self):
        pass


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyWithWings()
        self._quack_behavior = Quack()

    def info(self):
        print("This is a Mallard Duck")


class RubberDuck(Duck):

    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyNoWay()
        self._quack_behavior = Squeak()

    def info(self):
        print("This is a Rubber Ducky")


class DecoyDuck(Duck):

    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyNoWay()
        self._quack_behavior = MuteQuack()

    def info(self):
        print("This is just a decoy")


flock: List[Duck] = []

flock.append(MallardDuck())
flock.append(RubberDuck())
flock.append(DecoyDuck())

for i in flock:
    print("")
    i.info()
    i.perform_fly()
    i.perform_quack()
