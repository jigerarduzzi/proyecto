#py -m pip install tika  
from tika import parser   
import glob
import dataCreator

etiqueta = input('¿Qué dataset desea crear?')
files = glob.glob("./Leyes/"+etiqueta+"/*.pdf")
laws = []
newData = dataCreator

for file in files:
    parsed_pdf = parser.from_file(file) 
    newData.addDataset(parsed_pdf['content'], etiqueta)
