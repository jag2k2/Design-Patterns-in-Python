from abc import ABC, abstractmethod


class Point:

    def __init__(self, x: int, y: int):

        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y


class Window(ABC):

    def __init__(self) -> None:
        self._imp: WindowImp = None

    def draw_rect(self, a: Point, b: Point) -> None:
        self._imp.draw_dev_rectangle(a.get_x(), a.get_y(), b.get_x(), b.get_y())


class ApplicationWindow(Window):
    pass


class IconWindow(Window):
    pass


class WindowImp(ABC):

    @abstractmethod
    def draw_dev_rectangle(self, a: int, b: int, c: int, d: int) -> None:
        pass


class XWindowImp(WindowImp):

    def draw_dev_rectangle(self, a: int, b: int, c: int, d: int) -> None:
        print("Drawing rectangle for Xwin")


class PMWindowImp(WindowImp):
    def draw_dev_rectangle(self, a: int, b: int, c: int, d: int) -> None:
        print("Drawing rectangle for PMWin")


