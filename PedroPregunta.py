""" Juego: Pedro Responde (Broma del Oráculo) """

import tkinter as tk
from tkinter import messagebox

frase_automatica = "Pedro por favor responde"
respuesta_oculta = ""
modo_truco = False
indice_letra = 0

ventana = tk.Tk()
ventana.title("Pedro Responde")
ventana.geometry("400x250")

def detectar_tecla(event):
    global modo_truco, respuesta_oculta, indice_letra
    
    if event.char == ".":
        modo_truco = not modo_truco
        entrada_peticion.insert(tk.END, frase_automatica[indice_letra])
        indice_letra += 1
        return "break" 

    if modo_truco:
        if event.keysym != "BackSpace": 
            respuesta_oculta += event.char

        if indice_letra < len(frase_automatica):
            entrada_peticion.insert(tk.END, frase_automatica[indice_letra])
            indice_letra += 1
        return "break" 

def procesar_respuesta():
    global respuesta_oculta, modo_truco, indice_letra
    
    pregunta = entrada_pregunta.get()
    
    if not entrada_peticion.get() or not pregunta:
        messagebox.showwarning("Advertencia", "Debes rellenar ambos campos.")
        return
    if respuesta_oculta:
        texto_resultado.config(text=f"Pedro dice:\n{respuesta_oculta.strip().lower()}")

    else:
        texto_resultado.config(text="Pedro dice:\nNo tienes el suficiente respeto ni fe para conocer la respuesta.")

    respuesta_oculta = ""
    modo_truco = False
    indice_letra = 0
    entrada_peticion.delete(0, tk.END)
    entrada_pregunta.delete(0, tk.END)

texto_titulo = tk.Label(ventana, text="El Oráculo Virtual", font=("Arial", 10))
texto_titulo.pack(pady=6)

tk.Label(ventana, text="Has tu pregunta a Pedro:", font=("Arial", 10)).pack()
entrada_peticion = tk.Entry(ventana, font=("Arial", 10))
entrada_peticion.pack(pady=6)
entrada_peticion.bind("<Key>", detectar_tecla)

tk.Label(ventana, text="Escribe tu pregunta", font=("Arial", 10)).pack()
entrada_pregunta = tk.Entry(ventana, font=("Arial", 10))
entrada_pregunta.pack(pady=6)

boton_preguntar = tk.Button(ventana, text="Has tu pregunta", command=procesar_respuesta, bg="#FFFFFF", fg="Black")
boton_preguntar.pack(pady=6)

texto_resultado = tk.Label(ventana, text="Pedro está esperando...", font=("Arial", 10))
texto_resultado.pack(pady=6)

texto_resultado.config(text=f"Pedro dice:\n{respuesta_oculta.capitalize()}")
texto_resultado.config(text=f"Pedro dice:\n{respuesta_oculta.lower()}")

ventana.mainloop()  