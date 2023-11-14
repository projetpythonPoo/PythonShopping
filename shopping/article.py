
class Article:
    def __init__(self, id_, description, price):
        self._id = id_
        self._description = description
        self._price = price

    def get_id(self):
        return self._id

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_price(self):
        return self._price

    prop = property(get_id, get_description, set_description, get_price)
