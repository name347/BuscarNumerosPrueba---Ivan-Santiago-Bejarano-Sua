""" Adivinar un número entre 1 y 100 """

import random 
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Adivinador de Números")
ventana.geometry("300x250")

number = random.randint(1, 100)
intentos = 10
intento_actual = 1
numero_anterior = None  

print("Adivina numeros entre 1 y 100 con solo 10 intentos")
while intentos > 0:
    print(f"\nIntento Número {intento_actual}") 
    adivina = int(input("Introduce un numero: ")) 
    
    if adivina == number:
        print(" Adivinaste el numero secreto")
        break
    
    if adivina < number:
        print(f"El numero secreto es MAYOR a: {adivina}")
    else:
        print(f"El numero secreto es MENOR a: {adivina}")
        
    numero_anterior = adivina
    
    intentos -= 1
    intento_actual += 1
    print(f"Te quedan {intentos} intentos.")

if intentos == 0:
    print("\nSe acabaron tus intentos. El numero era:", number)