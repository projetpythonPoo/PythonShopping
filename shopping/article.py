
class Article:
    def __init__(self, id_=int(0), description=str(""), price=float(0.0)):
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
