
class Article:
    def __init__(self, id_, description, price):
        self._id = id_
        self._description = description
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def price(self):
        return self._price
