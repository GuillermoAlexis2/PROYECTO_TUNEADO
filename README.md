# PROYECTO_TUNEADO
FACULTAD DE INGIENERIA CIVIL
ING TOPOGRAFO GEOMATICO
Grado y Grupo 3-B
Programa informático para obtener áreas , distancias y el desnivel con la mínima precisión de las operaciones dentro de la topografía .
Autor:Avalos Lucas Alexis Guillermo
Asesor:Sebastián Gonzales Zepeda

RESUMEN 
Una descripción breve sobre lo que realizaremos es una calculadora informática esto mediante la programación , buscamos una representación del terreno tanto como es su distancia y área , esto dado que importaremos un archivo CSV de un levantamiento topográfico que realizamos. 
INTRODUCION
En este programa que es sobre una calculadora topográfica , lo que queremos obtener  la medición de distancias , áreas y el desnivel que faciliten el trabajo y la precisión de las operaciones dentro de la topografía mediante un programa informático , esto el cual es a través de un programa , algunos beneficios es que nos vamos a obtener es que será muy preciso en los resultados , el mínimo error que se obtendrá lo queremos dejar en 0

En este trabajo a realizar nos daremos cuenta si un programa nos puede llegar a facilitar los cálculos y minimizando el mínimo error , La medición precisa de distancias e áreas es fundamental en la topografía, al igual es importante saber el desnivel que hay , esto para llevar a cabo operaciones y proyectos con eficiencia y exactitud. Las calculadoras topográficas son diseñadas para realizar cálculos relacionados con la topografía, como la distancia entre puntos, el cálculo de áreas y volúmenes, la elevación de puntos, entre otras.

DESARROLLO 
Mediante un archivo CSV queremos representar en un grafico, un programa informático destinado a la medición de distancias e áreas como el saber el desnivel que hay  en el ámbito de la topografía representa una innovación crucial para optimizar el trabajo y aumentar la precisión en las operaciones topográficas. Este tipo de herramienta se vuelve esencial en proyectos de cartografía, urbanismo y diseño de terrenos, donde la exactitud de las mediciones es fundamental.
Lo que buscamos en este programa informático es que el programa nos podría ayudar a representar como el procesamiento de una representación grafico o imágenes y claro que también la integración de datos GPS o documentos CSV para representar un levantamiento topográfico
Tenemos en cuenta que el programa nos ayude con cualquier tipo de cálculos tanto como ya mencionados , por ejemplo que lea un archivo CSV y nos de lo que es su desnivel , distancias y lo que es el área , al igual que buscamos también una representación sobre lo que es el terreno 

MANEJO DE DATOS	
El manejo de datos en un proyecto de calculadora informática implica gestionar la entrada del usuario, procesarla adecuadamente y mostrar los resultados.
Entrada de Datos:
 Diseña una interfaz de usuario que permita al usuario ingresar datos de manera clara y eficiente.
Implementa mecanismos de validación para asegurar que la entrada del usuario sea válida y cumpla con los requisitos de la calculadora.
Operaciones Matemáticas:
 Desarrolla la lógica para realizar las operaciones matemáticas básicas (suma, resta, multiplicación, división) y otras funciones más avanzadas si es necesario (potencia, raíz cuadrada, trigonometría, etc.)
Gestión de Resultados: 
Diseña un mecanismo para mostrar los resultados de las operaciones de manera clara y comprensible para el usuario.
Asegúrate de manejar casos especiales, como divisiones por cero o resultados demasiado grandes.
Pruebas Unitarias:
Implementa pruebas unitarias para verificar que el manejo de datos funciona correctamente en diferentes escenarios y condiciones.
Seguridad:
Considera la seguridad de los datos, especialmente si la calculadora maneja información sensible. Implementa medidas para proteger la privacidad y la integridad de los datos.
Documentación:
Documenta el manejo de datos en tu código para que sea comprensible para otros desarrolladores y para ti mismo en el futuro.


RESULTADOS
Como resultado del código obtuvimos lo que fue el área, distancia y podemos observar que el desnivel del terreno también lo representa , estos puntos que nos representa fue un levantamiento de los amiales , esto que nos presento el código no tenia en mente que nos lo representaría de esta manera , de tal manera que aquí vemos lo que fue cada punto levantado y los cadenamientos que íbamos tomando cada 20 mt


