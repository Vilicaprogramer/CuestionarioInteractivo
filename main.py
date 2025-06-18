from funciones import *

bienvenida()
puntuacion = 0
opcion = 0
while opcion != 3:
    menu_principal()
    try:
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            nombre = preguntar_nombre()
            ranking_jugador = {}
            ranking_jugador["nombre"] = nombre
            eleccion = 0
            while eleccion != 5:
                menu_cuestionarios()
                try:
                    eleccion = int(input("¿Qué cuestionario quieres?: "))
                    if eleccion == 1:
                        puntuacion += empieza_cuestionario("preguntas_programacion.json")
                    elif eleccion == 2:
                        puntuacion += empieza_cuestionario("preguntas_sql_bases_datos.json")
                    elif eleccion == 3:
                        puntuacion += empieza_cuestionario("preguntas_html_css_js.json")
                    elif eleccion == 4:
                        puntuacion += empieza_cuestionario("preguntas_cultura_general.json")
                except:
                    print("No es una opción válida, intentalo de nuevo")  
            print(f'\nTu puntuación ha sido de {puntuacion} puntos \n') 
            guardar_ranking(nombre, puntuacion)   
        elif opcion == 2:
            print("\n===RANKING===\n")
            mostrar_ranking()
    except:
        print("No es una opción válida, intentalo de nuevo")