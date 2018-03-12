#  This python script makes rest call to Juniper Northstar to create a new LSP
#  usage: python norsthstar_provision_new_lsp.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

url='http://a.b.c.d:8091/NorthStar/API/v2/tenant/1/topology/1/te-lsps'
authuser ='xxxx' 
authpwd ='yyyy'
headers = { 'content-type' : 'application/json'}
payload1='''{
    "name": "newlspfrompython",
    "from": {
        "topoObjectType": "ipv4",
        "address": "11.0.0.101"
    },
    "to": {
        "topoObjectType": "ipv4",
        "address": "11.0.0.107"
    },
    "plannedProperties": {
        "bandwidth": "1M",
        "setupPriority": 7,
        "holdingPriority": 7
    }
}'''

q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload1)
