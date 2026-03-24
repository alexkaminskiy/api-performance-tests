from clients.base_client import BaseClient
from config.settings import AUTH_USER_NAME, AUTH_PASSWORD

class AuthClient(BaseClient):

    def login(self):
        resp = self.post(
            "/api/Authenticate/Login",
            json={"userName": AUTH_USER_NAME, "password": AUTH_PASSWORD}
        )
        token = resp.json().get("token")
        self.token = token
        return token

    def get_auth(self):
        return self.get("/api/Authenticate/Get")