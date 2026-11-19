from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import database
from schemas.pokemon import Pokemon
from Services import pokemon_service

app = FastAPI()

database.init_db()


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/pokemons/{number}/scan", response_model=Pokemon)
def scan_pokemon(number: int):
    try:
        return pokemon_service.scan_pokemon(number)
    except pokemon_service.PokemonAlreadyScannedError:
        raise HTTPException(status_code=409, detail="Pokémon déjà enregistré")