# Set subscription
az account set --subscription "Azure for Students"

# Setiing SQL server
az deployment group create --resource-group kgomdsuserg --template-file template/template.json --parameters template/parameters.json 
