from funciones import *

# Arranco mostrando un mensaje de bienvenida
bienvenida()

# Variables para acumular resultados del jugador
puntuacion = 0
num_preguntas = 0
aciertos = 0
fallos = 0

# Variable para controlar el menú principal
opcion = 0

# Bucle del menú principal: se repite hasta que el usuario elige 3 (Salir)
while opcion != 3:
    menu_principal()
    try:
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            # Opción 1: empezar cuestionario
            nombre = preguntar_nombre()

            # Aquí guardo temporalmente el nombre del jugador
            ranking_jugador = {}
            ranking_jugador["nombre"] = nombre

            # Variable para controlar el submenú de cuestionarios
            eleccion = 0
            while eleccion != 5:
                menu_cuestionarios()
                try:
                    eleccion = int(input("¿Qué cuestionario quieres?: "))
                    if eleccion == 1:
                        # Tema: Programación
                        datos = empieza_cuestionario("preguntas_programacion.json")
                        # datos = (puntuacion, num_preguntas, aciertos, fallos)
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 2:
                        # Tema: SQL y BBDD
                        datos = empieza_cuestionario("preguntas_sql_bases_datos.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 3:
                        # Tema: HTML, CSS, JavaScript
                        datos = empieza_cuestionario("preguntas_html_css_js.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    elif eleccion == 4:
                        # Tema: Cultura general
                        datos = empieza_cuestionario("preguntas_cultura_general.json")
                        puntuacion += datos[0]
                        num_preguntas += datos[1]
                        aciertos += datos[2]
                        fallos += datos[3]
                    # Si elige 5 se sale del submenú
                except:
                    # Si escribe algo que no es un número válido para el submenú
                    print("No es una opción válida, intentalo de nuevo") 
            
            # Cuando sale del submenú, muestro el resumen del jugador
            porcentaje = round((aciertos/num_preguntas)*100,2)

            print(f'''\nTu puntuación ha sido de {puntuacion} puntos.
Número total de preguntas realizadas {num_preguntas}.
Número de aciertos: {aciertos}.
Número de fallos: {fallos}.
Porcentaje total de aciertos: {porcentaje}%.''')

            # Muestro mensaje final según el porcentaje
            valoracion_final(porcentaje) 

            # Guardo el resultado en el ranking (JSON)
            guardar_ranking(nombre, puntuacion)   

        elif opcion == 2:
            # Opción 2: mostrar ranking
            print("\n===RANKING===\n")
            mostrar_ranking()

        # Si elige 3, el while terminará y se sale del programa

    except:
        # Si mete una opción no válida en el menú principal
        print("No es una opción válida, intentalo de nuevo")
