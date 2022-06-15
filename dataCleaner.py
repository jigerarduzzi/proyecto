#library to replace aáäAÁÄeéëEÉËiíïIÍÏoóöOÓÖuúüUÚÜñÑ
from turtle import clear
from unidecode import unidecode
import re
from nltk.corpus import stopwords
from nltk import SnowballStemmer
#pip3 install spacy==2.2.4
import spacy
#py -m pip install install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz
# or:  py -m spacy download es_core_news_sm 
nlp = spacy.load("es_core_news_sm")
spanishstemmer=SnowballStemmer('spanish')

import json
with open('civilDatasetTraining.json', encoding="utf8") as f:
  data = json.load(f)




def tokenization(text):
    doc=nlp(text) #create spacy object of npl tipe
    return [tok.lemma_.lower() for tok in doc if tok.pos_ != 'PRON'] #crea lista de palabras del texto y aplica lemas


def deleteStopwords(text, stopwords):
    return ' '.join([word for word in text.split(' ') if word not in stopwords])

def stemming(tokenLine): #convertir palabras a raices
    stems = [spanishstemmer.stem(token) for token in tokenLine]
    return stems

def cleanText(line):
    #eliminar saltos, caracteres especioales y espacios innecesarios
    cleanedText=unidecode(line.lower().replace("  ", " ").rstrip ( '\n'))
    #eliminar articulo x y nro) del inicio de cada linea
    cleanedText=re.sub(r"(^articulo [0-9]*.-)|(^[a-z]*\))","",cleanedText)
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

#print(doc)


cleanedLaw=[]
for i in range(len(contents)):
    #print(unidecode(contents[i]).lower().replace("  ", " ").rstrip ( '\n'))#elimina caracteres especiales, mayusculas, espacios y saltos de linea repetidos
    #print(re.sub(r"(^artículo [0-9]*.-)|(^[a-z]*\))","",contents[i].lower()))
    #elimina caracteres especiales, mayusculas, espacios y saltos de linea repetidos
    #expresion regular elimina lo que empieza con esos patrones (ejemplo, ARTÍCULO 26.- y a))
   # print(re.sub(r"(^articulo [0-9]*.-)|(^[a-z]*\))","",unidecode(contents[i]).lower().replace("  ", " ").rstrip ( '\n')))
    
    
    #lineWithoutStopWords=delete_stopwords(contents[i].lower(), stopwords.words('spanish'))
    #print(re.sub(r"(^articulo [0-9]*.-)|(^[a-z]*\))","",unidecode(lineWithoutStopWords.replace("  ", " ").rstrip ( '\n'))))

    ##print(stemming(tokenization(contents[i])))

    if(contents[i]!="\n"):
        cleanedLaw.append(stemming(cleanText(contents[i])))

#print(flattenArray(cleanedLaw))
#print(stemming(cleanText(data[0]["contenido"])))

for ley in range(len(data)):
    print(stemming(cleanText(data[ley]["contenido"])))
    




 



