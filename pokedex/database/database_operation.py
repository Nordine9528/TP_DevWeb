from database.database import init_connection

def get_type_in_pkmn_type(name: str):
    connection = init_connection()
    row = connection.execute(
        "SELECT * FROM pokemon_types WHERE name = ?", (name,)
    ).fetchone()
    connection.close()
    return dict(row) if row else None

def insert_types(list_type_fr : str, list_type_en: str):
    #Possibilité de faire une fonction iterable sur une list de tuple (feu : fire)
    connection = init_connection()

    connection.executemany(
        "INSERT OR IGNORE INTO pokemon_types (id, name, name_fr) VALUES (?, ?, ?)",
        [(i, en, fr) for i, (en, fr) in enumerate(zip(list_type_en, list_type_fr))],
    )

    connection.commit()
    connection.close()