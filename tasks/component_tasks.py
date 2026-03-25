from locust import TaskSet, task
from clients.component_client import ComponentClient
from config.settings import DEFAULT_PRODUCT_ID

class ComponentTasks(TaskSet):

    def on_start(self):
        self.client_api = ComponentClient(self.client)

    @task(80)
    def get_components_by_product(self):
        self.client_api.get_by_product(DEFAULT_PRODUCT_ID)

    @task(20)
    def get_all_components(self):
        self.client_api.get_all_components()