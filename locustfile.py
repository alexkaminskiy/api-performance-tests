from locust import HttpUser, between # type: ignore
from tasks.auth_tasks import AuthTasks
from tasks.mixed_load import MixedLoadTasks
from tasks.component_tasks import ComponentTasks
from tasks.product_tasks import ProductTasks

class ApiUser(HttpUser):
    wait_time = between(1, 3)
    
    tasks = {
            MixedLoadTasks: 50,      
            ProductTasks: 25,         
            ComponentTasks: 20,      
            AuthTasks: 5              
        }
