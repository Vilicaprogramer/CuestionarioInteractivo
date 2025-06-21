from funciones import *

bienvenida()
puntuacion = 0
num_preguntas = 0
aciertos = 0
fallos = 0
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
                        datos = empieza_cuestionario("preguntas_programacion.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 2:
                        datos = empieza_cuestionario("preguntas_sql_bases_datos.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 3:
                        datos = empieza_cuestionario("preguntas_html_css_js.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 4:
                        datos = empieza_cuestionario("preguntas_cultura_general.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                except:
                    print("No es una opción válida, intentalo de nuevo") 
            
            porcentaje = round((aciertos/num_preguntas)*100,2)
            print(f'''\nTu puntuación ha sido de {puntuacion} puntos.
    Número total de pregunatas realizadas {num_preguntas}.
    Número de aciertos: {aciertos}.
    Número de fallos: {fallos}.
    Porcentaje total de aciertos: {porcentaje}%.''')
            valoracion_final(porcentaje) 
            guardar_ranking(nombre, puntuacion)   
        elif opcion == 2:
            print("\n===RANKING===\n")
            mostrar_ranking()
    except:
        print("No es una opción válida, intentalo de nuevo")