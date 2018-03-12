# This python script makes a rest call to Juniper Northstar to get all LSP

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'Accept': 'application/json' }
headers = { 'Content-type': 'application/json' }
url='http://a.b.c.d:8091/NorthStar/API/v2/tenant/1/topology/1/te-lsps'
authuser='xxxx'
authpwd='yyyyy'

r = requests.get(url, headers=headers, auth=(authuser, authpwd))

# type(r.json())
# pprint(r.json())

for item in r.json():
        print "LSP name: " + item['name']

