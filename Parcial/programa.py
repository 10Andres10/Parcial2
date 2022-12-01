import tkinter as tk
from tkinter import Tk, Label
from tkinter import ttk
import random

filas = 3
columnas = 3

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Matríz")

numero = ttk.Entry(justify=tk.RIGHT)
# numero.pack()

for fila in range(filas):
    ventana.rowconfigure(fila, weight=1)
    for columna in range(columnas):
        etiqueta = Label(text=random.randint(0, 9), bg="cadetblue1",font=1)
        etiqueta.configure(font=99)
        etiqueta.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
        ventana.columnconfigure(columna, weight=1)


def encontrar_numero():
    for i in range(0, 9):
        for fila in range(filas):
            for columna in range(columnas):
                if etiqueta.cget("text") == i:
                    ventana.configure(bg="cadetblue3")


encontrar_numero()

ventana.mainloop()
