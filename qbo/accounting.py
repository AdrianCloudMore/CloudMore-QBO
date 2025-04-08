from quickbooks import QuickBooks
from quickbooks.objects.bill import Bill
from quickbooks.objects.bill import ItemBasedExpenseLine
from quickbooks.objects.bill import AccountBasedExpenseLine
from quickbooks.objects.bill import DetailLine
from quickbooks.objects.customer import Customer

from quickbooks.objects.vendor import Vendor

class qbo:

    client: QuickBooks

    def __init__(self, **kwargs):
        self.client = kwargs.get("client")

    def getVendor(self, name):
        vendors = Vendor.filter(DisplayName=name,qb=self.client)
        for v in vendors:
            print(v.DisplayName)
        return vendors.__getitem__(0)

    def getAllVendors(self):
        vendors = Vendor.all(qb=self.client)
        for v in vendors:
            print(v.DisplayName)
        return vendors

    def getAllCustomers(self):
        customers = Customer.all(qb=self.client)
        for customer in customers:
            print(customer.DisplayName)
        return customers

    def createBill(self, vendor, data):

        bill = Bill()
       # "TxnDate": "2014-11-06",
       # "TotalAmt": 103.55,

        bill.VendorRef = vendor
        bill.TxnDate = data["billingDate"]
        bill.TotalAmt = data["price"]
        bill.DueDate = data["dueDate"]

        # Save New Bill
        bill.save(qb=self.client)

