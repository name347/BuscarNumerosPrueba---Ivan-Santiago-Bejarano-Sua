""" Juego de Piedra, Papel y Tijeras """

import random
import tkinter as tk
from tkinter import messagebox

opciones = ["Piedra", "Papel", "Tijera"]

puntos_jugador = 0
puntos_pc = 0

ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("250x175")

def jugar(eleccion_jugador):
    global puntos_jugador, puntos_pc
    
    eleccion_pc = random.choice(opciones)
    
    if eleccion_jugador == eleccion_pc:
        resultado = "Empatas esta ronda"
    elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
        resultado = "Ganas esta ronda"
        puntos_jugador += 1
    else:
        resultado = "Pierdes esta ronda"
        puntos_pc += 1

    texto_resultado.config(text=f"Usuario: {eleccion_jugador}  vs  Contrincante: {eleccion_pc}\n{resultado}")
    texto_marcador.config(text=f"Usuario: {puntos_jugador} Contrincante: {puntos_pc}")

    if puntos_jugador == 3:
        messagebox.showinfo("Tu Ganaste")
        ventana.destroy()
    elif puntos_pc == 3:
        messagebox.showerror("Tu Perdiste")
        ventana.destroy()

texto_titulo = tk.Label(ventana, text="Piedra, Papel o Tijera", font=("Arial", 10))
texto_titulo.pack(pady=5)

texto_instruccion = tk.Label(ventana, text="Quien gane 3 rondas gana", font=("Arial", 10))
texto_instruccion.pack(pady=5)

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)

boton_piedra = tk.Button(marco_botones, text="Piedra", command=lambda: jugar("Piedra"), width=5)
boton_piedra.pack(side="left", padx=3)

boton_papel = tk.Button(marco_botones, text="Papel", command=lambda: jugar("Papel"), width=5)
boton_papel.pack(side="left", padx=3)

boton_tijera = tk.Button(marco_botones, text="Tijera", command=lambda: jugar("Tijera"), width=5)
boton_tijera.pack(side="left", padx=3)

texto_resultado = tk.Label(ventana, text="¿Quién ganará?", font=("Arial", 10), fg="black")
texto_resultado.pack(pady=5)

texto_marcador = tk.Label(ventana, text="Usuario: 0 / Contrincante: 0", font=("Arial", 10))
texto_marcador.pack(pady=5)

ventana.mainloop()