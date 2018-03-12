# This python script makes a rest call to Juniper Northstar to delete LSPs defined in the file variables.yml
# usage: python delete_LSPs.py

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

LSPs_to_delete = my_variables_in_yaml['lsp_to_delete']

r = requests.get(url, headers=headers, auth=(authuser, authpwd))
for LSP_to_delete in LSPs_to_delete:
    for LSP in r.json():
        if LSP['name'] == LSP_to_delete: 
            url_to_delete = url + '/' + str(LSP['lspIndex'])
            requests.delete(url_to_delete, headers=headers, auth=(authuser, authpwd))
            print "deleted LSP: " + LSP['name']


