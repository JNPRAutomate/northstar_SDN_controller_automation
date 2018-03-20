# This python script makes REST calls to Northstar to delete the LSPs defined in the file variables.yml
# usage: python delete_LSPs.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def import_variables_from_file():
 my_variables_file=open('variables.yml', 'r')
 my_variables_in_string=my_variables_file.read()
 my_variables_in_yaml=yaml.load(my_variables_in_string)
 my_variables_file.close()
 return my_variables_in_yaml

def get_token():
 url = 'https://' + my_variables_in_yaml['northstar']['ip'] + ':8443/oauth2/token'
 data_to_get_token = {"grant_type":"password","username":authuser,"password":authpwd}
 r = requests.post(url, data=json.dumps(data_to_get_token), auth=(authuser, authpwd), headers=headers, verify=False)
 return str('Bearer ' + r.json()['access_token'])

my_variables_in_yaml=import_variables_from_file()
authuser = my_variables_in_yaml['northstar']['username']
authpwd = my_variables_in_yaml['northstar']['password']
LSPs_to_delete = my_variables_in_yaml['lsp_to_delete']
url_base = 'http://' + my_variables_in_yaml['northstar']['ip'] + ':8091/NorthStar/API/v2/tenant/'

url = url_base + '1/topology/1/te-lsps'
headers = { 'Accept': 'application/json' }
headers = { 'Content-type': 'application/json' }



# r = requests.get(url, headers=headers, auth=(authuser, authpwd))
get_token()
headers = {'Authorization':get_token(), 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.get(url, headers=headers, verify=False)

for LSP_to_delete in LSPs_to_delete:
    for LSP in r.json():
        if LSP['name'] == LSP_to_delete: 
            url_to_delete = url + '/' + str(LSP['lspIndex'])
            #requests.delete(url_to_delete, headers=headers, auth=(authuser, authpwd))
            requests.delete(url_to_delete, headers=headers, verify=False)
            print "deleted LSP: " + LSP['name']


