""" Classes with items """
class Item:
    """ all items """
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def describe(self):
        """ Describe an item

        >>> item = Item("123", "456")
        >>> item.describe()
        '[123] — 456'
        """
        return f"[{self.name}] — {self.description}"


class Good(Item):
    """ Item to buy """
    def __init__(self, name: str, description: str, price: int) -> None:
        super().__init__(name, description)
        self.price = price
