# -*- coding: latin-1 -*-

import math
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter

def calcular_entropia(probabilidades):
    entropia = sum(p * math.log2(1 / p) for p in probabilidades if p > 0)
    return entropia

def calcular_redundancia(entropia, num_simbolos):
    entropia_maxima = math.log2(num_simbolos) if num_simbolos > 0 else 0
    redundancia = (entropia_maxima - entropia) / entropia_maxima if entropia_maxima > 0 else 0
    return redundancia

def procesar_archivo(archivo):
    with open(archivo, 'rb') as file:
        contenido = file.read()

    # Contar la frecuencia de cada byte en el archivo
    contador = Counter(contenido)
    
    # Calcular la probabilidad de cada símbolo
    total_simbolos = sum(contador.values())
    probabilidades = [freq / total_simbolos for freq in contador.values()]
    
    # Número de símbolos únicos
    num_simbolos = len(contador)

    # Calcular entropía y redundancia
    entropia = calcular_entropia(probabilidades)
    redundancia = calcular_redundancia(entropia, num_simbolos)

    return entropia, redundancia

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Todos los archivos", "*.*")])
    if archivo:
        try:
            entropia, redundancia = procesar_archivo(archivo)
            messagebox.showinfo("Resultados", f"Archivo: {archivo}\nEntropía: {entropia:.4f} bits/símbolo\nRedundancia: {redundancia:.4f}")
        except Exception as e:
            messagebox.showerror("Error", f"Error procesando el archivo: {e}")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Calculadora de Entropía y Redundancia")
    ventana.geometry("400x200")

    btn_abrir = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
    btn_abrir.pack(pady=50)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
