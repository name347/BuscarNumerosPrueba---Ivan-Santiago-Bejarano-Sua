""" Adivinar un número entre 1 y 100 """

import random
import tkinter as tk
from tkinter import messagebox

number = random.randint(1, 100)
intentos = 10
intento_actual = 1

ventana = tk.Tk()
ventana.title("Juego: Adivina el Número (Visual)")
ventana.geometry("325x200") 

def comprobar_intento():
    global intentos, intento_actual 
    
    try:
        adivina = int(entrada_numero.get())
    except ValueError:
        messagebox.showwarning("Ingresaste un numero no valido")
        return

    if adivina == number:
        messagebox.showinfo("Adivinaste el numero secreto")
        ventana.destroy() 
        return
    
    if adivina < number:
        texto_pista.config(text=f"El numero secreto es MAYOR a: {adivina}")
    else:
        texto_pista.config(text=f"El numero secreto es MENOR a: {adivina}")
        
    intentos -= 1
    intento_actual += 1
    
    texto_intentos.config(text=f"Te quedan {intentos} intentos.")
    texto_titulo.config(text=f"Intento Número {intento_actual}")
    entrada_numero.delete(0, tk.END) 

    if intentos == 0:
        messagebox.showerror(f"Se acabaron tus intentos. El numero era: {number}")
        ventana.destroy() 

texto_titulo = tk.Label(ventana, text=f"Intento Número {intento_actual}", font=("Arial", 10))
texto_titulo.pack(pady=10)

texto_instruccion = tk.Label(ventana, text="Adivina numero entre 1 y 100 con solo 10 intentos", font=("Arial", 10))
texto_instruccion.pack(pady=5)

entrada_numero = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada_numero.pack(pady=10)

boton_adivinar = tk.Button(ventana, text="Ingresa número", command=comprobar_intento, bg="#FFFFFF", fg="black", font=("Arial", 10))
boton_adivinar.pack(pady=5)

texto_pista = tk.Label(ventana, text="", font=("Arial", 10), fg="black")
texto_pista.pack(pady=10)

texto_intentos = tk.Label(ventana, text=f"Te quedan {intentos} intentos.", font=("Arial", 10))
texto_intentos.pack(pady=5)

ventana.mainloop()