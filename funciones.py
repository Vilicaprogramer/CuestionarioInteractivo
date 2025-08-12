import json
from random import randint


def bienvenida():
    print("BIENVENIDO AL CUESTIONARIO INTERACTIVO")

def preguntar_nombre():
    return input("¿Cual es tu nombre? ")

def menu_principal():
    print ('''\n### MENÚ CUESTIONARIO INTERACTIVO ###
1 - Empezar cuestionario
2 - Ranking
3 - Salir\n''')
    
def menu_cuestionarios():
    print('''\n### ELIGE UNA TEMÁTICA ###
1 - Programación
2 - SQL y BBDD
3 - HTML, CSS, JavaScript
4 - Cultura general
5 - Salir\n''')


def continuar_preguntando():
    while True:
        try:
            continuar = int(input('''\n¿QUIERES CONTINUAR?
                                1 - Para continuar    2 - Para salir:\t   '''))
            if continuar == 1:
                return True
            else:
                return False
        except:
            print("Opción incorrecta, intentalo de nuevo: ")
    
        
def empieza_cuestionario(cuestionario):
    with open(cuestionario, "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    
    puntuacion = 0
    num_preguntas = 0
    aciertos = 0
    fallos = 0
    cambio_de_tema = True
    while cambio_de_tema:
        try:
            preguntas_hechas = []
            num_aleatorio = randint(1,20)
            if num_aleatorio not in preguntas_hechas: 
                preguntas_hechas.append(num_aleatorio)  
                for pregunta in preguntas["preguntas"]:
                    if pregunta["numero"] == num_aleatorio:
                        print(pregunta["pregunta"])
                        for opcion in pregunta["opciones"]:
                            print(opcion)
                        
                        print()
                        repuesta = input("¿Cual es tu respuesta?: ").upper()
                        print()

                        if repuesta == pregunta['respuesta_correcta']:
                            print('¡¡¡CORRECTO!!!')
                            num_preguntas += 1
                            aciertos += 1
                            puntuacion += 10
                            cambio_de_tema = continuar_preguntando()
                        else:
                            num_preguntas += 1
                            fallos += 1
                            print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
                            print()
                            cambio_de_tema = continuar_preguntando()
            else:
                continue
        except:
            print("Opción incorrecta, intentalo de nuevo: ")
       
    return puntuacion, num_preguntas, aciertos, fallos


def guardar_ranking(nombre, puntuacion):
    with open("ranking.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    nueva_puntuacion = {"nombre": nombre, "puntuacion": puntuacion}
    
    for ranking in range(len(datos['ranking'])):
        if nombre in datos['ranking'][ranking]['nombre']:
            del datos['ranking'][ranking]
            break

    datos["ranking"].append(nueva_puntuacion)

    with open("ranking.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def mostrar_ranking():
    with open("ranking.json", "r", encoding="utf-8") as archivo:
        ranking = json.load(archivo)

    ranking_lista = []
    for persona in ranking['ranking']:
        ranking_lista.append((persona['nombre'], persona['puntuacion']))

    ranking_lista = sorted(ranking_lista, key= lambda item: item[1], reverse=True)

    for n, p in ranking_lista:
        print(f'{n:<10} --> {p:>5} puntos')
    print()

def valoracion_final(valoracion):
    if valoracion < 50:
        print('Tienes que estudiar más.')
    elif valoracion < 70:
        print('¡Buen trabajo! Un poco más de estudio y ya lo tienes')
    elif valoracion < 100:
        print('¡Muy bien! Ya lo tienes!')
    else:
        print('¡Abusón! Tendrémos que buscar preguntas más dificiles para ti.')