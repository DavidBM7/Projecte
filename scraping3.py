"""import requests
for i in range(1000):
	a = "https://pokeapi.co/api/v2/evolution-chain/"+str((i+1))
	res=requests.get(a)
	if res.status_code == 200:
		dades = res.json()
		print("El nom del pokémon és: {}".format(dades["chain"]["species"]["name"]))
		for e in dades["chain"]["evolves_to"]:
			print("Nom de la seva evolució: ", e["species"]["name"])
	else:
	    print("No hi ha dades.")"""

import requests

for i in range(1000):
    url = f"https://pokeapi.co/api/v2/evolution-chain/{i + 1}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemon_name = data["chain"]["species"]["name"]
        print(f"El nom del pokémon és: {pokemon_name}")
        
        for evolution in data["chain"]["evolves_to"]:
            evolution_name = evolution["species"]["name"]
            min_level = evolution["evolution_details"][0]["min_level"]
            print(f"Nom de la seva evolució: {evolution_name}, Nivell mínim: {min_level}")
    else:
        print("No hi ha dades.")