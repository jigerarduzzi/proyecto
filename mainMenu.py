from TFIDF import trainModel
from classifyNewLaw import clasificarLeyes
model=None

def main():
    print("[1] Entrenar Modelo")
    print("[2] Clasificar Leyes")
    print("[0] Salir")

def option1():
    print("Entrenando modelo...")
    return trainModel()
    

def option2():
    if model:
        print(clasificarLeyes(model))
    else:
        print("Debe entrenar el modelo primero")
main()
option=int(input("Ingrese su opción: "))

while option != 0:
    if option ==1:
        #entrenar modelo
        model=option1()
        pass
    elif option == 2:
        #do option 2
        print(option2())
        pass
    else: 
        print("opcion invalida")

    main()
    option=int(input("Ingrese su opción: "))

print("Gracias por utilizar el modelo")
