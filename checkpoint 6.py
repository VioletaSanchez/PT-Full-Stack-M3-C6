# Checkpoint 6
# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase

# Creamos la clase de Usuario
class Usuario:
    # Le pasamos los argumentos de usuario y contraseña. Además los asignamos a self para poder usarlos a continuación
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña


# Instanciamos la clase
usuario_uno = Usuario("Violeta", "1234")

# Enseñamos usuario_uno por pantalla, que nos permite ver el objeto Usuario y dónde está en memoria
print(usuario_uno)