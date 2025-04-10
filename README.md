# CloudMore-QBO
CloudMore &lt;-> QuickBooks Integration 


## Dependencies

    * python-quickbooks
    * intuit-oauth

## Installation 


## Configuration

### Authentication 


## QBO Objects To Map 

```python
{
  "Bill": {
    "SyncToken": "2", 
    "domain": "QBO", 
    "APAccountRef": {
      "name": "Accounts Payable (A/P)", 
      "value": "33"
    }, 
    "VendorRef": {
      "name": "Norton Lumber and Building Materials", 
      "value": "46"
    }, 
    "TxnDate": "2014-11-06", 
    "TotalAmt": 103.55, 
    "CurrencyRef": {
      "name": "United States Dollar", 
      "value": "USD"
    }, 
    "LinkedTxn": [
      {
        "TxnId": "118", 
        "TxnType": "BillPaymentCheck"
      }
    ], 
    "SalesTermRef": {
      "value": "3"
    }, 
    "DueDate": "2014-12-06", 
    "sparse": false, 
    "Line": [
      {
        "Description": "Lumber", 
        "DetailType": "AccountBasedExpenseLineDetail", 
        "ProjectRef": {
          "value": "39298034"
        }, 
        "Amount": 103.55, 
        "Id": "1", 
        "AccountBasedExpenseLineDetail": {
          "TaxCodeRef": {
            "value": "TAX"
          }, 
          "AccountRef": {
            "name": "Job Expenses:Job Materials:Decks and Patios", 
            "value": "64"
          }, 
          "BillableStatus": "Billable", 
          "CustomerRef": {
            "name": "Travis Waldron", 
            "value": "26"
          }
        }
      }
    ], 
    "Balance": 0, 
    "Id": "25", 
    "MetaData": {
      "CreateTime": "2014-11-06T15:37:25-08:00", 
      "LastUpdatedTime": "2015-02-09T10:11:11-08:00"
    }
  }, 
  "time": "2015-02-09T10:17:20.251-08:00"
}
```
