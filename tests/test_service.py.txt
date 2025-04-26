import unittest
from app.service import ProductService

class TestProductService(unittest.TestCase):
    def test_add_and_list_product(self):
        service = ProductService()
        service.add_product("Hamburguer", 25.0)
        products = service.list_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]['name'], "Hamburguer")
        self.assertEqual(products[0]['price'], 25.0)

    def test_get_product_by_id(self):
        service = ProductService()
        service.add_product("Pizza", 40.0)
        product = service.get_product_by_id(1)
        self.assertIsNotNone(product)
        self.assertEqual(product['name'], "Pizza")

if __name__ == '__main__':
    unittest.main()
