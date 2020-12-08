# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='Tutorials', # provide a name for your workspace
                      subscription_id='db3257b8-45ef-4e48-95c4-67c2df22d943', # provide your subscription ID
                      resource_group='ML_Tutorial', # provide a resource group name
                      create_resource_group=True,
                      location='westeurope') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')