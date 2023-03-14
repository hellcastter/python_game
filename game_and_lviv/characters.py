""" Characters """
from item import Good, Item


class Character:
    """ Any character class """
    def __init__(self, name, speech = "") -> None:
        self.name = name
        self.__speech = speech

    def talk(self):
        """ say a speech """
        print(f"[{self.name}]: {self.__speech}")


class Enemy(Character):
    """ Class of enemy """


class Friend(Character):
    """ Class of friend """


class Hero(Character):
    """ Class of main hero """
    def __init__(self, name, speech="") -> None:
        super().__init__(name, speech)
        self.__backpack = []
        self.money = 200

    def put_in_backpack(self, item: Item):
        """ append item to backpack """
        print("Ти поклав предмет у рюкзак.")
        self.__backpack.append(item)

    def buy(self, item: Good):
        """ buy item if you can afford it """
        if self.money > item.price:
            self.money -= item.price
            self.__backpack.append(item)
            print(f"Ти купив {item.name} за {item.price}")
        else:
            print("У тебе не хватає коштів.")
