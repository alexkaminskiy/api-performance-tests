from locust import HttpUser, between
from tasks.mixed_load import MixedLoadTasks

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    tasks = [MixedLoadTasks]