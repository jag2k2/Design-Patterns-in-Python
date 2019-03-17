from abc import ABC, abstractmethod


class VisualComponent(ABC):

    @abstractmethod
    def draw(self)->None:
        pass

    @abstractmethod
    def resize(self)->None:
        pass


class TextView(VisualComponent):

    def draw(self)->None:
        print("Drawing contents of TextView")

    def resize(self)->None:
        print("Resizing contents of TextView")


class Decorator(VisualComponent):

    def __init__(self, component: VisualComponent):
        self._component: VisualComponent = component    # enclose object into the decorator

    def draw(self)->None:
        self._component.draw()                          # forward request to the enclosed object

    def resize(self)->None:
        self._component.resize()                        # forward request to the enclosed object


class BorderDecorator(Decorator):

    def __init__(self, component: VisualComponent, border_width: int)->None:
        self._border_width: int = border_width
        super().__init__(component)

    def draw_border(self)->None:
        print("Drawing border with width " + str(self._border_width))

    def draw(self)->None:
        super().draw()
        self.draw_border()


glyph: VisualComponent = TextView()
glyph.draw()
glyph.resize()

border_dec: BorderDecorator = BorderDecorator(glyph, 3)   # wrap glyph into border_dec
border_dec.draw()       # border_dec has the same interface as glyph but modifies that object's capabilities


        


