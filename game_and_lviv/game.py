import sys

from characters import Enemy, Friend, Hero
from item import Good
from location import Location

DIRECTIONS = ("північ", "південь", "захід", "схід")

class Game:
    """ Game class """
    def __init__(
        self,
        start_location: Location,
        end_location: Location
    ) -> None:
        self.location = start_location
        self.end_location = end_location

    def __input(self):
        return input("> ").lower()

    def main_loop(self):
        """ main loop of the game """
        print("Привіт. Твоя ціль дійти до \"Доброго друга\" та відпочити зі своїми друзями!")
        print("Ти можеш виконати одну з наступних команд:")
        print("північ, південь, захід, схід — піти у заданому напрямку.")
        print("поговорити — поговорити з героями.")
        print("взяти — взяти предмет на локації.")
        print("втекти — спробувати втекти від злодія.")
        print("потоваришувати — завести нового друга.")
        print("exit — завершити гру.")

        print()
        print("Перш за все, як тебе звати?")
        hero = Hero(name=self.__input())

        print(f"Привіт, {hero.name}!")
        print(f"У тебе є {hero.money} грошей, щоб повеселитися.")
        print("Твоя поточна локація:")

        while True:
            self.location.describe()

            inp = self.__input()
            inhabitant = self.location.get_inhabitant()
            item = self.location.item

            if inp in DIRECTIONS:
                self.location = self.location.move(inp)

                if self.location == self.end_location:
                    print("Ура! Ви дійшли до місця призначення. Повеселіться добре з друзями!")
                    print(f"У тебе лишилося {hero.money} гривень.")
                    break
            elif inp == 'поговорити':
                if inhabitant:
                    inhabitant.talk()
                else:
                    print("Тут немає з ким поговорити.")
            elif inp == 'взяти':
                if item:
                    if isinstance(item, Good):
                        hero.buy(item)
                    else:
                        hero.put_in_backpack(item)
                else:
                    print("Тут нема чого взяти.")

            elif inp == 'потоваришувати':
                if inhabitant and isinstance(inhabitant, Friend):
                    print("Ви успішно завели нового друга.")
                else:
                    print("Немає з ким товаришувати.")

            elif inp == 'втекти':
                if inhabitant and isinstance(inhabitant, Enemy):
                    print("Ви успішно втекли від недруга.")
                else:
                    print("Немає від кого втікати.")
            elif inp == 'exit':
                sys.exit()
            else:
                print("Невідома команда.")

            print()
            print()
        