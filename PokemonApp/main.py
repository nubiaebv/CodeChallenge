import tkinter as tk
from ui.login import LoginWindow
from ui.ui import iniciar_aplicacion

def iniciar_sesion_exitoso():
    ventana_login.destroy()
    iniciar_aplicacion()

ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")

# Deshabilitar el botón de maximizar
ventana_login.resizable(False, False)

# Dar color al fondo de la ventana (ejemplo: gris claro)
ventana_login.configure(bg="#ECECEC")

# Establecer el tamaño de la ventana
ancho_ventana = 300
alto_ventana = 200
ventana_login.geometry(f"{ancho_ventana}x{alto_ventana}")

# Centrar la ventana
ancho_pantalla = ventana_login.winfo_screenwidth()
alto_pantalla = ventana_login.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
ventana_login.geometry(f"+{x}+{y}")

# Ejemplo de cómo podrías modificar la clase LoginWindow para personalizar tus labels y entry:
class LoginWindow:
    def __init__(self, master, on_login_success):
        self.master = master
        self.on_login_success = on_login_success

        # Frame contenedor para centralizar widgets
        self.frame = tk.Frame(master, bg="#ECECEC")
        self.frame.pack(expand=True, fill="both")

        # Label de "Usuario"
        self.label_usuario = tk.Label(self.frame, text="Usuario:",
                                      bg="#ECECEC",       # Fondo del label
                                      fg="#333333",       # Color de texto
                                      font=("Arial", 11)) # Fuente
        self.label_usuario.pack(pady=5)

        # Entry para usuario
        self.entry_usuario = tk.Entry(self.frame, font=("Arial", 11))
        self.entry_usuario.pack(pady=5)

        # Label de "Contraseña"
        self.label_contrasena = tk.Label(self.frame, text="Contraseña:",
                                         bg="#ECECEC",
                                         fg="#333333",
                                         font=("Arial", 11))
        self.label_contrasena.pack(pady=5)

        # Entry para contraseña
        self.entry_contrasena = tk.Entry(self.frame, show="*", font=("Arial", 11))
        self.entry_contrasena.pack(pady=5)

        # Botón de inicio de sesión
        self.boton_iniciar = tk.Button(self.frame, text="Iniciar Sesión",
                                       bg="#007ACC",       # Fondo del botón
                                       fg="white",         # Color de texto del botón
                                       activebackground="#005999", # Color de fondo al presionar
                                       font=("Arial", 11, "bold"),
                                       command=self.iniciar_sesion)
        self.boton_iniciar.pack(pady=10)

    def iniciar_sesion(self):
        # Aquí validas usuario y contraseña
        # ...
        self.on_login_success()

login_window = LoginWindow(ventana_login, iniciar_sesion_exitoso)
ventana_login.mainloop()
