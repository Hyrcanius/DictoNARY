def menu():
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")

usuarios = {
    "Barto": ["M", "chamalapachala"],
    "Homero": ["M", "douh666777"],
    "Marge": ["F", "mmhomero69"]
}

usuarios2 = {
    "Moe": {
        "sexo": "M",
        "pass": "barneymylove"
    },
    "Barney": {
        "sexo": "M",
        "pass": "moemylove666"
    },
    "Edna": {
        "sexo": "F",
        "pass": "crabaple23"
    } 
}
def ingresar_usuario(usuarios):
    nombre_usr = input("Ingrese el nombre de usuario: ").capitalize().strip()
    if nombre_usr in usuarios:
        print("Nombre de usuario en uso.")
        return
    
    while True:
        sexo = input("Ingrese el sexo del usuario, (F o M): ")
        if (sexo == "F") or (sexo == "M"):
            break
        else:
            print("Ingreso inválido, use 'F' o 'M'")

    while True:
        contra = input("Ingrese la contraseña del usuario: ").strip()
        cont = 0
        if len(contra) > 8:
            for i in range(len(contra)):
                pos = contra[i]
                if pos.isdigit() == True:
                    cont = cont + 1
            if cont > 0:
                if " " in contra:
                    print("Ingreso inválido")
                else:
                    usuarios[nombre_usr] = [sexo, contra]
                    break
            else:
                print("Contraseña debe tener al menos un número.")


def ingresar_usuario2(usuarios2):
    nombre_usr = input("Ingrese el nombre de usuario: ").strip().capitalize()
    if nombre_usr in usuarios2:
        print("Nombre en uso.")
        return
    
    while True:
        sexo = input("Ingrese el sexo (F o M): ")
        if (sexo == "F") or (sexo == "M"):
            break
        else:
            print("Ingrese una opción válida.")
    
    while True:
        contra = input("Ingrese la contraseña: ").strip()
        cont = 0
        if len(contra) > 8:
            for i in range(len(contra)):
                pos = contra[i]
                if pos.isdigit() == True:
                    cont = cont + 1
            if cont > 0:
                if " " in contra:
                    print("Contraseña inválida.")
                else:
                    usuarios[nombre_usr] = {
                        "sexo": sexo,
                        "contraseña": contra 
                    }
                    break
            else:
                print("Contraseña debe tener al menos un número.")

def buscar_usuario(usuarios):
    nombre = input("Ingrese el nombre de usuario: ").capitalize().strip()
    if nombre in usuarios:
        sexo, contrasena = usuarios[nombre]
        print(f"{sexo}, {contrasena}")
    else:
        print("No se encuentra el usuario.")
        return

def eliminar_usuario(usuarios):
    nombre = input("Ingrese el nombre de usuario: ").capitalize()
    if nombre in usuarios:
        del(usuarios[nombre])
        print("Usuario eliminado!")
        return
    else:
        print("¡No se encuentra el usuario!")

while True:
    menu()

    op = int(input(" -> "))

    if op == 1:
        ingresar_usuario(usuarios)
    elif op == 2:
        buscar_usuario(usuarios)
    elif op == 3:
        eliminar_usuario(usuarios)
    elif op == 4:
        print("Saliendo2")
        break