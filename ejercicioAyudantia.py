

def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver tareas ordenadas")
    print("4. Salir")

lista_tareas = []

def imprimir_tareas(lista_tareas):

    if lista_tareas == []:
        print("No hay tareas pendientes.")
    else:
        lista_tareas.sort()
        for tarea in lista_tareas:
            print(f"- {tarea}")

def agregar_tarea(lista_tareas):
    nueva_tarea = input("Ingrese la nueva tarea: ")
    lista_tareas.append(nueva_tarea.strip().capitalize())
    print(lista_tareas)

def eliminar_tarea(lista_tareas):
    quitar_tarea = input("Ingrese la tarea que quiere eliminar: ").strip().capitalize()
    if quitar_tarea in lista_tareas:
        lista_tareas.remove(quitar_tarea)
    

while True:
    try:
        mostrar_menu()
        op = int(input("Seleccioné una opción: "))
        if op == 1:
            agregar_tarea(lista_tareas)
        elif op == 2:
            eliminar_tarea(lista_tareas)
        elif op == 3:
            imprimir_tareas(lista_tareas)
        elif op == 4:
            print("Saliendo...")
            break
    except:
        print("Ingrese una opción válida.")