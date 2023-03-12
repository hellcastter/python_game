""" Game classes """
class Enemy:
    """ Enemy class """
    def __init__(self, name: str, description: str) -> None:
        self.__name = name
        self.__description = description
        self.__conversation = ""
        self.__weakness = ""
        self.__defeated = 0

    def describe(self):
        """let enemy describe themselves

        >>> enemy = Enemy("David", "A man")
        >>> enemy.describe()
        David is here!
        A man
        """
        print(f"{self.__name} is here!")
        print(self.__description)

    def set_conversation(self, conversation: str):
        """set what enemy says

        Args:
            conversation (str): message

        >>> enemy = Enemy("David", "A man")
        >>> enemy.set_conversation("test talk")
        >>> enemy._Enemy__conversation
        'test talk'
        """
        self.__conversation = conversation

    def set_weakness(self, weakness: str):
        """set weakness of enemy

        Args:
            weakness (str): any object

        >>> enemy = Enemy("David", "A man")
        >>> enemy.set_weakness("book")
        >>> enemy._Enemy__weakness
        'book'
        """
        self.__weakness = weakness

    def talk(self):
        """talk with enemy

        >>> enemy = Enemy("David", "A man")
        >>> enemy.set_conversation("test talk")
        >>> enemy.talk()
        [David says]: test talk.
        """
        print(f"[{self.__name} says]: {self.__conversation}.")

    def fight(self, fight_with: str) -> bool:
        """to fight with an enemy

        Args:
            fight_with (str): object (weapon) with what we fight

        Returns:
            bool: do we won or not

        >>> enemy = Enemy("David", "A man")
        >>> enemy.set_weakness("book")
        >>> enemy.fight("book")
        True
        >>> enemy.set_weakness("cheese")
        >>> enemy.fight("book")
        False
        """
        if self.__weakness == fight_with:
            self.__defeated += 1
            return True

        return False

    def get_defeated(self) -> int:
        """get how many times enemy was defeated

        Returns:
            int: times

        >>> enemy = Enemy("David", "A man")
        >>> enemy.get_defeated()
        0
        >>> enemy.set_weakness("cheese")
        >>> enemy.fight("cheese")
        True
        >>> enemy.get_defeated()
        1
        """
        return self.__defeated


class Item:
    """ Item class """
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__description = ""

    def set_description(self, description: str):
        """set description of item

        Args:
            description (str): description

        >>> banana = Item("banana")
        >>> banana.set_description("Yellow one")
        >>> banana._Item__description
        'Yellow one'
        """
        self.__description = description

    def describe(self):
        """get description of person

        >>> banana = Item("banana")
        >>> banana.set_description("Yellow one")
        >>> banana.describe()
        The [banana] is here — Yellow one
        """
        print(f"The [{self.__name}] is here — {self.__description}")

    def get_name(self) -> str:
        """get item name

        Returns:
            str: name

        >>> banana = Item("banana")
        >>> banana._Item__name
        'banana'
        """
        return self.__name


class Room:
    """ Room class """
    def __init__(self, name) -> None:
        self.__name = name
        self.__linked_rooms: dict[str, Room] = {}
        self.__description = ""
        self.character: Enemy | None = None
        self.__item: Item | None = None

    def link_room(self, room, location: str):
        """set linked room

        Args:
            room (Room): some room
            location (str): where is it located

        >>> room = Room('bathroom')
        >>> room1 = Room('balcony')
        >>> room.link_room(room1, 'south')
        >>> room._Room__linked_rooms['south'].get_name()
        'balcony'
        """
        self.__linked_rooms[location] = room

    def set_description(self, description: str):
        """set description

        Args:
            description (str): description

        >>> room = Room('bathroom')
        >>> room.set_description("with water")
        >>> room._Room__description
        'with water'
        """
        self.__description = description

    def set_character(self, character: Enemy):
        """set character

        Args:
            character (Enemy): character

        >>> room = Room('bathroom')
        >>> room.set_character( Enemy("david", "a man") )
        >>> room.character._Enemy__name
        'david'
        """
        self.character = character

    def set_item(self, item: Item):
        """throw some item to room

        Args:
            item (Item): item

        >>> room = Room('bathroom')
        >>> room.set_item( Item("banana") )
        >>> room._Room__item._Item__name
        'banana'
        """
        self.__item = item

    def get_details(self):
        """get details of the room

        >>> room = Room('bathroom')
        >>> room.set_description('with water')
        >>> room.link_room(Room('balcony'), 'south')
        >>> room.get_details()
        bathroom
        --------------------
        with water
        The balcony is south
        """
        print(self.__name)
        print("--------------------")
        print(self.__description)
        print(
            *(f"The {r.get_name()} is {d}" for d, r in self.__linked_rooms.items()),
            sep="\n"
        )

    def get_name(self) -> str:
        """get name of the room

        Returns:
            str: room name

        >>> room = Room('bathroom')
        >>> room.get_name()
        'bathroom'
        """
        return self.__name

    def get_item(self) -> Item:
        """get item from room

        Returns:
            Item: item from room

        >>> room = Room('bathroom')
        >>> room.get_item()
        >>> room.set_item( Item('banana') )
        >>> room.get_item().get_name()
        'banana'
        """
        return self.__item

    def get_character(self) -> Enemy:
        """get character from room

        Returns:
            Enemy: character

        >>> room = Room('balcony')
        >>> room.get_character()
        """
        return self.character

    def move(self, direction: str):
        """move to other room

        Args:
            direction (str): where to move

        Returns:
            Room: room where to move

        >>> room = Room('balcony')
        >>> room.move('south')
        You can't go south
        """
        if direction in self.__linked_rooms:
            return self.__linked_rooms[direction]

        print(f"You can't go {direction}")
