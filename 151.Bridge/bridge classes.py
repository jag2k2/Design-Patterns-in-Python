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
        self._imp: WindowImp = PMWindowImp()
        self._imp = None
        self._imp = self.get_window_imp()

    def get_window_imp(self) -> "WindowImp":
        if self._imp is None:
            print("Creating implementation class")
            return PMWindowImp()
        else:
            print("Using stored implementation class")
            return self._imp

    # This method uses a composed class to bridge the Window interface to the WindowImp interface
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
        print("Drawing rectangle for Xwin from " + str(a) + "," + str(b) + " to " + str(c) + "," + str(d))


class PMWindowImp(WindowImp):
    def draw_dev_rectangle(self, a: int, b: int, c: int, d: int) -> None:
        print("Drawing rectangle for PMWin from " + str(a) + "," + str(b) + " to " + str(c) + "," + str(d))


p1 = Point(1, 2)
p2 = Point(3, 4)

win_obj = ApplicationWindow()
win_obj.get_window_imp()
win_obj.draw_rect(p1, p2)