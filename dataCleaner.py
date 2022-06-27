#library to replace aáäAÁÄeéëEÉËiíïIÍÏoóöOÓÖuúüUÚÜñÑ
from turtle import clear
from unidecode import unidecode
import re
from nltk.corpus import stopwords
from nltk import SnowballStemmer
import json
#pip3 install spacy==2.2.4
import spacy
#py -m pip install install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
# or:  py -m spacy download es_core_news_sm 
nlp = spacy.load("es_core_news_sm")
spanishstemmer=SnowballStemmer('spanish')

def tokenization(text):
    doc=nlp(text) #create spacy object of npl tipe
    return [tok.lemma_.lower() for tok in doc if tok.pos_ != 'PRON'] #crea lista de palabras del texto y aplica lemas

def deleteStopwords(text, stopwords):
    return ' '.join([word for word in text.split(' ') if word not in stopwords])

def stemming(tokenLine): #convertir palabras a raices
    stems = [spanishstemmer.stem(token) for token in tokenLine]
    return stems

def cleanText(line):
    #agregar espacios donde hay saltos de lineas
    cleanedText=re.sub(r"(\n)"," ",line)
    #eliminar saltos, caracteres especioales y espacios innecesarios
    cleanedText=re.sub("\s\s+", ' ',cleanedText)
    cleanedText=unidecode(cleanedText)
    #eliminar articulo x y nro) del inicio de cada linea
    #print(cleanedText)
    cleanedText=re.sub(r"(articulo [0-9]*)|(ley [0-9]*)|(^texto definitivo)|(ley e[0-9])|(antes dnu [0-9])|(antes ley [0-9])|(sancion: \d{2}/\d{2}/\d{4})|(publicacion: b.o. \d{2}/\d{2}/\d{4})|(actualizacion: \d{2}/\d{2}/\d{4})|(promulgacion: \d{2}/\d{2}/\d{4})|(rama: [a-z])|(^[a-z]*\))","",cleanedText.lower())
    #eliminar puntos y comas
    cleanedText=re.sub(r'[^\w\s]','',cleanedText)
    #eliminar stopwords
    cleanedText=deleteStopwords(cleanedText, stopwords.words('spanish'))  
    #convertir linea a tokens de palabras
    return tokenization(cleanedText)

def flattenArray(originalArray):
    flatArray=[]
    for a in originalArray:
        for item in a:
            if(item!=" "):
                flatArray.append(item)
    
    return flatArray

with open('lawExampleToClean.txt',"r", encoding="utf8") as f:
    contents = f.readlines()

cleanedLaw=[]
for i in range(len(contents)):
    if(contents[i]!="\n"):
        cleanedLaw.append(stemming(cleanText(contents[i])))

def cleanDataset(rama):
    with open('./datasets/'+rama+'.json', encoding="utf8") as f:
        data = json.load(f)
    for ley in range(len(data)):
        print(stemming(cleanText(data[ley]["contenido"])))
        #cleanText(data[ley]["contenido"])

    




 



