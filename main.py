import funciones as f

nombre = f.preguntar_nombre()
suma_puntos = 0
ranking_jugador = {}
ranking_jugador["nombre"] = nombre

opcion = 0
while opcion != 3:
    f.menu_principal()
    try:
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            f.empieza_cuestionario()
        elif opcion == 2:
            f.mostrar_ranking()
        else:
            print("No es una opción válida, intentalo de nuevo")
    except:
        print("No es una opción válida, intentalo de nuevo")