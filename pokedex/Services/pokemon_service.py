from Clients import pokeapi as f_pokapi
from repositories import pokemon_repository
from schemas.pokemon import Pokemon


class PokemonAlreadyScannedError(Exception):
    pass


def scan_pokemon(pokemon_id: int) -> Pokemon:
    if pokemon_repository.get_pokemon_by_number(pokemon_id):
        raise PokemonAlreadyScannedError(pokemon_id)

    r_json = f_pokapi.get_pokemon_from_api(pokemon_id)
    name_fr = f_pokapi.get_pokemon_fr_name(pokemon_id)
    type1, type2 = f_pokapi.get_type_pokemon(r_json)
    pre_evl_name, pre_evl_id = f_pokapi.get_pre_evolution_pokemon(pokemon_id)

    types = [t for t in (type1, type2) if t != "None"]

    pokemon = Pokemon(
        number=r_json["id"],
        name=r_json["name"],
        name_fr=name_fr,
        types=types,
        image_url=r_json["sprites"]["front_default"],
        height=r_json["height"] * 10,
        weight=r_json["weight"] * 100,
        evolves_from_number=pre_evl_id,
    )


    pokemon_repository.insert_pokemon(pokemon)
    return pokemon