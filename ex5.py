# Importamos el módulo requests para hacer peticiones HTTP
import requests  

# Definimos una función que toma el nombre de un Pokémon y retorna sus tipos
def si(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"  # Construimos la URL para obtener los datos del Pokémon
    response = requests.get(url)  # Hacemos una petición GET a la URL

    if response.status_code == 200:  # Verificamos si la respuesta fue exitosa
        data = response.json()  # Convertimos la respuesta JSON en un diccionario de Python
        types = [t["type"]["name"] for t in data["types"]]  # Extraemos los tipos del Pokémon
        return types  # Retornamos la lista de tipos
    else:
        return None  # Si la respuesta no fue exitosa, retornamos None

# Definimos una función que obtiene y muestra las cadenas de evolución de los primeros 151 Pokémon
def pex5():
    for i in range(151):  # Iteramos desde 0 hasta 150 (para obtener los primeros 151 Pokémon)
        url = f"https://pokeapi.co/api/v2/evolution-chain/{i + 1}"  # Construimos la URL para la cadena de evolución
        response = requests.get(url)  # Hacemos una petición GET a la URL
        
        if response.status_code == 200:  # Verificamos si la respuesta fue exitosa
            data = response.json()  # Convertimos la respuesta JSON en un diccionario de Python
            pokemon_name = data["chain"]["species"]["name"]  # Obtenemos el nombre del Pokémon base
            print(f"El nom del pokémon és: {pokemon_name}")  # Imprimimos el nombre del Pokémon
            
            for evolution in data["chain"]["evolves_to"]:  # Iteramos sobre las evoluciones del Pokémon base
                evolution_name = evolution["species"]["name"]  # Obtenemos el nombre de la evolución
                print(f"Nom de la seva evolució: {evolution_name}")  # Imprimimos el nombre de la evolución
        else:
            print("No hi ha dades.")  # Si la respuesta no fue exitosa, imprimimos un mensaje indicando que no hay datos

