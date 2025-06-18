import json
from random import randint


def bienvenida():
    print("BIENVENIDO AL CUESTIONARIO INTERACTIVO")

def preguntar_nombre():
    return input("Cual es tu nombre? ")

def menu_principal():
    print ('''### MENÚ CUESTIONARIO INTERACTIVO ###
1 - Empezar cuestionario
2 - Ranking (opcional)
3 - Salir\n''')
    
def menu_cuestionarios():
    print('''### ELIGE UNA TEMÁTICA ###
1 - Programación
2 - SQL y BBDD
3 - HTML, CSS, JavaScript
4 - Cultura general
5 - Salir\n''')


def continuar_preguntando():
    while True:
        try:
            continuar = int(input('''¿QUIERES CONTINUAR?
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
    cambio_de_tema = True
    while cambio_de_tema:
        try:
            preguntas_hechas = []
            num_aleatorio = randint(1,20)
            if num_aleatorio not in preguntas_hechas:   
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
                            puntuacion += 10
                            continuar = int(input("1 para continuar 2 para salir: \t"))
                            print()
                            if continuar == True:
                                continue
                            else:
                                cambio_de_tema = False
                        else:
                            print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
                            print()
                else:
                    continue
        except:
            print("Opción incorrecta, intentalo de nuevo: ")
       
    return puntuacion


def guardar_ranking(nombre, puntuacion):
    with open("ranking.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
    nueva_puntuacion = {"nombre": nombre, "puntuacion": puntuacion}

    datos["ranking"].append(nueva_puntuacion)

    with open("ranking.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)


def mostrar_ranking():
    pass