CONCLUSIÓN 
En lo personal sobre este proyecto de la realización de una calculadora informática nos sirve para obtener cálculos mucho mas rápido , Durante el proceso, hemos enfrentado desafíos que nos han llevado a mejorar nuestras habilidades de resolución de problemas y a comprender la importancia de la modularidad y la eficiencia en el código.
En este  proyecto de la calculadora informática ha sido un ejercicio fundamental que ha permitido aplicar y consolidar conocimientos en el desarrollo de software
En este trabajo lo que me sirvió fue que me puse a investigar cosas que no entendía y lo lleve a cabo a desarrollar al final el resultado fue lo esperado.

CODIGO MEJORADO
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import math
import matplotlib.pyplot as plt
from matplotlib import cm

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calcular_area(coordenadas):
    n = len(coordenadas)
    area = 0
    for i in range(n):
        x1, y1, _ = coordenadas[i]
        x2, y2, _ = coordenadas[(i + 1) % n]
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2

def calcular_desnivel(coordenadas):
    desnivel_total = 0
    desniveles = []
    for i in range(len(coordenadas)):
        _, _, z1 = coordenadas[i]
        _, _, z2 = coordenadas[(i + 1) % len(coordenadas)]
        desnivel = abs(z2 - z1)
        desniveles.append(desnivel)
        desnivel_total += desnivel
    return desnivel_total, desniveles

def leer_archivo_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)
    coordenadas = [(x, y, z) for x, y, z in zip(df['COORDENADA X'], df['COORDENADA Y'], df['Z'])]
    return coordenadas

def plot_terreno(coordenadas):
    x, y, _ = zip(*coordenadas)
    desnivel_total, desniveles = calcular_desnivel(coordenadas)

    # Normaliza los desniveles para asignar colores
    norm = plt.Normalize(0, max(desniveles))
    cmap = cm.viridis

    fig, ax = plt.subplots()
    scatter = ax.scatter(x + (x[0],), y + (y[0],), c=desniveles + [desniveles[0]], cmap=cmap, marker='o', linestyle='-')
    plt.colorbar(scatter, label='Desnivel')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title(f"Representación Gráfica del Terreno (Desnivel total: {desnivel_total:.2f} unidades)")
    plt.show()

def calcular_resultado():
    global resultado  # Añade esta línea para indicar que se está utilizando la variable global

    if not coordenadas:
        resultado.set("No se han cargado coordenadas desde el archivo CSV.")
        return

    distancia_total = 0
    desnivel_total, _ = calcular_desnivel(coordenadas)
    for i in range(len(coordenadas)):
        x1, y1, z1 = coordenadas[i]
        x2, y2, z2 = coordenadas[(i + 1) % len(coordenadas)]
        distancia = calcular_distancia(x1, y1, x2, y2)
        distancia_total += distancia

    area = calcular_area(coordenadas)
    resultado_text = f"Distancia total: {distancia_total:.2f} unidades\nÁrea del polígono: {area:.2f} unidades cuadradas\nDesnivel total: {desnivel_total:.2f} unidades"
    resultado.set(resultado_text)

    with open("resultado.txt", "w") as file:
        file.write(f"Distancia total: {distancia_total:.2f} unidades\nÁrea del polígono: {area:.2f} unidades cuadradas\nDesnivel total: {desnivel_total:.2f} unidades")

    with open(__file__, "a") as code_file:
        code_file.write("\n# Coordenadas leídas desde el archivo CSV:\n")
        for coord in coordenadas:
            code_file.write(f"# {coord}\n")

    plot_terreno(coordenadas)

ventana = tk.Tk()
ventana.title("Calculadora Topográfica")

resultado = tk.StringVar()
coordenadas = leer_archivo_csv('C:/Users\Colibecas\Documents\CALCULADORA TOPOGRAFICA\PUNTOS_AMIALES.csv')

frame_entrada = tk.Frame(ventana)
frame_resultado = tk.Frame(ventana)

frame_entrada.pack(padx=10, pady=10)
frame_resultado.pack(padx=10, pady=10)

label_resultado = tk.Label(frame_resultado, textvariable=resultado, wraplength=400)
label_resultado.pack()

calcular_resultado()  # Llama a la función para que se ejecute al inicio

ventana.mainloop()
