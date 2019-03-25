from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3


class MapSite(ABC):
    @abstractmethod
    def enter(self)->None:
        pass


class Room(MapSite):

    _room_num: int
    _sides: List[MapSite] = []

    def __init__(self, room_no: int)->None:
        self._room_num = room_no

    def get_room_no(self)->int:
        return self._room_num

    def get_side(self, direction: Direction)->None:
        # print("Getting side for " + str(self._room_num) + " in the " + str(direction) + " direction")
        pass

    def set_side(self, direction: Direction, neighbor: MapSite)->None:
        print("Setting side '" + str(direction) + "' to " + str(neighbor) + " for room " + str(self._room_num))

    def enter(self)->None:
        pass


class Wall(MapSite):

    def enter(self)->None:
        pass


class Door(MapSite):

    _roomIn: MapSite = Room(0)
    _roomOut: MapSite = Room(0)
    _isOpen: bool

    def __init__(self, room_in: MapSite, room_out: MapSite)->None:
        self._roomIn = room_in
        self._roomOut = room_out

    def other_side_from(self, this_room: MapSite)->MapSite:
        pass

    def enter(self)->None:
        pass


class Maze:

    def __init__(self) -> None:
        self._room_list: [Room] = []

    def add_room(self, room: Room)->None:
        self._room_list.append(room)

    def room_no(self, room_no: int)->Room:
        for i in self._room_list:
            if i.get_room_no() == room_no:
                return i
        return None


class MazeGame:

    '''
    The factory method is below.  
    
    If create_maze() calls abstract methods instead of constructors for room/walls/doors then we can make a subclass for 
    MazeGame and change the classes that are created.  Factory Method
    
    If create_maze() is passed an object parameter then we could change which rooms/walls/doors are used as a family.  
    Abstract Factory
    
    
    '''

    def __init__(self)->None:
        self._maze_main = None

    def create_maze(self)->Maze:        # this is the factory method!
        self._maze_main = Maze()
        r1: Room = Room(1)
        r2: Room = Room(2)
        the_door: Door = Door(r1, r2)

        self._maze_main.add_room(r1)
        self._maze_main.add_room(r2)

        r1.set_side(Direction.North, Wall())
        r1.set_side(Direction.East, the_door)
        r1.set_side(Direction.South, Wall())
        r1.set_side(Direction.West, Wall())

        r2.set_side(Direction.North, Wall())
        r2.set_side(Direction.East, Wall())
        r2.set_side(Direction.South, Wall())
        r2.set_side(Direction.West, the_door)

        return self._maze_main


game = MazeGame()
game_board = game.create_maze()

