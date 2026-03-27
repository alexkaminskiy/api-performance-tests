from locust import TaskSet, task 
from clients.auth_client import AuthClient

class AuthTasks(TaskSet):

    def on_start(self):
        self.client_api = AuthClient(self.client)

    @task
    def get_auth_info(self):
        self.client_api.get_auth()