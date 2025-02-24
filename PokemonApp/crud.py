
def agregar_pokemon_local(pokemon, pokemones_locales):
    """Agrega un Pokémon personalizado a la lista de Pokémon locales."""
    if pokemon['name'] and pokemon['name'] not in [p['name'] for p in pokemones_locales]:
        pokemones_locales.append(pokemon)
        return True
    return False

def eliminar_pokemon_local(pokemon_nombre, pokemones_locales):
    """Elimina un Pokémon de la lista de Pokémon locales."""
    for pokemon in pokemones_locales:
        if pokemon['name'] == pokemon_nombre:
            pokemones_locales.remove(pokemon)
            return True
    return False

def editar_pokemon_local(pokemon_antiguo, pokemon_nuevo, lista_pokemones):
    """Edita un Pokémon en la lista local."""
    for i, pokemon in enumerate(lista_pokemones):
        if pokemon['name'] == pokemon_antiguo:
            lista_pokemones[i] = pokemon_nuevo  # Actualizar con el nuevo Pokémon
            return True
    return False


