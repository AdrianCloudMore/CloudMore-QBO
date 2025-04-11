import array
from configparser import ConfigParser

import cloudmore_sdk
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
import configparser
import fastapi
import psycopg2
import json
from fastapi import HTTPException
from fastapi import FastAPI, Request
from cloudmore.client import CloudmoreClient as CloudmoreClient
from contextlib import asynccontextmanager
from typing import List
import cloudmore.auth_config
from exceptions.CloudMoreException import CLoudMoreException

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting ... ")

    auth_client = AuthClient(
        client_id = config["authentication.quickbooks"]["CLIENT_ID"],
        client_secret = config["authentication.quickbooks"]["CLIENT_SECRET"],
        access_token = config["authentication.quickbooks"]["ACCESS_TOKEN"],
        environment=config["authentication.quickbooks"]["ENVIRONMENT"],
        redirect_uri=config["authentication.quickbooks"]["REDIRECT_URI"]
    )

    client = QuickBooks(
        auth_client=auth_client,
        refresh_token=config["authentication.quickbooks"]["REFRESH_TOKEN"],
        company_id=config["authentication.quickbooks"]["COMPANY_ID"]
    )

    print("Loaded QuickBooks Client")



    yield


config = configparser.ConfigParser()
config.read('settings.ini')


auth_client = AuthClient
client = QuickBooks

app = FastAPI(lifespan=lifespan)

auth_config = cloudmore.auth_config.AuthConfig(username=config["authentication.cloudmore"]["USERNAME"],
                                                    password=config["authentication.cloudmore"]["PASSWORD"],
                                                   client_secret=config["authentication.cloudmore"]["CLIENT_SECRET"])

cm = CloudmoreClient(authConfig=auth_config, host="https://api-dev.cloudmore.com")


@app.get("/seller/services")
async def get_all_seller_services():
    try:
        cm.authenticate()
        data = cm.GetServiceCategories()
        d = { "data" : data.__str__()}
        return d
    except CLoudMoreException as error:
        details = json.loads(error.args[0])
        raise HTTPException(400,detail={"type": details["type"], "msg": details["details"]})




def main():

    cm.authenticate()

    data = cm.GetAllSellerServices(config["seller.cloudmore"]["SELLER_ID"])

    for d in data:
        print(d)


if __name__ == '__main__':
    main()