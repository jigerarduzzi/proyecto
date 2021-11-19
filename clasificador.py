import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = 'C:/Users/Juani Gerarduzzi/Desktop/UTN/PROYECTO/code/chromedriver.exe'

URL = 'https://www.boletinoficial.gob.ar/seccion/primera'
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()

prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(URL)
driver.execute_script("descargarPDFSeccion('primera','20211117', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211116', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211118', '/pdf/download_section')")



