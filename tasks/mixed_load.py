from locust import TaskSet, task
from clients.auth_client import AuthClient
from clients.product_client import ProductClient
from clients.component_client import ComponentClient
from config.settings import DEFAULT_PRODUCT_ID

class MixedLoadTasks(TaskSet):

    def on_start(self):
        auth = AuthClient()
        token = auth.login()

        self.products = ProductClient(token=token)
        self.components = ComponentClient(token=token)

    @task(3)
    def fetch_products(self):
        self.products.get_all_products()

    @task(2)
    def fetch_components(self):
        self.components.get_by_product(DEFAULT_PRODUCT_ID)

    @task(1)
    def health_auth(self):
        self.products.get("/api/Authenticate/Get")