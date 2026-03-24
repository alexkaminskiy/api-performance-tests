from clients.base_client import BaseClient

class ProductClient(BaseClient):

    def get_product_by_id(self, product_id: int):
        return self.get(f"/Product/GetProductById/{product_id}")

    def get_product_by_name(self, name: str):
        return self.get(f"/Product/GetProductByName/{name}")

    def get_all_products(self):
        return self.get("/Product/GetProducts")

    def create_product(self, product_body: dict):
        return self.post("/Product/Create", json=product_body)