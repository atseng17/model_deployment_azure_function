import requests
import json

local_url = "http://localhost:7071/api/httpTrigger"
# azure_url = "https://titanicmodeltest.azurewebsites.net/api/httptrigger"
azure_url = "https://titanicmodeltest.azurewebsites.net/api/httpTrigger?code=jK2QTwFj3O1WRa7pK2tSM95KsjoxteFl1YoIu-0fDIGOAzFuDgJg9A=="
data = [
    {
    'pclass': '1',
    'age': 29,
    'embarked': 'C',
    'sex': 'female'
    },
    {
    'pclass': '1',
    'age': 29,
    'embarked': 'C',
    'sex': 'male'
    },
    {
    'pclass': '2',
    'age': 29,
    'embarked': 'C',
    'sex': 'female'
    },
    {
    'pclass': '2',
    'age': 29,
    'embarked': 'C',
    'sex': 'male'
    }
]

r = requests.post(local_url, json=json.dumps(data))
print(r)
print(r.text)

# r = requests.post(azure_url, json=json.dumps(data))
# print(r)
# print(r.text)