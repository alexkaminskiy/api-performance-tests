from locust import TaskSet, task
from clients.product_client import ProductClient
from config.settings import DEFAULT_PRODUCT_ID

class ProductTasks(TaskSet):

    def on_start(self):
        self.client_api = ProductClient()

    @task
    def get_product_by_id(self):
        self.client_api.get_product_by_id(DEFAULT_PRODUCT_ID)

    @task
    def get_all_products(self):
        self.client_api.get_all_products()