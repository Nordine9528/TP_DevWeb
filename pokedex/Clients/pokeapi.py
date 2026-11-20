import requests

type_list_FR = []

def get_pokemon_from_api(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    response_json = response.json()
    return response_json


def get_pokemon_fr_name(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    response_json = response.json()
    name = None

    for i in range(len(response_json['names'])):
        if response_json['names'][i]['language']['name'] == "fr":
            name = response_json['names'][i]['name']
            break
        else:
            name = response_json['names']
    return name


def get_type_list_EN():
    response = requests.get("https://pokeapi.co/api/v2/type")
    response_json = response.json()
    type_list_EN = []

    for i in range(len(response_json['results'])):
        type_list_EN.append(response_json['results'][i]['name'])

    return type_list_EN #liste de chaine de caractere


def get_type_list_FR(name_list_EN):
    type_list_FR.clear()
    en_2_fr = dict()

    for name in name_list_EN:
        response = requests.get(f"https://pokeapi.co/api/v2/type/{name}")
        response_json = response.json()

        nom_fr = ""
        for translated_name in response_json['names']:
            if translated_name['language']['name'] == "fr":
                nom_fr = translated_name['name']
                break
        en_2_fr[name] = nom_fr
    print(en_2_fr)

    return en_2_fr


def get_type_pokemon(pokemon_json):
    type_list_EN = get_type_list_EN()
    type1 = type2 = ""

    if (len(pokemon_json['types']) < 2):
        type1 = pokemon_json['types'][0]['type']['name']
    else:
        type1, type2 = pokemon_json['types'][0]['type']['name'], pokemon_json['types'][1]['type']['name']

    if len(type_list_FR) != len(type_list_EN):
        get_type_list_FR(type_list_EN)

    if len(type_list_FR) == len(type_list_EN):
        for i in range(len(type_list_EN)):
            j = type_list_EN[i]
            if j == type1:
                type1 = type_list_FR[i]
            if j == type2:
                type2 = type_list_FR[i]

    return type1, type2

def get_pre_evolution_pokemon(pokemon_id : int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    response_json = response.json()

    pre_evl_pokemon_name = None
    pre_evl_pokemon_id = None

    if response_json['evolves_from_species']:
        pre_evl_pokemon_name = response_json['evolves_from_species']['name']
        pre_evl_pokemon_id = int(response_json['evolves_from_species']["url"].rstrip("/").split("/")[-1])

        if pre_evl_pokemon_id > 151:
            pre_evl_pokemon_name = None
            pre_evl_pokemon_id = None


    return pre_evl_pokemon_name, pre_evl_pokemon_id

