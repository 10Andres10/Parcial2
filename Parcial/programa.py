# Importo las librerias para llevar asi la parte  de la matriz 
from tkinter import *
import random
 
# los numeros se agragan para asi poder poner el numero de filas y de colunas que tiene cada matriz 
filas = 3
columnas = 3

#---------------------------
# Funciones operaciones
# --------------------------

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Matríz")

#num = [0,1,2,3,4,5,6,7,8,9]

#for i in range(1):
#   print(random.choice(num))

for fila in range(filas):
   ventana.rowconfigure(fila, weight=1)
   for columna in range(columnas):
      etiqueta = Label(text="1"+str(fila)+str(columna), bg="cadetblue1")
      etiqueta.grid(row=fila,column=columna, padx=2, pady=2, sticky="nsew")
      #etiqueta.grid(row=fila,column=columna, padx=2, pady=2)
      ventana.columnconfigure(columna, weight=1)

ventana.mainloop()

