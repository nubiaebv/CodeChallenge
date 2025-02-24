import unittest
from api_client import obtener_lista_pokemon, obtener_detalle_pokemon


class TestAPIClient(unittest.TestCase):

    def test_obtener_lista_pokemon(self):
        """Prueba para verificar que se obtiene la lista de Pokémon correctamente."""
        pokemones = obtener_lista_pokemon(limite=5)
        self.assertEqual(len(pokemones), 5)  # Verificamos que se obtienen 5 Pokémon
        self.assertIn("name", pokemones[0])  # Verificamos que cada Pokémon tiene un "name"

    def test_obtener_detalle_pokemon(self):
        """Prueba para verificar que se obtienen los detalles de un Pokémon."""
        detalles = obtener_detalle_pokemon("bulbasaur")
        self.assertIsNotNone(detalles)  # Verificamos que los detalles no son None
        self.assertIn("name", detalles)  # Verificamos que los detalles contienen el nombre
        self.assertIn("height", detalles)  # Verificamos que los detalles contienen la altura
        self.assertIn("weight", detalles)  # Verificamos que los detalles contienen el peso


if __name__ == "__main__":
    unittest.main()
