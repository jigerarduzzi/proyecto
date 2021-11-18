import os
import requests



urls = [
    'http://s3.arsat.com.ar/cdn-bo-001/pdf-del-dia/primera.pdf',
]

output_dir = '.\output'

for url in urls:
    response = requests.get(url)
    if response.status_code==200:
        file_path = os.path.join(output_dir,os.path.basename(url))
        with open (file_path,'wb') as f:
            f.write(response.content)