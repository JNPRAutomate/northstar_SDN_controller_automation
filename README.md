[![Build Status](https://travis-ci.org/ksator/northstar_SDN_controller_automation.svg?branch=master)](https://travis-ci.org/ksator/northstar_SDN_controller_automation)

## About this repo
how to automate Northstar SDN controller with Python

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
git clone https://github.com/ksator/northstar_SDN_controller_automation.git
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

The script [**provision_new_LSP.py**](provision_new_LSP.py) makes rest call to Northstar to create a new LSP. The LSP is hardcoded in the script.    
usage:   
```
python provision_new_LSP.py 
created LSP: newlspfrompython
```

The script [**provision_new_LSPs.py**](provision_new_LSPs.py) makes rest calls to Northstar to create new LSPs. They are defined in [**variables.yml**](variables.yml) file.    
usage:   
```
python provision_new_LSPs.py 
created LSP: lSP1frompython
created LSP: lSP2frompython
```

The script [**python get_active_LSPs.py**](get_active_LSPs.py) makes a rest call to Northstar to get all actives LSP  
usage: 
```
python get_active_LSPs.py
```
  
The script [**get_all_LSPs.py**](get_all_LSPs.py) makes rest calls to Northstar to get all LSP  
usage:   
```
python get_all_LSPs.py
```

The script [**delete_LSPs.py**](delete_LSPs.py) makes rest calls to Northstar to delete the LSPs defined in [**variables.yml**](variables.yml) file.  
Usage: 
```
python delete_LSPs.py
deleted LSP: lSP1frompython
deleted LSP: lSP2frompython
deleted LSP: newlspfrompython
```

The script [**put_nodes_in_maintenance.py**](put_nodes_in_maintenance.py) makes rest calls to Northstar to put the nodes defined in [**variables.yml**](variables.yml) file into maintenance mode.
Usage:
```
python put_nodes_in_maintenance.py


## Continuous integration with Travis CI

There is a github webhook with Travis CI
The syntax of the python scripts and ansible playbooks in this repository are tested automatically by Travis CI. 
The files [**.travis.yml**](.travis.yml) and [**requirements.txt**](requirements.txt) at the root of this repository are used for this.  

Here's the last build status  
[![Build Status](https://travis-ci.org/ksator/northstar_SDN_controller_automation.svg?branch=master)](https://travis-ci.org/ksator/northstar_SDN_controller_automation)


## Looking for more automation solutions

https://github.com/ksator?tab=repositories  
https://gitlab.com/users/ksator/projects  
https://gist.github.com/ksator/  
