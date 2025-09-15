from django.shortcuts import render
from django.views.decorators.cache import never_cache

import requests
import random

from .utils import get_pokemon, calculate_winner

@never_cache
def home(request, template="battlecards/home.html"):
    users_pokemon = get_pokemon()
    
    return render(request, template, {"users_pokemon":users_pokemon, "range_5": range(5)})
    
@never_cache
def select_card(request, card_id, template="battlecards/includes/game_board_inc.html"):
    print("card_id", card_id)
    random_pokemon_id = random.randint(1, 1010)
    users_card = get_pokemon(card_id)
    computers_card = get_pokemon(random_pokemon_id)
    winner = calculate_winner(users_card, computers_card)

    return render(request, template, {"users_card": users_card, "computers_card": computers_card})
    
    # return render(request, template, {"users_pokemon":users_pokemon, "computers_pokemon": computers_pokemon})
    
