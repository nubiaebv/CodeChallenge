import tkinter as tk
from tkinter import messagebox
from api_client import obtener_lista_pokemon, obtener_detalle_pokemon
from crud import agregar_pokemon_local, eliminar_pokemon_local, editar_pokemon_local

# Definir colores a usar:
POKEMON_YELLOW = "#FFCB05"  # Amarillo Pokémon (Pikachu)
POKEMON_BLUE = "#3B4CCA"  # Azul Pokémon
POKEMON_RED = "#FF0000"  # Rojo de contraste (opcional)
POKEMON_BLACK = "#000000"
TEXT_WHITE = "#FFFFFF"
TEXT_BLACK = "#000000"
TEXT_YELLOW = "#FFCB05"

class PokemonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokémon App")
        # Centrar ventana
        self.centrar_ventana(810, 810)  # Ajusta el tamaño como desees

        # Deshabilitar botón de maximizar
        self.root.resizable(False, False)

        # Dar color al fondo de la ventana
        self.root.configure(bg=POKEMON_BLUE)

        # --- TÍTULO PRINCIPAL ---
        self.label_titulo = tk.Label(
            root,
            text="Lista de Pokémon",
            font=("Arial", 16, "bold"),
            bg=POKEMON_BLUE,
            fg=POKEMON_YELLOW
        )
        self.label_titulo.pack(pady=10)

        # --- LISTA DE POKÉMON (LISTBOX) ---
        self.lista_pokemon = tk.Listbox(
            root,
            width=50,
            height=15,
            font=("Arial", 12),
        )
        self.lista_pokemon.pack(pady=10)

        # --- BOTÓN PARA VER DETALLES ---
        self.boton_detalle = tk.Button(
            root,
            text="Ver Detalles",
            command=self.mostrar_detalle,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,  # Color cuando se presiona
            activeforeground=TEXT_WHITE
        )
        self.boton_detalle.pack(pady=5)

        # --- SECCIÓN: AGREGAR POKÉMON ---
        self.label_acciones = tk.Label(
            root,
            text="Agregar Pokémon",
            font=("Arial", 12, "bold"),
            bg=POKEMON_BLUE,
            fg=POKEMON_YELLOW
        )
        self.label_acciones.pack(pady=5)

        self.nombre_pokemon = tk.Entry(
            root,
            font=("Arial", 12),
            bg="white",
            fg=TEXT_BLACK
        )
        self.nombre_pokemon.pack(pady=5)

        self.boton_agregar = tk.Button(
            root,
            text="Agregar Pokémon",
            command=self.agregar_pokemon,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,
            activeforeground=TEXT_WHITE
        )
        self.boton_agregar.pack(pady=5)

        self.boton_eliminar = tk.Button(
            root,
            text="Eliminar Pokémon",
            command=self.eliminar_pokemon,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,
            activeforeground=TEXT_WHITE
        )
        self.boton_eliminar.pack(pady=5)

        # --- SECCIÓN: EDITAR POKÉMON ---
        self.label_acciones = tk.Label(
            root,
            text="Editar Pokémon",
            font=("Arial", 12, "bold"),
            bg=POKEMON_BLUE,
            fg=POKEMON_YELLOW
        )
        self.label_acciones.pack(pady=5)

        self.boton_editar = tk.Button(
            root,
            text="Editar Pokémon",
            command=self.editar_pokemon,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,
            activeforeground=TEXT_WHITE
        )
        self.boton_editar.pack(pady=5)

        # Cuadros de texto para la edición
        self.nombre_pokemon_editar = tk.Entry(
            root,
            font=("Arial", 12),
            bg="white",
            fg=TEXT_BLACK
        )
        self.nombre_pokemon_editar.pack(pady=5)

        self.altura_pokemon_editar = tk.Entry(
            root,
            font=("Arial", 12),
            bg="white",
            fg=TEXT_BLACK
        )
        self.altura_pokemon_editar.pack(pady=5)

        self.peso_pokemon_editar = tk.Entry(
            root,
            font=("Arial", 12),
            bg="white",
            fg=TEXT_BLACK
        )
        self.peso_pokemon_editar.pack(pady=5)

        self.habilidades_pokemon_editar = tk.Entry(
            root,
            font=("Arial", 12),
            bg="white",
            fg=TEXT_BLACK
        )
        self.habilidades_pokemon_editar.pack(pady=5)

        # Botón para guardar los cambios
        self.boton_guardar = tk.Button(
            root,
            text="Guardar Cambios",
            command=self.guardar_cambios,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,
            activeforeground=TEXT_WHITE
        )
        self.boton_guardar.pack(pady=5)

        # Botón para cancelar los cambios
        self.boton_cancelar = tk.Button(
            root,
            text="Cancelar",
            command=self.cancelar_edicion,
            bg=POKEMON_YELLOW,
            fg=TEXT_BLACK,
            activebackground=POKEMON_RED,
            activeforeground=TEXT_WHITE
        )
        self.boton_cancelar.pack(pady=5)
        # Cargar la lista de Pokémon
        self.pokemones_locales = []  # Lista para almacenar los Pokémon personalizados
        self.cargar_pokemones()

        # Almacenar el Pokémon original para poder restaurarlo
        self.pokemon_original = None

    def centrar_ventana(self, ancho=600, alto=400):
        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2

        # Establecer el tamaño y la posición de la ventana
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def cargar_pokemones(self):
        """Obtiene y muestra la lista de Pokémon en el Listbox."""
        self.lista_pokemon.delete(0, tk.END)  # Limpiar la lista actual
        pokemones = obtener_lista_pokemon()  # Obtener los primeros 20 Pokémon desde la API

        # Añadir los Pokémon iniciales a la lista local (si no están ya en ella)
        for pokemon in pokemones:
            if not any(p['name'] == pokemon["name"] for p in
                       self.pokemones_locales):  # Verificar si ya está en la lista local
                detalles_pokemon = obtener_detalle_pokemon(pokemon["name"])
                if detalles_pokemon:
                    pokemon_completo = {
                        'name': detalles_pokemon['name'],
                        'height': detalles_pokemon['height'],
                        'weight': detalles_pokemon['weight'],
                        'abilities': [{'ability': {'name': ab['ability']['name']}} for ab in
                                      detalles_pokemon['abilities']]
                    }
                    self.pokemones_locales.append(pokemon_completo)  # Agregar a la lista local

            # Añadir el nombre del Pokémon al Listbox (sin duplicados)
            self.lista_pokemon.insert(tk.END, pokemon["name"])

        # Añadir los Pokémon locales a la lista (sin duplicados)
        for pokemon in self.pokemones_locales:
            if pokemon['name'] not in [self.lista_pokemon.get(i) for i in range(self.lista_pokemon.size())]:
                self.lista_pokemon.insert(tk.END, pokemon['name'])

    def mostrar_detalle(self):
        """Muestra detalles del Pokémon seleccionado."""
        seleccionado = self.lista_pokemon.curselection()

        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un Pokémon de la lista.")
            return

        nombre_pokemon = self.lista_pokemon.get(seleccionado)

        # Buscar el Pokémon en los locales
        pokemon_local = next((p for p in self.pokemones_locales if p['name'] == nombre_pokemon), None)
        if pokemon_local:
            detalles = pokemon_local  # Si está en la lista local, usa los detalles locales
        else:
            # Si no está en la lista local, obtén los detalles desde la API
            detalles = obtener_detalle_pokemon(nombre_pokemon)

        if detalles:
            info = f"Nombre: {detalles['name']}\n"
            info += f"Altura: {detalles['height']}\n"
            info += f"Peso: {detalles['weight']}\n"
            info += "Habilidades:\n"
            for habilidad in detalles['abilities']:
                info += f" - {habilidad['ability']['name']}\n"

            messagebox.showinfo("Detalles del Pokémon", info)

    def agregar_pokemon(self):
        """Agrega un Pokémon a la lista desde la API."""
        pokemon_nombre = self.nombre_pokemon.get().strip()  # Obtener nombre del campo

        if pokemon_nombre:
            # Consultamos la API para obtener los detalles completos del Pokémon
            detalles_pokemon = obtener_detalle_pokemon(pokemon_nombre)

            if detalles_pokemon:
                # Extraemos los detalles que nos interesan
                pokemon = {
                    'name': detalles_pokemon['name'],
                    'height': detalles_pokemon['height'],
                    'weight': detalles_pokemon['weight'],
                    'abilities': [{'ability': {'name': ab['ability']['name']}} for ab in detalles_pokemon['abilities']]
                }

                # Ahora, agregamos el Pokémon a la lista local
                if agregar_pokemon_local(pokemon, self.pokemones_locales):
                    self.cargar_pokemones()  # Actualizamos la lista de Pokémon
                    self.nombre_pokemon.delete(0, tk.END)  # Limpiar el campo de texto
                else:
                    messagebox.showwarning("Atención", "Este Pokémon ya está en la lista.")
            else:
                messagebox.showwarning("Error", "No se encontró el Pokémon en la API.")
        else:
            messagebox.showwarning("Atención", "Escribe un nombre de Pokémon.")

    def eliminar_pokemon(self):
        """Elimina un Pokémon de la lista."""
        seleccionado = self.lista_pokemon.curselection()

        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un Pokémon de la lista.")
            return

        pokemon_nombre = self.lista_pokemon.get(seleccionado)
        if eliminar_pokemon_local(pokemon_nombre, self.pokemones_locales):
            self.cargar_pokemones()  # Actualizar la lista
        else:
            messagebox.showwarning("Atención", "No se pudo eliminar el Pokémon.")

    def editar_pokemon(self):
        """Carga los datos del Pokémon seleccionado para editar."""
        seleccionado = self.lista_pokemon.curselection()

        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un Pokémon de la lista.")
            return

        pokemon_nombre = self.lista_pokemon.get(seleccionado)

        # Buscar el Pokémon en la lista local
        pokemon = next((p for p in self.pokemones_locales if p['name'] == pokemon_nombre), None)
        if pokemon:
            # Almacenar el Pokémon original para restaurarlo si se cancela
            self.pokemon_original = pokemon.copy()

            # Autocompletar los campos con los datos del Pokémon seleccionado
            self.nombre_pokemon_editar.delete(0, tk.END)
            self.nombre_pokemon_editar.insert(0, pokemon['name'])
            self.altura_pokemon_editar.delete(0, tk.END)
            self.altura_pokemon_editar.insert(0, pokemon['height'])
            self.peso_pokemon_editar.delete(0, tk.END)
            self.peso_pokemon_editar.insert(0, pokemon['weight'])
            self.habilidades_pokemon_editar.delete(0, tk.END)
            self.habilidades_pokemon_editar.insert(0, ', '.join(
                [h['ability']['name'] for h in pokemon['abilities']]))  # Convertir habilidades a texto

    def guardar_cambios(self):
        """Guarda los cambios realizados en un Pokémon."""
        seleccionado = self.lista_pokemon.curselection()

        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un Pokémon de la lista.")
            return

        pokemon_antiguo = self.lista_pokemon.get(seleccionado)

        # Obtener los nuevos valores desde los cuadros de texto
        nombre_nuevo = self.nombre_pokemon_editar.get().strip()
        altura_nueva = self.altura_pokemon_editar.get().strip()
        peso_nuevo = self.peso_pokemon_editar.get().strip()
        habilidades_nuevas = self.habilidades_pokemon_editar.get().strip().split(',')  # Separar habilidades por coma

        if nombre_nuevo and altura_nueva and peso_nuevo and habilidades_nuevas:
            pokemon_nuevo = {
                'name': nombre_nuevo,
                'height': float(altura_nueva),
                'weight': float(peso_nuevo),
                'abilities': [{'ability': {'name': h.strip()}} for h in habilidades_nuevas]
            }
            if editar_pokemon_local(pokemon_antiguo, pokemon_nuevo, self.pokemones_locales):
                self.cargar_pokemones()  # Actualizar la lista
                self.nombre_pokemon_editar.delete(0, tk.END)  # Limpiar los cuadros de texto
                self.altura_pokemon_editar.delete(0, tk.END)
                self.peso_pokemon_editar.delete(0, tk.END)
                self.habilidades_pokemon_editar.delete(0, tk.END)
            else:
                messagebox.showwarning("Atención", "No se pudo editar el Pokémon.")
        else:
            messagebox.showwarning("Atención", "Rellena todos los campos correctamente.")

    def cancelar_edicion(self):
        """Restaura los datos originales del Pokémon si no se realizaron cambios y limpia los campos de edición."""
        if self.pokemon_original:
            # Restaurar los datos originales en los campos de texto
            self.nombre_pokemon_editar.delete(0, tk.END)
            self.nombre_pokemon_editar.insert(0, self.pokemon_original['name'])
            self.altura_pokemon_editar.delete(0, tk.END)
            self.altura_pokemon_editar.insert(0, self.pokemon_original['height'])
            self.peso_pokemon_editar.delete(0, tk.END)
            self.peso_pokemon_editar.insert(0, self.pokemon_original['weight'])
            self.habilidades_pokemon_editar.delete(0, tk.END)
            self.habilidades_pokemon_editar.insert(0, ', '.join(
                [h['ability']['name'] for h in self.pokemon_original['abilities']]))

            # Limpiar los campos de edición después de cancelar
            self.nombre_pokemon_editar.delete(0, tk.END)
            self.altura_pokemon_editar.delete(0, tk.END)
            self.peso_pokemon_editar.delete(0, tk.END)
            self.habilidades_pokemon_editar.delete(0, tk.END)

            # Limpiar la referencia al Pokémon original
            self.pokemon_original = None


def iniciar_aplicacion():
    root = tk.Tk()  # Aquí se define root
    app = PokemonApp(root)
    root.mainloop()
