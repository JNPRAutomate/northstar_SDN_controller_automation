# This python script makes a rest call to Juniper Northstar to get all LSP
# usage: python get_all_lsp.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml

def import_variables_from_file():
 my_variables_file=open('variables.yml', 'r')
 my_variables_in_string=my_variables_file.read()
 my_variables_in_yaml=yaml.load(my_variables_in_string)
 my_variables_file.close()
 return my_variables_in_yaml

my_variables_in_yaml=import_variables_from_file()

authuser = my_variables_in_yaml['northstar']['username']
authpwd = my_variables_in_yaml['northstar']['password']
url_base = 'http://' + my_variables_in_yaml['northstar']['ip'] + ':8091/NorthStar/API/v2/tenant/'

url = url_base + '1/topology/1/te-lsps'
headers = { 'Accept': 'application/json' }
headers = { 'Content-type': 'application/json' }

r = requests.get(url, headers=headers, auth=(authuser, authpwd))

# type(r.json())
# pprint(r.json())

for item in r.json():
        print "LSP name: " + item['name']

