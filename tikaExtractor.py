#py -m pip install tika  
from tika import parser   
  
parsed_pdf = parser.from_file("seccion_primera_20211231.pdf") 
  
data = parsed_pdf['content']  
  
print(data) 
  
print(type(data))