from abc import ABC, abstractmethod


class VisualComponent(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass


class TextView(VisualComponent):

    def draw(self) -> None:
        print("Drawing contents of TextView")


class Decorator(VisualComponent):

    def __init__(self, component: VisualComponent):
        self._component: VisualComponent = component    # enclose object into the decorator

    @abstractmethod
    def draw(self) -> None:
        self._component.draw()                          # forward request to the enclosed object


class BorderDecorator(Decorator):

    def __init__(self, component: VisualComponent) -> None:
        self._border_width = 0
        super().__init__(component)

    def set_border(self, border_width: int) -> None:
        self._border_width = border_width

    def draw(self) -> None:
        print("Doing something first.")
        super().draw()                    # call the wrapped function
        print("Do something after: Drawing border with width " + str(self._border_width))


glyph: VisualComponent = TextView()
glyph.draw()
print("")

border_dec: BorderDecorator = BorderDecorator(glyph)   # wrap glyph into border_dec
border_dec.set_border(3)
border_dec.draw()       # border_dec has the same interface as glyph but modifies that object's capabilities


        


