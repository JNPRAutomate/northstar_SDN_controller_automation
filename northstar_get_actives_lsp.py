# this python script makes a rest call to Juniper Northstar to get all active LSP 
# usage: python northstar_get_actives_lsp.py


import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

headers = { 'Accept': 'application/json' }
headers = { 'Content-type': 'application/json' }
url='http://a.b.c.d:8091/NorthStar/API/v2/tenant/1/topology/1/te-lsps'
authuser='xxxx'
authpwd='yyyy'

r = requests.get(url, headers=headers, auth=(authuser, authpwd))

# type(r.json())
# pprint(r.json())

# This gives the names of all the LSPs that are active
for item in r.json():
    if item['operationalStatus'] == 'Active':
print "This LSP is active: " + item['name']
