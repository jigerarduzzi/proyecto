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
from csv import writer

def deleteEndContent(line):
    a_string = line
    split_string = a_string.split("TABLA DE ANTECEDENTES", 1)

    substring = split_string[0]
    return substring

def tokenization(text):
    doc=nlp(text) #create spacy object of npl tipe
    tokens = [t.orth_ for t in doc]
    return tokens

def tokenizationAndLemmatization(text):
    doc=nlp(text) #create spacy object of npl tipe
    return [tok.lemma_.lower() for tok in doc if tok.pos_ != 'PRON'] #crea lista de palabras del texto y aplica lemas

def deleteStopwords(text, stopwords):
    return ' '.join([word for word in text.split(' ') if word not in stopwords])

def stemming(tokenLine): #convertir palabras a raices
    stems = [spanishstemmer.stem(token) for token in tokenLine]
    return stems

def cleanText(line):
    #agregar espacios donde hay saltos de lineas
    #print(line)
    #eliminar tabla de antecedentes
    cleanedText=deleteEndContent(line)
    cleanedText=re.sub(r"(\n)"," ",cleanedText)
    #eliminar numeros romanos
    cleanedText=re.sub(r"(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$","",cleanedText)
    #eliminar saltos, caracteres especioales y espacios innecesarios
    cleanedText=re.sub("\s\s+", ' ',cleanedText)
    cleanedText=unidecode(cleanedText)
    #eliminar articulo x y nro) del inicio de cada linea
    cleanedText=re.sub(r"(microsoft word)|(ley_[0-9]+)|(e-[0-9]+)|(articulo [0-9]º)|(art. [0-9]*)|(articulo [0-9]*)|(ley [0-9]*)|(texto definitivo)|(ley e[0-9]*)|(antes dnu [0-9])|(antes ley [0-9]*)|(sancion: \d{2}/\d{2}/\d{4})|(publicacion: b.o. \d{2}/\d{2}/\d{4})|(actualizacion: \d{2}/\d{2}/\d{4})|(promulgacion: \d{2}/\d{2}/\d{4})|(rama: [a-z]*)|(^[a-z]*\))","",cleanedText.lower())
    #eliminar numeros 
    cleanedText=re.sub(r"[0-9]","",cleanedText)
    #eliminar puntos y comas
    cleanedText=re.sub(r'[^\w\s]','',cleanedText)
    #eliminar stopwords
    cleanedText=deleteStopwords(cleanedText, stopwords.words('spanish'))  
    #eliminar saltos, caracteres especioales y espacios innecesarios
    cleanedText=re.sub("\s\s+", ' ',cleanedText)
    return cleanedText

def flattenArray(originalArray):
    flatArray=[]
    for a in originalArray:
        for item in a:
            if(item!=" "):
                flatArray.append(item)
    
    return flatArray

#with open('lawExampleToClean.txt',"r", encoding="utf8") as f:
#    contents = f.readlines()

#cleanedLaw=[]
#for i in range(len(contents)):
#    if(contents[i]!="\n"):
#        cleanedLaw.append(stemming(cleanText(contents[i])))

def cleanDataset(rama):
    with open('./datasets/'+rama+'.json', encoding="utf8") as f:
        data = json.load(f)
    for ley in range(len(data)):

        #print(tokenizationAndLemmatization(cleanText(data[ley]["contenido"])))
        #or
        newCSVRow=stemming(tokenization(cleanText(data[ley]["contenido"])))
        # First, open the old CSV file in append mode, hence mentioned as 'a'
        # Then, for the CSV file, create a file object
        with open('./datasets/Dataset.csv', 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow([rama,newCSVRow])  
            # Close the file object
            f_object.close()

        #cleanText(data[ley]["contenido"])

    




 



