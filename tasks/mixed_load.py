from locust import TaskSet, task
from clients.auth_client import AuthClient
from clients.product_client import ProductClient
from clients.component_client import ComponentClient
from config.settings import DEFAULT_PRODUCT_ID

class MixedLoadTasks(TaskSet):

    def on_start(self):
        auth = AuthClient(self.client)

        self.products = ProductClient(self.client)
        self.components = ComponentClient(self.client)

    @task(20)
    def fetch_products(self):
        self.products.get_all_products()

    @task(50)
    def fetch_components(self):
        self.components.get_by_product(DEFAULT_PRODUCT_ID)

    @task(30)
    def health_auth(self):
        self.products.get("/api/Authenticate/Get")