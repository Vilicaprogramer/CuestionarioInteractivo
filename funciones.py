import json
from random import randint


def bienvenida():
    print("BIENVENIDO AL CUESTIONARIO INTERACTIVO")

def preguntar_nombre():
    return input("Cual es tu nombre? ")

def menu_principal():
    print('''### MENÚ CUESTIONARIO INTERACTIVO ###
1 - Empezar cuestionario
2 - Ranking (opcional)
3 - Salir''')

def empieza_cuestionario():
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    
    num_aleatorio = randint(1,20)

    for pregunta in preguntas["preguntas"]:
        if pregunta["numero"] == num_aleatorio:
            print(pregunta["pregunta"])
            for opcion in pregunta["opciones"]:
                print(opcion)
            print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
            print()


def guardar_ranking():
    pass

def mostrar_ranking():
    pass