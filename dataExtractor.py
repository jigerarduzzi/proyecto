#py -m pip install tika  
from tika import parser   
import glob
import dataCreator
import dataCleaner

etiqueta = input('¿Qué dataset desea crear?')
files = glob.glob("./Leyes/"+etiqueta+"/*.pdf")
laws = []
newData = dataCreator
cleaner = dataCleaner

#for file in files: descomentar para crear nuevos datasets
#    parsed_pdf = parser.from_file(file) 
#    newData.addDataset(parsed_pdf['content'], etiqueta)

cleaner.cleanDataset(etiqueta)