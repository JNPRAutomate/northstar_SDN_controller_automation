#  This python script makes rest calls to Juniper Northstar to create new LSPs. These new LSPs are defined in the file variables.yaml
#  usage: python provision_new_LSPs.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_token():
 url = 'https://' + my_variables_in_yaml['northstar']['ip'] + ':8443/oauth2/token'
 data_to_get_token = {"grant_type":"password","username":authuser,"password":authpwd}
 r = requests.post(url, data=json.dumps(data_to_get_token), auth=(authuser, authpwd), headers=headers, verify=False)
 return str('Bearer ' + r.json()['access_token'])

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
payload = my_variables_in_yaml['lsp_to_add']

url = url_base + '1/topology/1/te-lsps'
headers = { 'content-type' : 'application/json'}
headers = {'Authorization':get_token(), 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

for item in payload:
    # q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=json.dumps(item, indent=4))
    q = requests.post(url, headers=headers, verify=False, data=json.dumps(item, indent=4))
    print 'created LSP: ' + q.json()['name']


