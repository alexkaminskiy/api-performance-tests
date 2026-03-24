from clients.base_client import BaseClient

class ComponentClient(BaseClient):

    def get_by_product(self, product_id: int):
        return self.get(f"/Components/GetComponentsByProductId/{product_id}")

    def create_component(self, body: dict):
        return self.post("/Components/CreateComponent", json=body)

    def get_all_components(self):
        return self.get("/Components/GetAllComponents")