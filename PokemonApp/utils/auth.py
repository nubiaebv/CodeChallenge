
usuarios = {
    "nbrenes": "1234",
    "pmarin": "12345"
}

def verificar_credenciales(usuario, contrasena):
    """Verifica si las credenciales son válidas."""
    if usuario in usuarios and usuarios[usuario] == contrasena:
        return True
    return False