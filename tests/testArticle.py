import unittest
from shopping.article import Article


class TestArticle(unittest.TestCase):

    def setUp(self):
        # Private attributes
        self._article = None
        self._id = 0
        self._description = ""
        self._price = 0.0

    def test_all_properties_after_instantiation_success(self):
        # given
        self._id = 1
        self._description = "product description"
        self._price = 20.45
        self._article = Article(self._id,self._description,self._price)
        # then
        self.assertEqual(self._id, self._article.get_id)
        self.assertEqual(self._description, self._article.get_description)
        self.assertEqual(self._price, self._article.get_price)


if __name__ == '__main__':
    unittest.main()
