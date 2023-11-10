
class Article:
    def __init__(self, id_, description, price):
        self._id = id_
        self._description = description
        self._price = price

    @property
    def get_id(self):
        return self._id

    @property
    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    @property
    def get_price(self):
        return self._price
