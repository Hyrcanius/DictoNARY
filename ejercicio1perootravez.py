productos = {
 "Mouse": [10, 15000],
 "Teclado": [5, 25000],
 "Monitor": [3, 180000]
}


def agregar_producto(productos):
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacio.")
            return

        if nombre in productos:
            print("No se permite agregar productos repetidos.")
            return

        stock = int(input("Ingrese el stock: "))

        if stock < 0:
            print("Stock debe ser mayor o igual a 0.")
            return
        
        precio = int(input("Ingrese el precio: "))

        if precio <= 0:
            print("El precio debe ser mayor que 0.")
            return
    except:
        print("Ingreso inválido.")
        return
    
    productos[nombre] = [stock, precio]

def mostrar_productos(productos):
    if productos == {}:
        print("No existen productos registrados.")
        return
    else:
        for nombre, (stock, precio) in productos.items():
            print(f"{nombre} {stock} {precio}")

def buscar_producto(productos):
    try:
        nombre = input("Ingrese el nombre del producto a buscar: ").strip()

        if nombre in productos:
            stock, precio = productos[nombre]
            print(f"El producto '{nombre}' está disponible, tiene un stock de: {stock} unidades y su precio es: ${precio}")
            return
        else:
            print("Producto no disponible.")
            return
    except:
        print("Ingreso inválido.")
        return
    
def producto_mas_caro(productos):
    if productos == {}:
        print("No hay productos registrados.")
        return
    else:
        mas_caro = -1
        nombre_mas_caro = ""
        for nombre, (stock, precio) in productos.items():
            if precio > mas_caro:
                mas_caro = precio
                nombre_mas_caro = nombre
        
        print(f"El producto: '{nombre_mas_caro}' con el precio: ${mas_caro} es el más caro.")



while True:
    try:
        print("---MENU---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Producto más caro")
        print("5. Salir")

        op = int(input("Ingrese una opción: "))

        if op == 1:
            agregar_producto(productos)
        elif op == 2:
            mostrar_productos(productos)
        elif op == 3:
            buscar_producto(productos)
        elif op == 4:
            producto_mas_caro(productos)
        elif op == 5:
            print("Adios...")
            break
        else:
            print("Opción inválida.")
    except:
        print("Opción inválida.")