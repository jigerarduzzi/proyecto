import json

from numpy import empty

def addDataset(contenido, etiqueta):

    newLaw={
        "clasificacion":etiqueta,
        "contenido":contenido
    }
        
    with open('./datasets/'+etiqueta+'.json', 'r+') as file:
        data = json.load(file)

    data.append(newLaw)

    with open('./datasets/'+etiqueta+'.json', "w") as file:
        json.dump(data,file)
