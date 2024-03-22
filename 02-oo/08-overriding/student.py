class Customer:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country


class ShoppingList:
    def __init__(self, owner):
        self.__owner = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_be_sold_to(self):
        return True
class AgeRestrictedItem(Item):
    def can_be_sold_to(self):
        if Customer.age > 17:
            return True
        return False

class CountryRestrictedItem(Item):
    def can_be_sold_to(self):
        if Customer.country != "Arstotzka":
            return True
        return False