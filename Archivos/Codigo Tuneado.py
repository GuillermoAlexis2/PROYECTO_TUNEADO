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
