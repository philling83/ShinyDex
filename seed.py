import requests

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")

data = pokemon.json()['results']

list_of_sprites = []
list_of_names = []

# for x in data:
#   print(x['name'].capitalize())

for x in range(1, 152):
  pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{x}")
  img = pokemon.json()['sprites']['front_shiny']
  name = pokemon.json()['species']['name']
  list_of_sprites.append(img)
  list_of_names.append(name.capitalize())

# print(list_of_sprites)
# print(list_of_names)
def show():
  for (a, b) in zip(list_of_sprites, list_of_names):
    print([a, b])

show()
