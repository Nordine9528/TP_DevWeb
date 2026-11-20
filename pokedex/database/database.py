import sqlite3

DB_NAME = "pokedex.db"

def init_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = init_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            name_fr TEXT NOT NULL,
            types TEXT NOT NULL,
            image_url TEXT NOT NULL,
            height INTEGER NOT NULL,
            weight INTEGER NOT NULL,
            evolves_from_number INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon_types (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            name_fr TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("Base de données creee avec succes.")

def init_connection_db_show_tables():
    connection = sqlite3.connect("pokedex.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    tables = cursor.fetchall()

    print([t[0] for t in tables])
    connection.close()


