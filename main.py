import funciones as f

f.bienvenida()
nombre = f.preguntar_nombre()
suma_puntos = 0
ranking_jugador = {}
ranking_jugador["nombre"] = nombre

puntuacion = 0
opcion = 0
while opcion != 3:
    f.menu_principal()
    try:
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            eleccion = 0
            while eleccion != 5:
                f.menu_cuestionarios()
                try:
                    eleccion = int(input("¿Qué cuestionario quieres?: "))
                    if eleccion == 1:
                        puntuacion += f.empieza_cuestionario("preguntas_programacion.json")
                    elif eleccion == 2:
                        puntuacion += f.empieza_cuestionario("preguntas_sql_bases_datos.json")
                    elif eleccion == 3:
                        puntuacion += f.empieza_cuestionario("preguntas_html_css_js.json")
                    elif eleccion == 4:
                        puntuacion += f.empieza_cuestionario("preguntas_cultura_general.json")
                except:
                    print("No es una opción válida, intentalo de nuevo")  
            print(f'\nTu puntuación ha sido de {puntuacion} puntos \n') 
            f.guardar_ranking(nombre, puntuacion)   
        elif opcion == 2:
            pass
    except:
        print("No es una opción válida, intentalo de nuevo")