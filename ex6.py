from flask import Flask  # Importamos la clase Flask desde el módulo flask

app = Flask(__name__)  # Creamos una instancia de la clase Flask, pasándole el nombre del módulo actual

# Definimos una ruta para la URL principal del sitio ("/")
@app.route('/')
def home():
    return "Hola mundo!!! (alt + F4 para recibir 5 euros)"  # Esta función retorna un mensaje cuando alguien visita la URL principal

def pex6():
    print("Se esta ejecutando")  # Imprimimos un mensaje en la consola indicando que la aplicación está en ejecución
    app.run()  # Ejecutamos la aplicación Flask

# Si este archivo se está ejecutando directamente (no importado como módulo), ejecutamos la función pex6
if __name__ == '__main__':
    pex6()
