from selenium import webdriver

driver = webdriver.Chrome(r'C:/Users/Juani Gerarduzzi/Desktop/UTN/PROYECTO/code/chromedriver.exe')

URL = 'https://www.boletinoficial.gob.ar/seccion/primera'
driver.get(URL)
driver.execute_script("descargarPDFSeccion('primera','20211117', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211116', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211118', '/pdf/download_section')")



