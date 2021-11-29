
from appJar import gui

class Main(object):
    app = gui("Clasificador de Leyes", "600x500")

    def __init__(self):
        super(Main, self).__init__()
        self.iniciarInterfaz()
        pass

    def iniciarInterfaz(self):
        self.app.startFrameStack("MENU")
 
        self.app.startFrame("Main")
        #self.app.setBg("gray")
        self.app.setPadding([20,5])

        self.app.startFrame("TITULOMAIN")
        self.app.addLabel("tituloMain", "Chat interactivo", 0, 1)
        self.app.setLabelFg("tituloMain", "black")
        self.app.setLabelFont("tituloMain", size=18, weight="bold")
        self.app.stopFrame()

        
        self.app.addLabelEntry("Mensaje")

        self.app.addButtons(["Volver", "Enviar"], print("as"))
        self.app.stopFrame()
        
        self.app.startFrame("OPTIONS")
        self.app.setBg("gray")
        self.app.setPadding([20,20])
        self.app.startFrame("OPTIONSTITLE")
        self.app.addLabel("OptionTitle", "Seleccione una acción",0,1)
        self.app.setLabelFg("OptionTitle", "black")
        self.app.setLabelFont("OptionTitle", size=18, weight="bold")
        self.app.stopFrame()
        self.app.startFrame("BUTTONSOPTIONS")
        self.app.addButton("Descargar BORAS", print("as"), 0, 0)
        self.app.addButton("A implementar", print("as"), 0, 1)
        self.app.addButton("A implementarr", print("as"), 1, 0)
        self.app.addButton("A implementarrr", print("as"), 1, 1)
        self.app.stopFrame()
        self.app.addButton("Salir", print("as"))
        self.app.stopFrame()
        
        self.app.stopFrameStack()
        self.app.go()
        pass

chat = Main()
