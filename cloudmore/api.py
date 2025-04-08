from cloudmore.auth_config import AuthConfig
import swagger_client
import requests
import datetime
from datetime import timedelta

class CloudmoreClient:

    client: swagger_client.ApiClient
    authConfig: AuthConfig
    host: str = "https://api-dev.cloudmore.com"
    config: swagger_client.Configuration()

    def __init__(self,**kwargs):
        self.authConfig = kwargs.get("authConfig")
        self.host = kwargs.get("host")
        self.config.host = self.host
        self.client = swagger_client.ApiClient(configuration=self.config)

    def authenticate(self):
        """Retrieve and store access token for Cloudmore API"""
        url = f"{self.client.configuration.host}/connect/token"
        payload = {
            "client_id": self.authConfig.client_id,
            "client_secret": self.authConfig.client_secret,
            "grant_type": self.authConfig.grant_type,
            "scope": self.authConfig.scope,
            "username": self.authConfig.username,
            "password": self.authConfig.password
        }

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, payload, headers)
        if response.status_code == 200:
            data = response.json()
            self.client.configuration.access_token = data["access_token"]
            self.client.set_default_header("Authorization", "%s %s" % ("Bearer", data["access_token"]))
            self.client.configuration.token_expiry = datetime.now() + timedelta(seconds=data["expires_in"])
        else:
            print(response)
            raise Exception("Failed to authenticate with CloudMore API")
