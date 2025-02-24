# ui/login.py
import tkinter as tk
from tkinter import messagebox
from utils.auth import verificar_credenciales

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.on_login_success = on_login_success

        self.etiqueta_usuario = tk.Label(root, text="Usuario:")
        self.etiqueta_usuario.pack()

        self.entrada_usuario = tk.Entry(root)
        self.entrada_usuario.pack()

        self.etiqueta_contrasena = tk.Label(root, text="Contraseña:")
        self.etiqueta_contrasena.pack()

        self.entrada_contrasena = tk.Entry(root, show="*")
        self.entrada_contrasena.pack()

        self.boton_inicio = tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.boton_inicio.pack(pady=10)

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contrasena = self.entrada_contrasena.get()

        if verificar_credenciales(usuario, contrasena):
            self.on_login_success()
        else:
            messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas")