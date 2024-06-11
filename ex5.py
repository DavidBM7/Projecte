import requests

def si(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        types = [t["type"]["name"] for t in data["types"]]
        return types
    else:
        return None

def pex5():
    for i in range(151):  # Solo hasta el ID 151 para la primera generación
        url = f"https://pokeapi.co/api/v2/evolution-chain/{i + 1}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            pokemon_name = data["chain"]["species"]["name"]
            print(f"El nom del pokémon és: {pokemon_name}")
            
            for evolution in data["chain"]["evolves_to"]:
                evolution_name = evolution["species"]["name"]
                print(f"Nom de la seva evolució: {evolution_name}")
        else:
            print("No hi ha dades.")
