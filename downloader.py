import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

class Downloader:
   
   def downloadFiles(dates):
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
      #parameter to keep open selenium when it is started in a function
      chrome_options.add_experimental_option("detach", True)
      driver = webdriver.Chrome(chrome_options=chrome_options)

      #Search URL
      driver.get(URL)
      for x in dates:
         str_aux=datetime.strptime(str(x), '%d/%m/%Y').strftime('%Y%m%d')
         driver.execute_script("descargarPDFSeccion('primera','"+str_aux+"', '/pdf/download_section')")

      return driver
