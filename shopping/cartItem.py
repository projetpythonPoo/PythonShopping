from shopping import article


class CartItem:

    # region private attributes
    _article = None
    _quantity = 0

    # endregion private attributes

    def __init__(self, quantity, article):
        _article = article
        _quantity = quantity

    @property
    def article(self):
        return NotImplementedError

    @property
    def quantity(self):
        return NotImplementedError

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    class CartItemException(Exception):
        pass

    class WrongQuantityException(CartItemException):
        pass
