import requests 
import os

pokemon = input("Give a pokemon name for its pokedex entry and sprite: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}/").json()
pokedex_entry = response['flavor_text_entries'][0]['flavor_text']
print(pokedex_entry)

sprite_response = requests.get(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}/").json()['sprites']['front_default'])
file_path = os.path.join(os.getcwd(), f'{pokemon.lower()}.png')

# Write the image content to the file
with open(file_path, 'wb') as file:
    file.write(sprite_response.content)
    

 