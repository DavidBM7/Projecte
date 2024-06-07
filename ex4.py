class grafica():
    def __init__(self,marca,nom,ram,frecuencia):
        self.marca=marca
        self.nom=nom
        self.ram=ram
        self.frecuencia=frecuencia

    def getmarca(self):
        pass
    def getnom(self):
        pass
    def getram(self):
        pass
    def getfrecuencia(self):
        pass

class un(grafica):
    def getmarca(self):
        print("Nvidia")
    def getnom(self):
        print("RTX 4090")
    def getram(self):
        print("24GB GDDR6X")
    def getfrecuencia(self):
        print("2,52 GHz")

class dos(grafica):
    def getmarca(self):
        print("Nvidia")
    def getnom(self):
        print("GTX 1650")
    def getram(self):
        print("4GB GDDR5")
    def getfrecuencia(self):
        print("1410 MHz")

class tres(grafica):
    def getmarca(self):
        print("AMD")
    def getnom(self):
        print("RX 6600")
    def getram(self):
        print("8GB GDDR6")
    def getfrecuencia(self):
        print("2044 MHz")

class quatre(grafica):
    def getmarca(self):
        print("Nvidia")
    def getnom(self):
        print("RTX 3090")
    def getram(self):
        print("24GB GDDR6X")
    def getfrecuencia(self):
        print("1,70 GHz")

class cinc(grafica):
    def getmarca(self):
        print("AMD")
    def getnom(self):
        print("RX 7900 XTX")
    def getram(self):
        print("24GB GDDR6")
    def getfrecuencia(self):
        print("2500 MHz")

def pex4():
    llista=[un("Nvidia","RTX 4090","24GB GDDR6X","2,52 GHz"),dos("Nvidia","GTX 1650","4GB GDDR5","1410 MHz"),tres("AMD","RX 6600","8GB GDDR6","2044 MHz"),quatre("Nvidia","RTX 3090","24GB GDDR6X","1,70 GHz"),cinc("AMD","RX 7900 XTX","24GB GDDR6","2500 MHz")]
    for e in llista:
        e.getmarca()
        e.getnom()
        e.getram()
        e.getfrecuencia()
            
    