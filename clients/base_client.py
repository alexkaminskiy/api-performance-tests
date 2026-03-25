from config.settings import BASE_URL, AUTH_USER_NAME, AUTH_PASSWORD
from utils.logger import get_logger
import requests

logger = get_logger()

class BaseClient:

    def __init__(self, locust_client, token=None, base_url: str = BASE_URL):
        self.client = locust_client                    # <-- Locust HttpUser client
        self.base_url = base_url.rstrip("/")
        self.token = token if token else self._get_token()

    @property
    def headers(self):
        h = {"Content-Type": "application/json"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def _url(self, path: str):
        return f"{self.base_url}/{path.lstrip('/')}"

    def _get_token(self):
        auth_url = self._url('/api/Authenticate/Login')
        logger.info(f"Requesting auth token from {auth_url}")

        r = requests.post(auth_url, json={"username": AUTH_USER_NAME, "password": AUTH_PASSWORD})

        logger.debug(f"Auth response status={r.status_code}, body={r.text}")

        r.raise_for_status()
        token = r.json().get("token")

        logger.info("Token successfully retrieved")
        return token

    def get(self, path, **kwargs):
        url = self._url(path)
        logger.info(f"GET {url}")

        return self.client.get(                  
            url,
            headers=self.headers,
            **kwargs
        )

    def post(self, path, **kwargs):
        url = self._url(path)
        logger.info(f"POST {url}")

        return self.client.post(                    
            url,
            headers=self.headers,
            **kwargs
        )