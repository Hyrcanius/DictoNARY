def mostrar_menu():
    print("-Op 1: Ver Catálogo")
    print("-Op 2: Agregar juego al carrito")
    print("-Op 3: Ver mi carrito")
    print("-Op 4: Cargar fondos a la cartera")
    print("-Op 5: Pagar carrito: ")
    print("-Op 6: Ver mi biblioteca")
    print("-Op 7: Salir")

def mostrar_juegos(lista_generica):
    
    if lista_generica == []:
        print("No hay elementos en la lista.")
        return
    
    for i in range(len(lista_generica)):
        actual = lista_generica[i]
        for titulo, precio in actual.items():
            print(f"-{titulo}, ${precio}")

def calcular_total(carrito_compras):
    suma = 0
    for i in range(len(carrito_compras)):
        posicion = carrito_compras[i]
        for titulo, precio in posicion.items():
            valor = precio
            suma = suma + valor
    
    return suma