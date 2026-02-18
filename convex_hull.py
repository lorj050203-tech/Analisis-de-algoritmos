
import csv #libreria para leer archivos cvs
from typing import List, Tuple
import matplotlib.pyplot as plt #libreria para graficar
import tkinter as tk #libreria para GUI
from tkinter import filedialog #libreria para abrir el explorador de archivos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #fuiona matplot con tkinder

Point = Tuple[float, float] #se uiliza para definir una tupla 


def leer_puntos_csv(ruta_csv: str) -> List[Point]: #funcion que lle los puntos de un archivo cvs
    puntos: List[Point] = [] #lista donde se guardan los puntos
    with open(ruta_csv, "r", encoding="utf-8") as f: #abre el archivo
        reader = csv.DictReader(f) #lee el archivo
        for row in reader: #recorre la fila
            x = float(row["x"]) #convierte las columnas a flotande
            y = float(row["y"]) #convierte las columnas a flotante
            puntos.append((x, y)) #agrega los puntos
    return puntos


def punto_mas_izquierdo(puntos: List[Point]) -> int: #funcion para los puntos 
    idx = 0 #comienza el lado izquierdo en 0
    for i in range(1, len(puntos)): #recorre todos los puntos
        if puntos[i][0] < puntos[idx][0] or (
            puntos[i][0] == puntos[idx][0] and puntos[i][1] < puntos[idx][1]
        ):
            idx = i
    return idx


def orientacion(a: Point, b: Point, c: Point) -> float:
    cross = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return cross


def distancia2(a: Point, b: Point) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


def convex_hull(puntos: List[Point]) -> List[Point]:

    if len(puntos) < 3:
        return puntos[:]

    hull: List[Point] = []
    start_idx = punto_mas_izquierdo(puntos)
    p_idx = start_idx

    while True: 
        hull.append(puntos[p_idx])
        q_idx = (p_idx + 1) % len(puntos)

        for r_idx in range(len(puntos)):
            if r_idx == p_idx:
                continue

            o = orientacion(puntos[p_idx], puntos[q_idx], puntos[r_idx])

            if o < 0:
                q_idx = r_idx

            elif o == 0:
                if distancia2(puntos[p_idx], puntos[r_idx]) > distancia2(
                    puntos[p_idx], puntos[q_idx]
                ):
                    q_idx = r_idx

        p_idx = q_idx
        if p_idx == start_idx:
            break

    return hull


def dibujar(puntos: List[Point], hull: List[Point], ax):
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]

    ax.clear()
    ax.scatter(xs, ys)

    if len(hull) >= 2:
        hx = [p[0] for p in hull] + [hull[0][0]]
        hy = [p[1] for p in hull] + [hull[0][1]]
        ax.plot(hx, hy)

    ax.set_title("Convex Hull")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

def main():

    root = tk.Tk()
    root.title("Convex Hull")

    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def cargar_archivo():
        ruta = filedialog.askopenfilename(
            filetypes=[("Archivos CSV", "*.csv")]
        )
        if not ruta:
            return

        puntos = leer_puntos_csv(ruta)
        hull = convex_hull(puntos)
        dibujar(puntos, hull, ax)
        canvas.draw()

    boton = tk.Button(root, text="Seleccionar archivo CSV", command=cargar_archivo)
    boton.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
