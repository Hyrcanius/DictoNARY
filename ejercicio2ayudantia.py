op = ""
nombre_buscado = ""

def pedir_opcion():
    print("[A] Agregar contacto | [B] Buscar | [S] Salir")
    op = input("Ingrese una opción: ")
    op.strip().capitalize()
    return op

contactos = {}

def buscar_numero(contactos, nombre_buscado):
    nombre_buscado = input("Ingrese el nombre del usuario: ")
    if nombre_buscado in contactos:
        numero = contactos.items(nombre_buscado)
        return numero
    else:
        print("El contacto no existe.")

while True:
    pedir_opcion()
    if op == "A":
        nombre = input("Ingrese el nombre: ").strip().capitalize()
        telefono = input("Ingrese el número de teléfono: ").strip()
        contactos[nombre] = telefono
    elif op == "B":
        buscar_numero(contactos, nombre_buscado)
    elif op == "S":
        print("Saliendo....")
        break