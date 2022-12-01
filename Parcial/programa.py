import tkinter as tk
from tkinter import Tk, Label
from tkinter import ttk
import random

COLORS = [
    "red",
    "blue",
    "yellow",
    "orange",
    "purple",
    "green",
    "white",
    "gold",
    "silver",
]

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Matríz")
ventana.configure(background="white")


def crear_matriz(entry_numero):
    filas = entry_numero
    columnas = entry_numero
    for fila in range(filas):
        ventana.rowconfigure(fila, weight=1)
        for columna in range(columnas):
            etiqueta = Label(canvas, text=random.randint(0, 9), bg="blue")
            etiqueta.configure(font=("Arial", 25))
            etiqueta.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
            ventana.columnconfigure(columna, weight=1)


def hallar_numero():
    filas = int(entry_numero.get())
    columnas = int(entry_numero.get())
    for numero in range(9):
        color = random.sample(COLORS, 1)
        for fila in range(filas):
            for columna in range(columnas):
                if (
                    canvas.grid_slaves(row=fila, column=columna)[0].cget("text")
                    == numero
                ):
                    canvas.grid_slaves(row=fila, column=columna)[0].configure(
                        background=color
                    )


frame = tk.Frame(ventana, background="white")
frame.pack()
canvas = tk.Canvas(frame, background="white")
canvas.pack()
entry_numero = ttk.Entry(justify=tk.RIGHT)
entry_numero.pack()
boton_numero = tk.Button(
    text="Crear", command=lambda: crear_matriz(int(entry_numero.get()))
)
boton_numero.pack()
boton_hallar_numero = tk.Button(text="Hallar", command=hallar_numero)
boton_hallar_numero.pack()
ventana.mainloop()
