from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo!!! (alt + F4 para recibir 5 euros)"

def pex6():
    print("Se esta ejecutando")
    app.run()

if __name__ == '__main__':
    pex6()