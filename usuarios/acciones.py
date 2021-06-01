import usuarios.usuario as modelo
import notas.acciones 


class Acciones:

    def registro(self):
        print("\nOk!!! Vamos a registrarte en el sistema...")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Cual es tu email?: ")
        password = input("Cual es tu password?: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro [0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email} ")

        else:
            print("\nNo te has registrado correctamente")


    def login(self):
        print("\nPerfecto!!! Identificate en el sistema...")

        try:
            email = input("Cual es tu email?: ")
            password = input("Cual es tu password?: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print (f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Que deseas hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"\nOk, {usuario[1]}, Hasta pronto!!!")
            exit()  
    

