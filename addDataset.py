import json

THE_FILE = 'dataExample.json'

ley = {"ley":"ley nueva",
    "clasificacion":"ramaLey",
    "contenido":"contenido nueva ley "}


with open('dataExample.json', 'r+') as file:
    data = json.load(file)

data.append(ley)

with open('dataExample.json', "w") as file:
    json.dump(data,file)