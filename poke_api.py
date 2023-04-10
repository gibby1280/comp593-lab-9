""""
Library for interacting with the PokeAPU.
https://pokeapt.co/
"""


import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon):
    """Gets information aobut a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)
    
    Returns:
        dict: Dicitionary of Pokemon information, if successful. Otherwise None.
    """


    pokemon = str(pokemon).strip().lower()

    if pokemon == '':
        print('Error: No Pokemon name given')
        return 
    
    print(f'Getting information for {pokemon}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return