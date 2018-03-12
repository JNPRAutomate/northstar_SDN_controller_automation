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

The script [**norsthstar_provision_new_lsp.py**](norsthstar_provision_new_lsp.py) makes rest call to Juniper Northstar to create a new LSP  
usage:   
```
python norsthstar_provision_new_lsp.py
```
  
The script [**python northstar_get_actives_lsp.py**](northstar_get_actives_lsp.py) makes a rest call to Juniper Northstar to get all active LSP  
usage: 
```
python northstar_get_actives_lsp.py
```
  
The script [**northstar_get_all_lsp.py**](northstar_get_all_lsp.py) makes a rest call to Juniper Northstar to get all LSP  
usage:   
```
northstar_get_all_lsp.py
```




