import unittest
from module001 import ShoppingList
#from 文件名 import 类名，纯数字的话不行


class TestShoppingList(unittest.TestCase):
#            类         #继承自unittest.TestCase类的下面
    def setUp(self):
        self.shopping_list = ShoppingList({"衣服": 2, "裤子": 3})

    def test_get_item_count(self):
#       这个一定要有test，才能被unittest自动当成测试用例
        self.assertEqual(self.shopping_list.get_item_count(),2)
#          调用module001里shopping_list类里的get_item_count功能
#            assertEqual的作用是检查返回值是否为2（assert）

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(),5)



















