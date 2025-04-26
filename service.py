from model import Product

class ProductService:
    def __init__(self):
        self.products = []
        self.next_id = 1

    def list_products(self):
        return [product.to_dict() for product in self.products]

    def add_product(self, name, price):
        product = Product(self.next_id, name, price)
        self.products.append(product)
        self.next_id += 1
        return product.to_dict()

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product.to_dict()
        return None
