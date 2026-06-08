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

    contra = input("Ingrese la contraseña del usuario: ").strip()
    cont = 0
    if len(contra) > 8:
        for i in range(len(contra)):
            pos = contra[i]
            if (pos == "1") or (pos == "2") or (pos == "3") or (pos == "4") or (pos == "5") or (pos == "6") or (pos == "7") or (pos == "8") or (pos == "9") or (pos == "0"):
                cont = cont + 1
        if cont > 0:
            if " " in contra:
                print("Ingreso inválido")
                return
            else:
                usuarios[nombre_usr] = [sexo, contra]

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