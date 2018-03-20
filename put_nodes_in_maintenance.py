from datetime import timedelta, datetime
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml
import json

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

def get_node_index(qqqq):
 url = url_base + '1/topology/1/nodes'
 r = requests.get(url, headers=headers, verify=False)
 for i in r.json():
  if i['hostName'] == qqqq:
   node_index = i['nodeIndex']
 return node_index

def put_nodes_in_maintenance():
 elements_to_put_in_maintenance = []
 for item in nodes:
  elements_to_put_in_maintenance.append({"topoObjectType": "node", "index": get_node_index(item)})
 maintenance_data = {
     "topoObjectType": "maintenance",
     "topologyIndex": 1,
     "user": "admin",
     "name": "whatever",
     "startTime": starttime.isoformat(),
     "endTime": endtime.isoformat(),
     "elements": elements_to_put_in_maintenance
     }
 return(maintenance_data)

my_variables_in_yaml=import_variables_from_file()
authuser = my_variables_in_yaml['northstar']['username']
authpwd = my_variables_in_yaml['northstar']['password']
nodes = my_variables_in_yaml['nodes_to_put_into_maintenance']

headers = { 'content-type' : 'application/json'}

headers = {'Authorization':get_token(), 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

url_base = 'http://' + my_variables_in_yaml['northstar']['ip'] + ':8091/NorthStar/API/v2/tenant/'
maintenance_url = url_base + '1/topology/1/maintenances'

starttime = datetime.now()
endtime = datetime.now() + timedelta(minutes=15)

json.dumps(put_nodes_in_maintenance())
m_res = requests.post(maintenance_url, data=json.dumps(put_nodes_in_maintenance()), headers=headers, verify=False)
#m_res
#print m_res.json()

