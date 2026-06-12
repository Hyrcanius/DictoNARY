alumnos = {
 "Ana": [5.5, 6.0, 4.8],
 "Luis": [3.9, 4.1, 5.0],
 "Pedro": [6.5, 6.8, 7.0]
}

def agregar_alumno(alumnos):
    nombre = input("Ingrese el nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    if nombre in alumnos:
        print("Alumno ya se encuentra inscrito.")
        return
    
    cant_notas = int(input("Ingrese la cantidad de notas: "))
    
    if cant_notas <= 0:
        print("Cantidad de notas debe ser mayor que 0.")
        return

    notas = []

    for i in range(cant_notas):
        while True:
            try:
                nota = float(input("Ingrese la nota: "))
                if (nota < 1.0) or (nota > 7.0):
                    print("Error, nota debe estar entre 1.0 y 7.0.")
                else:
                    notas.append(nota)
                    break
            except:
                print("Nota inválida.")
    
    alumnos[nombre] = notas

def mostrar_alumnos(alumnos):
    if alumnos == {}:
        print("No hay alumnos registrados.")
        return

    for nombre, notas in alumnos.items():
        print(nombre, *notas)

def ver_promedios(alumnos):
    if alumnos == {}:
        print("No hay alumnos registrados.")
        return

    for nombre, notas in alumnos.items():
        promedio = 0
        suma_nota = 0
        cant_notas = len(notas)
        for i in range(cant_notas):
            nota = notas[i]
            suma_nota += nota
        promedio =  round(suma_nota/cant_notas, ndigits= 1)
        print(f"{nombre}, promedio: {promedio}")

def mejor_alumno(alumnos):
    if alumnos == {}:
        print("No hay alumnos registrados.")
        return
    
    mejor_promedio = 0
    nombre_mejor = ""
    for nombre, notas in alumnos.items():
        promedio = 0
        suma_nota = 0
        cant_notas = len(notas)
        for i in range(cant_notas):
            nota = notas[i]
            suma_nota += nota
        promedio =  round(suma_nota/cant_notas, ndigits= 1)
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = nombre
    
    print(f"{mejor_alumno} tiene el mejor promedio con: {mejor_promedio}")

def cantidad_aprobados(alumnos):
    if alumnos == {}:
        print("No hay alumnos registrados.")
        return
    
    aprobados = 0
    for nombre, notas in alumnos.items():
        promedio = 0
        suma_nota = 0
        cant_notas = len(notas)
        for i in range(cant_notas):
            nota = notas[i]
            suma_nota += nota
        promedio =  round(suma_nota/cant_notas, ndigits= 1)
        if promedio > 4:
            aprobados += 1
    
    print(f"La cantidad de aprobados es {aprobados}")



while True:
    try:
        print("1. Agregar alumno")
        print("2. Mostrar alumnos")
        print("3. Ver promedios")
        print("4. Mejor alumno")
        print("5. Cantidad de aprobados")
        print("6. Salir")

        op = int(input("Ingrese una opción: "))

        if op == 1:
            agregar_alumno(alumnos)
        elif op == 2:
            mostrar_alumnos(alumnos)
        elif op == 3:
            ver_promedios(alumnos)
        elif op == 4:
            mejor_alumno(alumnos)
        elif op == 5:
            cantidad_aprobados(alumnos)
        elif op == 6:
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
    except:
        print("Opción inválida.")