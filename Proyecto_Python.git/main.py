"""
Proyecto Python y mysql:
-Abrir asistente
- Login o registro
- si elegimos registro. Creara un usuario en la base de datos
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, Mostrar notas, Borrarlas.
"""

from usuarios import acciones

print("""
Acciones disponibles:
    -login
    -registro
""")

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()

