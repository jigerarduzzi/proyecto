import os
import shutil

from io import StringIO
#py -m pip install tika  
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pathlib import Path

class PDFTextExtractor:
  boras = []
  output_string = StringIO()
  for file in os.listdir('BorasToClasify/'):
    boras.append(Path(os.path.join('BorasToClasify/',file)).stem)

  for bora in boras:
    with open('BorasToClasify/'+bora+'.pdf', 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    with open('BorasXML/'+bora+'.xml', 'w') as fd:
      output_string.seek(0)
      shutil.copyfileobj(output_string, fd)
