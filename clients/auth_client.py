from clients.base_client import BaseClient

class AuthClient(BaseClient):

    def get_auth(self):
        return self.get("/api/Authenticate/Get")