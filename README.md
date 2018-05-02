## About this repo

This repository has automation content for Northstar SDN controller.  
This repository requires Northstar version 4 or above. This repository doesn’t cover how to install Northstar.  

## install the requirements to use the automation content hosted in this repository  
The python scripts hosted in this repository use the library **requests** to make REST calls to Northstar.   
Run these commands on your laptop:
```
sudo -s
pip install requests
```

## clone this repository
Run these commands on your laptop:
```
sudo -s
git clone https://github.com/JNPRAutomate/northstar_SDN_controller_automation.git
```

## Use this repository

Move to your local copy of this remote repository
```
cd northstar_SDN_controller_automation
```

The file [**variables.yml**](variables.yml) has your Northstar setup details: 
- SDN controller ip address, username and password. 
- LSPs to add/remove.  
- Nodes to put into maintenance mode

usage:   
```
vi variables.yml
```

The script [**provision_new_LSP.py**](provision_new_LSP.py) makes REST calls to Northstar to create a new LSP. The LSP is hardcoded in the script.    
usage:   
```
python provision_new_LSP.py 
created LSP: newlspfrompython
```

The script [**provision_new_LSPs.py**](provision_new_LSPs.py) makes REST calls to Northstar to create new LSPs. They are defined in [**variables.yml**](variables.yml) file.    
usage:   
```
python provision_new_LSPs.py 
created LSP: lSP1frompython
created LSP: lSP2frompython
```

The script [**python get_active_LSPs.py**](get_active_LSPs.py) makes a REST call to Northstar to get all actives LSP  
usage: 
```
python get_active_LSPs.py
```
  
The script [**get_all_LSPs.py**](get_all_LSPs.py) makes REST calls to Northstar to get all LSP  
usage:   
```
python get_all_LSPs.py
```

The script [**delete_LSPs.py**](delete_LSPs.py) makes REST calls to Northstar to delete the LSPs defined in [**variables.yml**](variables.yml) file.  
Usage: 
```
python delete_LSPs.py
deleted LSP: lSP1frompython
deleted LSP: lSP2frompython
deleted LSP: newlspfrompython
```

The script [**put_nodes_in_maintenance.py**](put_nodes_in_maintenance.py) makes REST calls to Northstar to put the nodes defined in [**variables.yml**](variables.yml) file into maintenance mode.  
During a maintenance event, the selected elements are considered logically down, and the system reroutes the LSPs around those elements during the maintenance period. After the maintenance event is completed, delegated and PCE-initiated LSPs are reverted back to optimal paths.  

Usage:
```
python put_nodes_in_maintenance.py
```

The script [**list_maintenance.py**](list_maintenance.py) makes REST calls to Northstar to get the maintenance details from Northstar and print these details   
Usage:
```
python list_maintenance.py
[{u'elements': [{u'id': u'0110.0000.0101',
                 u'index': 1,
                 u'topoObjectType': u'node'},
                {u'id': u'0110.0000.0102',
                 u'index': 2,
                 u'topoObjectType': u'node'}],
  u'endTime': u'2018-03-21T01:48:09Z',
  u'maintenanceIndex': 3,
  u'name': u'event1',
  u'startTime': u'2018-03-21T01:33:09Z',
  u'status': u'planned',
  u'topoObjectType': u'maintenance',
  u'topologyIndex': 1,
  u'user': u'admin'},
 {u'elements': [{u'id': u'0110.0000.0103',
                 u'index': 3,
                 u'topoObjectType': u'node'},
                {u'id': u'0110.0000.0104',
                 u'index': 4,
                 u'topoObjectType': u'node'}],
  u'endTime': u'2018-03-21T03:33:18Z',
  u'maintenanceIndex': 4,
  u'name': u'event2',
  u'startTime': u'2018-03-21T01:33:18Z',
  u'status': u'planned',
  u'topoObjectType': u'maintenance',
  u'topologyIndex': 1,
  u'user': u'admin'}]
```
