import funcionesSteam as fn

# ===base de datos, copiar y pegar en el main ===
catalogo_steam = [
{"titulo" : "Elden Ring", "precio" : 45499},
{"titulo" : "Cyberpunk 2077", "precio" : 39999},
{"titulo" : "Stardew Valley", "precio" : 7500},
{"titulo" : "Hollow Knight", "precio" : 8300},
{"titulo" : "Sekiro: Shadows Die Twice", "precio" : 47650},
{"titulo" : "Resident Evil 4", "precio" : 27600},
{"titulo" : "Dead by Daylight", "precio" : 11994},
{"titulo" : "Clair Obscur: Expedition 33", "precio" : 39990},
{"titulo" : "Project Zomboid", "precio" : 10500},
{"titulo" : "Backrooms: Escape Together", "precio" : 5750},
{"titulo" : "Lethal Company", "precio" : 5750},
{"titulo" : "Helldivers 2", "precio" : 28000},
{"titulo" : "Red Dead Redemption 2", "precio" : 35948},
{"titulo" : "God of War", "precio" : 35000}
]
carrito_compras = []
biblioteca_juegos = []

while True:

    fn.mostrar_menu()
    op = int(input("Seleccione una opción: "))
    if op == 1:
        fn.mostrar_juegos(catalogo_steam)
    elif op == 2:
        nombre = input("Ingrese el nombre del juego: ").strip().capitalize()
        for juego in catalogo_steam:
            if juego['titulo'].lower() == nombre.lower():
                carrito_compras.append(catalogo_steam[nombre])
                print(carrito_compras)
    elif op == 3:
        print("viendo...")
    elif op == 4:
        print("cargando...")
    elif op == 5:
        print("pagando...")
    elif op == 6:
        print("viendo...")
    elif op == 7:
        print("saliendo...")
        break
    else:
        print("Ingrese una opción inválida.")

