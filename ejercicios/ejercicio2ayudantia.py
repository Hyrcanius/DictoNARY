op = ""
nombre_buscado = ""

def pedir_opcion():
    print("[A] Agregar contacto | [B] Buscar | [S] Salir")
    op = input("Ingrese una opción: ").strip().capitalize()
    return op

contactos = {}

def buscar_numero(contactos, nombre_buscado):
    nombre_buscado = input("Ingrese el nombre del usuario: ").strip().capitalize()
    if nombre_buscado in contactos:
        numero = contactos[nombre_buscado]
        return numero
    else:
        print("El contacto no existe.")

while True:
    op = pedir_opcion()
    if op == "A":
        nombre = input("Ingrese el nombre: ").strip().capitalize()
        telefono = input("Ingrese el número de teléfono: ").strip()
        contactos[nombre] = telefono
    elif op == "B":
        resultado = buscar_numero(contactos, nombre_buscado)
        print(resultado)
    elif op == "S":
        print("Saliendo....")
        break