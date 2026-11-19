import json
from database.database import init_connection
from schemas.pokemon import Pokemon


def get_pokemon_by_number(number: int) -> Pokemon | None:
    connection = init_connection()
    row = connection.execute(
        "SELECT * FROM pokemon WHERE number = ?", (number,)
    ).fetchone()
    connection.close()

    if row is None:
        return None

    return Pokemon(
        number=row["number"],
        name=row["name"],
        name_fr=row["name_fr"],
        types=json.loads(row["types"]),          # texte JSON -> liste
        image_url=row["image_url"],
        height=row["height"],
        weight=row["weight"],
        evolves_from_number=row["evolves_from_number"],
    )


def insert_pokemon(pokemon: Pokemon):
    connection = init_connection()
    connection.execute(
        """
        INSERT INTO pokemon
            (number, name, name_fr, types, image_url, height, weight, evolves_from_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon.number,
            pokemon.name,
            pokemon.name_fr,
            json.dumps(pokemon.types, ensure_ascii=False),   # liste -> texte JSON
            pokemon.image_url,
            pokemon.height,
            pokemon.weight,
            pokemon.evolves_from_number,
        ),
    )
    connection.commit()
    connection.close()

def get_type_by_name(name: str):
    connection = init_connection()
    row = connection.execute(
        "SELECT * FROM pokemon_types WHERE name = ?", (name,)
    ).fetchone()
    connection.close()
    return dict(row) if row else None


def insert_type(type_id: int, name: str, name_fr: str):
    connection = init_connection()
    connection.execute(
        "INSERT INTO pokemon_types (id, name, name_fr) VALUES (?, ?, ?)",
        (type_id, name, name_fr),
    )
    connection.commit()
    connection.close()