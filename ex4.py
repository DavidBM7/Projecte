# Definimos una clase base para las tarjetas gráficas
class grafica():
    def __init__(self, marca, nom, ram, frecuencia):
        self.marca = marca  # Marca de la tarjeta gráfica
        self.nom = nom  # Nombre del modelo
        self.ram = ram  # Memoria RAM de la tarjeta gráfica
        self.frecuencia = frecuencia  # Frecuencia de la tarjeta gráfica

    # Métodos para obtener los atributos (actualmente sin implementar)
    def getmarca(self):
        pass
    def getnom(self):
        pass
    def getram(self):
        pass
    def getfrecuencia(self):
        pass

# Definimos una clase derivada para un modelo específico de tarjeta gráfica
class un(grafica):
    def getmarca(self):
        print("Nvidia")  # Imprime la marca de la tarjeta gráfica
    def getnom(self):
        print("RTX 4090")  # Imprime el nombre del modelo
    def getram(self):
        print("24GB GDDR6X")  # Imprime la memoria RAM
    def getfrecuencia(self):
        print("2,52 GHz")  # Imprime la frecuencia

# Definimos otra clase derivada para otro modelo específico de tarjeta gráfica
class dos(grafica):
    def getmarca(self):
        print("Nvidia")
    def getnom(self):
        print("GTX 1650")
    def getram(self):
        print("4GB GDDR5")
    def getfrecuencia(self):
        print("1410 MHz")

# Otra clase derivada para un modelo de tarjeta gráfica de AMD
class tres(grafica):
    def getmarca(self):
        print("AMD")
    def getnom(self):
        print("RX 6600")
    def getram(self):
        print("8GB GDDR6")
    def getfrecuencia(self):
        print("2044 MHz")

# Otra clase derivada para otro modelo específico de Nvidia
class quatre(grafica):
    def getmarca(self):
        print("Nvidia")
    def getnom(self):
        print("RTX 3090")
    def getram(self):
        print("24GB GDDR6X")
    def getfrecuencia(self):
        print("1,70 GHz")

# Otra clase derivada para otro modelo específico de AMD
class cinc(grafica):
    def getmarca(self):
        print("AMD")
    def getnom(self):
        print("RX 7900 XTX")
    def getram(self):
        print("24GB GDDR6")
    def getfrecuencia(self):
        print("2500 MHz")

# Función principal para crear una lista de objetos de las clases derivadas y llamar a sus métodos
def pex4():
    # Creamos una lista de objetos de las clases derivadas con sus atributos específicos
    llista = [
        un("Nvidia", "RTX 4090", "24GB GDDR6X", "2,52 GHz"),
        dos("Nvidia", "GTX 1650", "4GB GDDR5", "1410 MHz"),
        tres("AMD", "RX 6600", "8GB GDDR6", "2044 MHz"),
        quatre("Nvidia", "RTX 3090", "24GB GDDR6X", "1,70 GHz"),
        cinc("AMD", "RX 7900 XTX", "24GB GDDR6", "2500 MHz")
    ]
    
    # Iteramos sobre cada objeto en la lista y llamamos a sus métodos para imprimir los detalles
    for e in llista:
        e.getmarca()  # Llamamos al método para imprimir la marca
        e.getnom()  # Llamamos al método para imprimir el nombre del modelo
        e.getram()  # Llamamos al método para imprimir la memoria RAM
        e.getfrecuencia()  # Llamamos al método para imprimir la frecuencia

# Llamamos a la función principal para ejecutar el código
pex4()
