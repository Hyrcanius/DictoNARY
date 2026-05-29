productos = {}
op = 0

def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    
    if "" in nombre:
        print("No pueden haber espacios en el nombre")
        return
    
    if nombre in productos:
        print("El producto ya existe.")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio: "))

    productos[nombre] = [stock, precio]

while True:
    try:
        print("----MENU----")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar productos")
        print("4. Producto más caro")
        print("5. Salir")
        op = int(input("Ingrese una opción: "))

        if op == 1:
            agregar_producto(productos)
        elif op == 2:
            #mostrar_productos(productos)#
            print(productos)
        elif op == 3:
            #buscar_producto(productos)#
            print("buscando")
        elif op == 4:
            #producto_mas_caro(productos)#
            print("carozzi")
        elif op == 5:
            print("Gracias por utilizar nuestro software.")
            break
        else:
            print("Ingrese una opción válida.")
    except:
        print("Opción inválida.")
