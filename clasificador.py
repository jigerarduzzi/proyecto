import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Create downloads directory
current_directory = os.getcwd()
downloads_directory = os.path.join(current_directory, r'Boras downloaded')
if not os.path.exists(downloads_directory):
   os.makedirs(downloads_directory)

#Start Chrome Driver
chromedriver = current_directory+'chromedriver.exe'
URL = 'https://www.boletinoficial.gob.ar/seccion/primera'
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()

#Set settings to downloads
prefs = {'profile.default_content_setting_values.automatic_downloads': 1,
"download.default_directory": downloads_directory, "safebrowsing.enabled":"false"}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

#Download files
driver.get(URL)
driver.execute_script("descargarPDFSeccion('primera','20211117', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211116', '/pdf/download_section')")
driver.execute_script("descargarPDFSeccion('primera','20211118', '/pdf/download_section')")



