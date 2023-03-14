""" Location module """
from typing import Literal
from characters import Character

from item import Item

DIRECTIONS = Literal["північ", "південь", "захід", "схід"]

class Location:
    """ Location """
    def __init__(self, name, description = "") -> None:
        self.name = name
        self.character: Character = None
        self.__linked: dict[DIRECTIONS, Location] = {}
        self.__description = description
        self.item: Item = None

    def link_location(self, direction: DIRECTIONS, location):
        """ Add linked location to current """
        self.__linked[direction] = location

    def move(self, direction: DIRECTIONS):
        """ move to next location """
        if direction in self.__linked:
            return self.__linked[direction]

        print(f"Ви не можете піти на {direction}")
        return self


    def describe(self):
        """ describe current location """
        print(self.name)
        print("----------------------------")
        print(self.__description)

        if self.item:
            print(f"На локації є {self.item.describe()}")

        if self.character:
            print(f"На локації є {self.character.name}")

        print(
            *(f"{l.name} — потрібно йти на {d}" for d, l in self.__linked.items()),
            sep="\n"
        )

    def get_inhabitant(self):
        """ get character from current location """
        return self.character
