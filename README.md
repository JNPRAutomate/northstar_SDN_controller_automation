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

The file [**variables.yml**](variables.yml) has your Northstar setup details.  
usage:   
```
vi variables.yml
```

The script [**provision_new_lsp.py**](provision_new_lsp.py) makes rest call to Juniper Northstar to create a new LSP  
usage:   
```
python provision_new_lsp.py
```
  
The script [**python get_actives_lsp.py**](get_actives_lsp.py) makes a rest call to Juniper Northstar to get all actives LSP  
usage: 
```
python get_actives_lsp.py
```
  
The script [**get_all_lsp.py**](get_all_lsp.py) makes a rest call to Juniper Northstar to get all LSP  
usage:   
```
python get_all_lsp.py
```

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
