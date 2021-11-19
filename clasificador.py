import requests

URL = "https://www.boletinoficial.gob.ar/seccion/primera"
page = requests.get(URL)

print(page.text)


