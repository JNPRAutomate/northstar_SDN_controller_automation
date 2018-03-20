#  This python script makes rest call to Northstar to create a new LSP. The LSP is hardcoded in the script
#  usage: python provision_new_LSP.py
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
import yaml

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
url_base = 'http://' + my_variables_in_yaml['northstar']['ip'] + ':8091/NorthStar/API/v2/tenant/'

url = url_base + '1/topology/1/te-lsps'
headers = { 'content-type' : 'application/json'}

payload='''{
    "name": "newlspfrompython",
    "from": {
        "topoObjectType": "ipv4",
        "address": "11.0.0.102"
    },
    "to": {
        "topoObjectType": "ipv4",
        "address": "11.0.0.103"
    },
    "plannedProperties": {
        "bandwidth": "1M",
        "setupPriority": 7,
        "holdingPriority": 7
    }
}'''

#payload='''{
#    "name": "newlspfrompython",
#    "from": {
#        "topoObjectType": "ipv4",
#        "address": "10.139.10.139"
#    },
#    "to": {
#        "topoObjectType": "ipv4",
#        "address": "10.210.10.112"
#    },
#    "plannedProperties": {
#        "bandwidth": "1M",
#        "setupPriority": 7,
#        "holdingPriority": 7
#    }
#}'''

# q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload)
get_token()
headers = {'Authorization':get_token(), 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
q = requests.post(url, data=payload, headers=headers, verify=False)
print 'created LSP: ' + q.json()['name']
