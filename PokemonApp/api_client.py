import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def obtener_lista_pokemon(limite=20, offset=0):
    """
    Obtiene una lista de Pokémon desde la Pokémon API.
    """
    url = f"{BASE_URL}pokemon?limit={limite}&offset={offset}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos["results"]  # Devuelve una lista de Pokémon
    else:
        print("Error al obtener la lista de Pokémon")
        return []

def obtener_detalle_pokemon(nombre):
    """
    Obtiene los detalles de un Pokémon específico por su nombre.
    """
    url = f"{BASE_URL}pokemon/{nombre}"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        return respuesta.json()  # Devuelve los detalles del Pokémon
    else:
        print(f"Error al obtener detalles de {nombre}")
        return None


# Prueba básica
if __name__ == "__main__":
    print("Obteniendo lista de Pokémon...")
    pokemones = obtener_lista_pokemon()
    for pokemon in pokemones:
        print(pokemon["name"])

    print("\nObteniendo detalles del primer Pokémon...")
    if pokemones:
        detalle = obtener_detalle_pokemon(pokemones[0]["name"])
        print(detalle)
