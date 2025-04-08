from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
import configparser

def main():

    config = configparser.ConfigParser()
    config.read('settings.ini')

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

    customers = Customer.all(qb=client)

    for customer in customers:
        print(customer.DisplayName)

if __name__ == '__main__':
    main()