""" Main module """
from location import Location
from item import Good, Item
from characters import Enemy, Friend
from game import Game

if __name__ == "__main__":
    # Create locations
    ucu = Location(
        "Український католицький університет",
        "Найкращий університет України за версією усіх нормальних людей."
    )
    str_stryjska = Location("вул. Стрийська", "Одна з найдовших вулиць Львова.")
    str_franka = Location("вул. Івана Франка", "Вулиця, яка з'єднує УКУ та центр.")
    str_hryshevskoho = Location(
        "вул. Михайла Грушевського",
        "Можна вийти на проспект Шевченка та до пам'ятника Грушевському."
    )
    av_shevchenka = Location("Проспект Тараса Шевченка", "Бульвар, на якому стоїть МакДональдс.")
    str_valova = Location("вул. Валова", "Гарна вуличка, на якій ще стоїть Собор.")
    str_halytska = Location("вул. Галицька", "Йдемо від коня до площі Ринок.")
    sq_rynok = Location("Площа Ринок", "Найколоритніше місце Львова.")
    g_friend = Location("Добрий друг", "Місце для хорошого відпочинку.")

    ucu.link_location("північ", str_stryjska)
    ucu.link_location("південь", str_franka)
    str_stryjska.link_location("південь", ucu)
    str_stryjska.link_location("захід", str_franka)
    str_franka.link_location("схід", str_stryjska)
    str_franka.link_location("північ", ucu)
    str_franka.link_location("захід", str_hryshevskoho)
    str_franka.link_location("південь", str_valova)
    str_hryshevskoho.link_location("схід", str_franka)
    str_hryshevskoho.link_location("захід", av_shevchenka)
    av_shevchenka.link_location("схід", str_hryshevskoho)
    av_shevchenka.link_location("захід", str_valova)
    str_valova.link_location("схід", av_shevchenka)
    str_valova.link_location("північ", str_franka)
    str_valova.link_location("захід", str_halytska)
    str_halytska.link_location("схід", str_valova)
    str_halytska.link_location("захід", sq_rynok)
    sq_rynok.link_location("схід", str_halytska)
    sq_rynok.link_location("північ", g_friend)
    g_friend.link_location("південь", sq_rynok)

    # items
    ucu.item = Item('Біблія', "Обов'язковий атрибут кожного студента УКУ.")
    str_franka.item = Item("Квиток на трамвай", "Одноразовий студентський квиток на трамвай.")
    av_shevchenka.item = Good(
        "McFlurry у McDonald's",
        "Смачне морозиво у теплий весняний день.",
        60
    )
    str_valova.item = Good(
        "Кокосовий батончик у Рошені",
        "новий батончик у Рошені. Чого його всі так хвалять?",
        20
    )

    # characters
    str_stryjska.character = Enemy("Військкомат", "")
    sq_rynok.character = Friend("Петро Радковець", "Привіт друже! Вітаю у нашому старому місті!")

    # crete game and start
    game = Game(ucu, g_friend)
    game.main_loop()
