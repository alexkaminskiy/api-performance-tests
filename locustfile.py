from locust import HttpUser, between
from tasks.auth_tasks import AuthTasks
from tasks.mixed_load import MixedLoadTasks
from tasks.component_tasks import ComponentTasks

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [MixedLoadTasks, ComponentTasks, AuthTasks]