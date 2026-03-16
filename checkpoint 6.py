# Checkpoint 6
# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y un mail. Crea un objeto usando la clase

# Creamos la clase de Usuario
class Usuario:
    # Le pasamos los argumentos de usuario y mail. Además los asignamos a self para poder usarlos a continuación
    def __init__(self, usuario, mail):
        self.usuario = usuario
        self.mail = mail

    # Retornamos un f-string con el usuario y el mail.
        print(f"Información obtenida. Usuario: {self.usuario}. Mail: {self.mail}.")

# Instanciamos la clase
usuario_uno = Usuario("Violeta", "vi@gmail.com")
usuario_dos = Usuario("Daphne", "daphne@gmail.com")
usuario_tres = Usuario("Jon Ander", "motocross@protonmail.com")
usuario_cuatro = Usuario("Lisa", "LH@gmail.com")

# Enseñamos por pantalla múltiples usuarios
print("\nEnseñamos los siguientes mensajes a los usuarios.\n")
print(f"Hola, {usuario_uno.usuario}. Tu correo electrónico es : {usuario_uno.mail}")

print(f"Hola, {usuario_dos.usuario}. Tu correo electrónico es : {usuario_dos.mail}")

print(f"Hola, {usuario_tres.usuario}. Tu correo electrónico es : {usuario_tres.mail}")

print(f"Hola, {usuario_cuatro.usuario}. Tu correo electrónico es : {usuario_cuatro.mail}")