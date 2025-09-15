
import requests
import random

def api_call(pokemon_id=None):
    random_pokemon_id = random.randint(1, 1010)
    if pokemon_id:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}"

    response = requests.get(url)
    selected_pokemon = response.json()
    return selected_pokemon

def get_pokemon(pokemon_id=None):
    pokemon = []
    if pokemon_id:
        return api_call(pokemon_id)  # returns a dict
    else:
        pokemon = []
        for i in range(5):
            selected_pokemon = api_call()
            if selected_pokemon['sprites']['front_shiny']:
                print(f"{selected_pokemon['name']} has a shiny!")
            else:
                print(f"{selected_pokemon['name']} does not have a shiny")
            pokemon.append(selected_pokemon)
        return pokemon
    
def calculate_winner(users_card, computers_card):
    # calculate from the stats which card is the winner
    return