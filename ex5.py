import requests

def get_pokemon_type(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        types = [t["type"]["name"] for t in data["types"]]
        return types
    else:
        return None

for i in range(1000):
    url = f"https://pokeapi.co/api/v2/evolution-chain/{i + 1}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_name = data["chain"]["species"]["name"]
        pokemon_types = get_pokemon_type(pokemon_name)
        types_text = ", ".join(pokemon_types) if pokemon_types else "Desconegut"
        print(f"El nom del pokémon és: {pokemon_name}, Tipus: {types_text}")
        
        for evolution in data["chain"]["evolves_to"]:
            evolution_name = evolution["species"]["name"]
            min_level = evolution["evolution_details"][0]["min_level"] if evolution["evolution_details"] else None
            min_level_text = f", Nivell mínim: {min_level}" if min_level is not None else ", Nivell mínim: No especificat"
            evolution_types = get_pokemon_type(evolution_name)
            evolution_types_text = ", ".join(evolution_types) if evolution_types else "Desconegut"
            print(f"Nom de la seva evolució: {evolution_name}, Tipus: {evolution_types_text}{min_level_text}")
    else:
        print("No hi ha dades.")
