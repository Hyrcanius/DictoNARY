def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")
    print("====================================")

def op_menu():
    while True:
        try:
            op = int(input("-> "))
            return op
        except:
            print("Opción inválida.")

vehiculos = [{"modelo": "Toyota Corolla", "anio": 1996, "precio": 1690000, "disponibilidad": False}, 
{"modelo": "Chevrolet Silverado", "anio": 2021, "precio": 4500000, "disponibilidad": False}, 
{"modelo": "Chery Tiggo", "anio": 2020, "precio": 5600000, "disponibilidad": False}, 
{"modelo": "Suzuki Baleno", "anio": 2022, "precio": 6900000, "disponibilidad": False}]

def agregar_vehiculo(vehiculos):
    modelo = input("Modelo: ")
    modelo_val = val_modelo(modelo)
    if modelo_val == False:
        print("Ingreso inválido.")
        return

    anio = int(input("Año: "))
    anio_val = val_anio(anio)
    if anio_val == False:
        print("Ingreso inválido.")
        return

    precio = int(input("Precio: "))
    precio_val = val_precio(precio)
    if precio_val == False:
        print("Ingreso inválido.")
        return
    
    vehiculos.append({"modelo":modelo,"anio":anio,"precio":precio,"disponibilidad":False})

def buscar_vehiculo(vehiculos, modelo):
    for i in range(len(vehiculos)):
        if vehiculos[i]["modelo"] == modelo:
            return i
    
    return -1

def act_disp(vehiculos):
    for i in range(len(vehiculos)):
        year = vehiculos[i]["anio"]
        if year >= 2020:
            vehiculos[i]["disponibilidad"] = True
    
    print(vehiculos)

def val_modelo(modelo):
    if modelo == "":
        return False
    
    cont = 0
    for i in range(len(modelo)):
        pos = modelo[i]
        if pos.isalpha():
            cont = cont + 1
    
    if cont == 0:
        return False
    
    return True

def val_anio(anio):
    if anio <= 1900:
        return False
    
    return True

def val_precio(precio):
    if precio % 1 != 0:
        return False

    if precio < 0:
        return False
    
    return True

while True:
    mostrar_menu()
    op = op_menu()

    if op == 1:
        agregar_vehiculo(vehiculos)
    elif op == 2:
        modelo = input("Ingrese el modelo: ")
        resultado = buscar_vehiculo(vehiculos, modelo)
        if resultado == -1:
            print("Modelo no encontrado.")
        else:
            vehiculo = vehiculos[resultado]
            print(f"""Modelo: {vehiculo["modelo"]} | Año: {vehiculo["anio"]} | Valor: {vehiculo["precio"]}""")
    elif op == 3:
        modelo = input("Ingrese el modelo: ")
        resultado = buscar_vehiculo(vehiculos, modelo)
        if resultado == -1:
            print(f"El vehiculo '{modelo}' no se encuentra registrado.")
        else:
            del vehiculos[resultado]
            print(f"Vehículo '{modelo}' eliminado.")
    elif op == 4:
        act_disp(vehiculos)
        print("Disponibilidad actualizada.")
    elif op == 5:
        act_disp(vehiculos)
        print("=== LISTA DE VEHÍCULOS ===")
        print("")
        for i in range(len(vehiculos)):
            vehiculo = vehiculos[i]
            print(f"Modelo: {vehiculo["modelo"]}")
            print(f"Año: {vehiculo["anio"]}")
            print(f"Precio: {vehiculo["precio"]}")
            if vehiculo["disponibilidad"] == True:
                print(f"Estado: DISPONIBLE")
            else:
                print(f"Estado: NO DISPONIBLE")
            print("*" * 40)
    elif op == 6:
        break
