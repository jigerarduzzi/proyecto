#Método para encontrar la primera iteración de la palabra leyes
def existenLeyes(list):
   i = 0
   while i < len(list):
       if (list[i].strip().lower() == "leyes"):
           return i
       i+=1
   return 0

#Método que devuelve una lista con los índices en los cuales hay una linea que comienza con numeral
def encontrarIndices(list, index):
    listaIndices = []
    #Convendría crear una variable fija para no declararla cada vez
    listaCategorias = ["asociaciones sindicales", "audiencias publicas", "avisos oficiales", "concursos oficiales", "convenciones colectivas de trabajo", 
    "decisiones administrativas", "decretos" "decretos desclasificados", "disposiciones", "disposiciones conjuntas", "disposiciones sintetizadas", 
    "fallos", "instrucciones presidenciales", "instrucciones generales", "legislacion", "remates oficiales", "resoluciones",
    "resoluciones conjuntas", "resoluciones generales", "resoluciones sintetizadas", "sentencias", "tratados y convenios internacionales"]
    #COMPLETAR CON CORTE
    while (list[index].strip().lower() not in listaCategorias):
        index+=1 
    print (index)      
    if(index  < len(list)):
        tope = list[index].strip().lower()
    index+=1
    while (list[index].strip().lower() != tope):
        if (list[index].strip().startswith("#")):
            listaIndices.append(index)
        index+=1
    return listaIndices

def crearLey(linesBora, inicio, fin, nLey):
    with open('Leyes/BoraX_Ley'+str(nLey), 'w') as l:
        while (inicio <= fin):
            l.write(linesBora[inicio])
            inicio+=1
    l.close()

#Método que se utiliza para crear los archivos con la lista y los índices
def creadorArchivosLeyes(linesBora, listaIndices):
    i, nLey = 0, 1
    print(i, nLey)
    while i < len(listaIndices):
        if (linesBora[listaIndices[i]][2:8] == linesBora[listaIndices[i+1]][2:8]):
            crearLey(linesBora, listaIndices[i], listaIndices[i+1], nLey)
            nLey+=1
        i+=2
    return

with open('Boras downloaded/file.xml', 'r') as f:
    linesBora = f.readlines()
    index = existenLeyes(linesBora)
    if (index > 0):
        #Se podría hacer un return por si se quiere hacer una comprobación de si existen leyes
        print("Existen leyes en este Bora")
        listaIndices = encontrarIndices(linesBora, (index))
        creadorArchivosLeyes(linesBora, listaIndices)
f.close()
