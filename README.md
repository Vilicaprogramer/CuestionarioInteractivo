# Proyecto 1 · Generador de Cuestionarios Interactivo

> Pequeña app de **consola en Python** para hacer cuestionarios tipo test. El usuario responde, el programa corrige y al final muestra **puntuación, aciertos, fallos y valoración**. Además, guarda un **ranking** sencillo en un `.json`.

## 🎯 Objetivo

Construir un cuestionario por consola con menú, preguntas por temas, corrección automática y resumen final. Ideal para practicar **funciones, bucles, estructuras de datos** y **ficheros JSON**.

## ✨ Qué hace

* Menú principal que se repite hasta salir:

  ```
  1 - Empezar cuestionario
  2 - Ranking
  3 - Salir
  ```
* Preguntas **una a una**, con **4 opciones** y **1 sola correcta** (A, B, C o D).
* Muestra si aciertas o fallas al momento.
* Resumen final: total de preguntas, aciertos, fallos, **% de acierto** y **valoración**.
* **Varios temas**: Programación, SQL/BBDD, HTML-CSS-JS y Cultura general.
* **Ranking** guardado en `ranking.json` (nombre + puntuación).

## 🧩 Contenidos del módulo que aplico

* Tipos de datos y estructuras (listas, diccionarios).
* Control de flujo (`if/elif/else`), bucles (`for/while`).
* **Funciones** con parámetros y retorno.
* Entrada/salida por consola.
* Lectura y escritura en **JSON**.

## 📦 Requisitos

* **Python 3.10+** (cualquier 3.x reciente vale).
* Sin dependencias externas (solo `json` y `random` de la librería estándar).

## 🚀 Cómo ejecutar

```bash
# Clona el repo
git clone https://github.com/USUARIO/REPO.git
cd REPO

# Ejecuta el programa
python main.py
```

## 🗂️ Estructura del proyecto

```
.
├── main.py                 # punto de entrada con el menú
├── funciones.py            # lógica del cuestionario, ranking y valoración
├── preguntas_programacion.json
├── preguntas_sql_bases_datos.json
├── preguntas_html_css_js.json
├── preguntas_cultura_general.json
└── ranking.json
```

## 📝 Formato de los ficheros

### Preguntas (`*.json`)

Cada fichero de preguntas sigue esta estructura (ejemplo):

```json
{
  "preguntas": [
    {
      "numero": 1,
      "pregunta": "¿Cuál es la capital de Francia?",
      "opciones": ["A. Madrid", "B. Roma", "C. París", "D. Berlín"],
      "respuesta_correcta": "C"
    }
  ]
}
```

### Ranking (`ranking.json`)

Inicialmente puede estar vacío:

```json
{ "ranking": [] }
```

Y se va guardando así:

```json
{
  "ranking": [
    { "nombre": "Vicente", "puntuacion": 70 },
    { "nombre": "Ana", "puntuacion": 90 }
  ]
}
```

## ▶️ Flujo de uso

1. Entro en **“Empezar cuestionario”** y elijo temática.
2. Respondo preguntas (A/B/C/D).
3. Tras cada respuesta puedo **continuar o salir**.
4. Al terminar veo mi **resumen** y se guarda mi **puntuación** en el ranking.
5. Puedo ir a **“Ranking”** para ver la clasificación ordenada.

## 👤 Autor

**Vicente Limones**
[LinkedIn](http://www.linkedin.com/in/vicente-limones-cantero-3a167328a) • [vilicaprogramer@gmail.com](mailto:vilicaprogramer@gmail.com)

---

> **Tip:** Si quieres probarlo con tus propias preguntas, copia uno de los JSON, cambia el nombre y los campos, y apúntalo en `main.py` para cargarlo desde el menú.
