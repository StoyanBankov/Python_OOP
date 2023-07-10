import string
from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: string):
        try:
            pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
        except IndexError:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)

        return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])

        return f"Pokemon Trainer {self.name}\n" +\
               f"Pokemon count {len(self.pokemons)}\n" +\
               f"{pokemons_data}"
