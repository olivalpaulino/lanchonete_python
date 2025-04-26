import json
from urllib.parse import parse_qs

from service import ProductService

product_service = ProductService()

def handle_request(path, method, body):
    if path == "/products" and method == "GET":
        return 200, product_service.list_products()
    
    if path == "/products" and method == "POST":
        data = json.loads(body)
        name = data.get("name")
        price = data.get("price")
        if name and price:
            return 201, product_service.add_product(name, price)
        else:
            return 400, {"error": "Missing name or price"}
    
    if path.startswith("/products/") and method == "GET":
        try:
            id = int(path.split("/")[-1])
            product = product_service.get_product_by_id(id)
            if product:
                return 200, product
            else:
                return 404, {"error": "Product not found"}
        except ValueError:
            return 400, {"error": "Invalid ID format"}
    
    return 404, {"error": "Endpoint not found"}
