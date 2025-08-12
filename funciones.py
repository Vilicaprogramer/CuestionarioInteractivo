import json
from random import randint

# ------------------------------------------------------------
# Pequeño cuestionario en consola con menú, preguntas por temas
# y un ranking guardado en JSON.
# ------------------------------------------------------------

def bienvenida():
    # Mensaje de bienvenida al arrancar el programa
    print("BIENVENIDO AL CUESTIONARIO INTERACTIVO")

def preguntar_nombre():
    # Pido el nombre al usuario y lo devuelvo
    return input("¿Cual es tu nombre? ")

def menu_principal():
    # Menú principal con opciones básicas
    print ('''\n### MENÚ CUESTIONARIO INTERACTIVO ###
1 - Empezar cuestionario
2 - Ranking
3 - Salir\n''')
    
def menu_cuestionarios():
    # Menú para elegir la temática del cuestionario
    print('''\n### ELIGE UNA TEMÁTICA ###
1 - Programación
2 - SQL y BBDD
3 - HTML, CSS, JavaScript
4 - Cultura general
5 - Salir\n''')

def continuar_preguntando():
    # Después de cada pregunta, pregunto si quiere seguir o salir
    while True:
        try:
            continuar = int(input('''\n¿QUIERES CONTINUAR?
                                1 - Para continuar    2 - Para salir:\t   '''))
            if continuar == 1:
                return True   # sigo preguntando
            else:
                return False  # salgo del cuestionario
        except:
            # Si mete algo que no es número, aviso y vuelvo a pedirlo
            print("Opción incorrecta, intentalo de nuevo: ")
    
def empieza_cuestionario(cuestionario):
    # Abro el fichero JSON con las preguntas del tema elegido
    with open(cuestionario, "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    
    # Variables para las estadísticas del usuario
    puntuacion = 0
    num_preguntas = 0
    aciertos = 0
    fallos = 0

    # Esta variable controla si seguimos en el bucle de preguntas
    cambio_de_tema = True
    # Lista de preguntas ya hechas
    preguntas_hechas = []

    while cambio_de_tema:
        try:
            # Elijo un número aleatorio de 1 a 20 (según estructura del JSON)
            num_aleatorio = randint(1,20)

            # Si esa pregunta no se ha hecho, la marco y la lanzo
            if num_aleatorio not in preguntas_hechas: 
                preguntas_hechas.append(num_aleatorio)  
                for pregunta in preguntas["preguntas"]:
                    if pregunta["numero"] == num_aleatorio:
                        # Muestro enunciado
                        print(pregunta["pregunta"])
                        # Muestro opciones (tipo A), B), C)...)
                        for opcion in pregunta["opciones"]:
                            print(opcion)
                        
                        print()
                        # Pido respuesta y la paso a mayúsculas para comparar tipo 'A'
                        repuesta = input("¿Cual es tu respuesta?: ").upper()
                        print()

                        # Si acierta, sumo puntos y aciertos
                        if repuesta == pregunta['respuesta_correcta']:
                            print('¡¡¡CORRECTO!!!')
                            num_preguntas += 1
                            aciertos += 1
                            puntuacion += 10
                            # Pregunto si quiere seguir
                            cambio_de_tema = continuar_preguntando()
                        else:
                            # Si falla, incremento fallos y muestro la correcta
                            num_preguntas += 1
                            fallos += 1
                            print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
                            print()
                            # Pregunto si quiere seguir
                            cambio_de_tema = continuar_preguntando()
            else:
                # Si ya se hizo la pregunta (no debería pasar aquí), salto
                continue
        except:
            # Si algo sale mal, aviso y sigo
            print("Opción incorrecta, intentalo de nuevo: ")
       
    # Devuelvo las estadísticas para que las use el programa principal
    return puntuacion, num_preguntas, aciertos, fallos

def guardar_ranking(nombre, puntuacion):
    # Abro el ranking existente
    with open("ranking.json", "r", encoding="utf-8") as f:
        datos = json.load(f)

    # Preparo la nueva entrada del ranking
    nueva_puntuacion = {"nombre": nombre, "puntuacion": puntuacion}
    
    # Si el nombre ya existe, lo elimino para dejar solo la última puntuación
    for ranking in range(len(datos['ranking'])):
        if nombre in datos['ranking'][ranking]['nombre']:
            del datos['ranking'][ranking]
            break

    # Añado el nuevo registro al ranking
    datos["ranking"].append(nueva_puntuacion)

    # Guardo el ranking formateado
    with open("ranking.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def mostrar_ranking():
    # Abro el ranking y lo convierto a una lista de tuplas (nombre, puntos)
    with open("ranking.json", "r", encoding="utf-8") as archivo:
        ranking = json.load(archivo)

    ranking_lista = []
    for persona in ranking['ranking']:
        ranking_lista.append((persona['nombre'], persona['puntuacion']))

    # Ordeno de mayor a menor puntuación
    ranking_lista = sorted(ranking_lista, key= lambda item: item[1], reverse=True)

    # Muestro el ranking con una pequeña alineación
    for n, p in ranking_lista:
        print(f'{n:<10} --> {p:>5} puntos')
    print()

def valoracion_final(valoracion):
    # Mensaje final según la puntuación total del usuario
    if valoracion < 50:
        print('Tienes que estudiar más.')
    elif valoracion < 70:
        print('¡Buen trabajo! Un poco más de estudio y ya lo tienes')
    elif valoracion < 100:
        print('¡Muy bien! Ya lo tienes!')
    else:
        print('¡Abusón! Tendrémos que buscar preguntas más dificiles para ti.')
