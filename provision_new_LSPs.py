#  This python script makes rest calls to Juniper Northstar to create new LSPs. These new LSPs are defined in the file variables.yaml 
#  usage: python norsthstar_provision_new_lsps.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml
import json

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
payload = json.dump(my_variables_in_yaml['northstar']['lsp_to_add'])

url = url_base + '1/topology/1/te-lsps'
headers = { 'content-type' : 'application/json'}

for item in payload: 
    q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=item)

