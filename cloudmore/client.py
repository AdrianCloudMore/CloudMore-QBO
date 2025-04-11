import json

from cloudmore_sdk import ServiceCategoriesApi, ServiceCategoryViewModel

from cloudmore.auth_config import AuthConfig
import cloudmore_sdk
import requests
import datetime
from datetime import timedelta
from typing import List

class CloudmoreClient():

    client: cloudmore_sdk.ApiClient
    authConfig: AuthConfig
    host: str = "https://api-dev.cloudmore.com"
    config: object

    def __init__(self,**kwargs):
        self.authConfig = kwargs.get("authConfig")
        self.host = kwargs.get("host")
        self.config = cloudmore_sdk.Configuration()
        self.config.host = self.host
        self.client = cloudmore_sdk.ApiClient(configuration=self.config)

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
            self.client.configuration.token_expiry = datetime.datetime.now() + timedelta(seconds=data["expires_in"])
        else:
            print(response)
            raise Exception("Failed to authenticate with CloudMore API")

    def GetSellerServiceByServiceId(self,sellerId,serviceId):
        api_instance = cloudmore_sdk.SellerServicesApi(api_client=self.client)
        data = api_instance.api_sellers_by_seller_id_services_by_id_get(sellerId,serviceId)
        return data

    def GetSellerServiceByServiceId(self,sellerId,serviceId):
        api_instance = cloudmore_sdk.SellerServicesApi(api_client=self.client)
        data = api_instance.api_sellers_by_seller_id_services_by_id_get(sellerId,serviceId)
        return data

    def GetAllSellerServices(self,sellerId) -> {}:
        api_instance = cloudmore_sdk.SellerServicesApi(api_client=self.client)
        data = api_instance.api_sellers_by_seller_id_services_get(sellerId)
        print(data)
        return data

    def GetAllSellerServiceProducts(self,sellerId, serviceId):
        api_instance = cloudmore_sdk.SellerServiceProductsApi(api_client=self.client)
        data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_get(sellerId, serviceId)
        print(data)
        return data

    def GetBrokerById(self,sellerId, brokerId):
        api_instance = cloudmore_sdk.ResellersApi(api_client=self.client)
        data = api_instance.api_sellers_by_seller_id_resellers_by_id_get(sellerId, brokerId)
        print(data)
        return data

    def GetServiceCategories(self):
        api_instance = cloudmore_sdk.ServiceCategoriesApi(api_client=self.client)
        data = api_instance.api_services_categories_get()
        return data
