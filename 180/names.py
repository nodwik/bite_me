from collections import defaultdict
import pandas as pd

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


#def group_names_by_country(data: str = data) -> defaultdict:
#    countries = defaultdict(list)
#    lines = data.split('\n')[1:]
#    for line in lines:
#        last_name, first_name, ID = line.split(',')
#        if ID in countries.keys():
#            current = countries[ID]
#            new = countries[ID] + [first_name + ' ' + last_name]
#            countries[ID] = new
#        else:
#            countries[ID] = [first_name + ' ' + last_name]
#    return countries

def group_names_by_country(data: str) -> defaultdict:
    countries = defaultdict(list)
    lines = data.strip().split('\n')[1:]  # Skip the header line and remove any leading/trailing whitespace
    for line in lines:
        last_name, first_name, ID = line.split(',')
        countries[ID].append(f"{first_name} {last_name}")
    return countries


group_names_by_country(data)