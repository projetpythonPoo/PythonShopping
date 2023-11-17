import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import *


class TestCartItem(unittest.TestCase):

    _cartItem = None
    _price = 0.00
    _quantity = 0

    def setUp(self):
        self._quantity = 1
        self.articles = [], ArticleGenerator.generate(1)
        self._cartItem = CartItem(self.articles[0], self._quantity)

    def test_AllProperties_AfterInstantiation_Success(self):
        # given
        # refer to Setup
        self._price = 2.00
        # when
        # Event will be triggered by constructor
        # then
        self.assertEqual(self._cartItem.article.price, self._price)
        self.assertEqual(self._cartItem.quantity, self._quantity)

    def test_SetQuantity_CorrectValue_GetNewValue(self):
        # given
        self.expected_quantity = 2
        # when
        self._cartItem.Quantity = self.expected_quantity
        # then
        self.assertEqual(self._cartItem.quantity, self.expected_quantity)

    def test_SetQuantity_WrongValue_ThrowException(self):
        # given
        self.expected_quantity = -2
        # when
        self.assertRaises(CartItem.WrongQuantityException)
        # then
        # throw exception
