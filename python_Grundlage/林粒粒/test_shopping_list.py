# @Time: 2024/10/7 
# @Author: Qi Wang
# @File: test_shopping_list
# @Project: Python-leran-in-total
# @Quelle:

from fastapi.testclient import TestClient
import unittest
from Shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"Paper": 8, "Cap": 30, "Pants": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)