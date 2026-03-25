
import os
from dotenv import load_dotenv


load_dotenv()

BASE_URL = str(os.getenv("BASE_URL"))
AUTH_USER_NAME = os.getenv("AUTH_USER_NAME")      
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

DEFAULT_PRODUCT_ID = 1
DEFAULT_COMPONENT_ID = 1