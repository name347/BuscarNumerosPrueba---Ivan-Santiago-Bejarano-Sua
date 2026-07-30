import random
import tkinter as tk
from tkinter import messagebox

class JuegoPiedraPapelTijera:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Piedra, Papel o Tijera")
        self.ventana.geometry("250x175")
        
        self.opciones = ["Piedra", "Papel", "Tijera"]
        self.puntos_jugador = 0
        self.puntos_pc = 0
        
        self.crear_interfaz()

    def crear_interfaz(self):
        texto_titulo = tk.Label(self.ventana, text="Piedra, Papel o Tijera", font=("Arial", 10))
        texto_titulo.pack(pady=5)

        texto_instruccion = tk.Label(self.ventana, text="Quien gane 3 rondas gana", font=("Arial", 10))
        texto_instruccion.pack(pady=5)

        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=5)

        # Nota el uso de lambda apuntando a self.jugar
        boton_piedra = tk.Button(marco_botones, text="Piedra", command=lambda: self.jugar("Piedra"), width=5)
        boton_piedra.pack(side="left", padx=3)

        boton_papel = tk.Button(marco_botones, text="Papel", command=lambda: self.jugar("Papel"), width=5)
        boton_papel.pack(side="left", padx=3)

        boton_tijera = tk.Button(marco_botones, text="Tijera", command=lambda: self.jugar("Tijera"), width=5)
        boton_tijera.pack(side="left", padx=3)

        self.texto_resultado = tk.Label(self.ventana, text="¿Quién ganará?", font=("Arial", 10), fg="black")
        self.texto_resultado.pack(pady=5)

        self.texto_marcador = tk.Label(self.ventana, text="Usuario: 0 / Contrincante: 0", font=("Arial", 10))
        self.texto_marcador.pack(pady=5)

    def jugar(self, eleccion_jugador):
        eleccion_pc = random.choice(self.opciones)
        
        if eleccion_jugador == eleccion_pc:
            resultado = "Empatas esta ronda"
        elif (eleccion_jugador == "Piedra" and eleccion_pc == "Tijera") or \
             (eleccion_jugador == "Papel" and eleccion_pc == "Piedra") or \
             (eleccion_jugador == "Tijera" and eleccion_pc == "Papel"):
            resultado = "Ganas esta ronda"
            self.puntos_jugador += 1
        else:
            resultado = "Pierdes esta ronda"
            self.puntos_pc += 1

        self.texto_resultado.config(text=f"Usuario: {eleccion_jugador}  vs  Contrincante: {eleccion_pc}\n{resultado}")
        self.texto_marcador.config(text=f"Usuario: {self.puntos_jugador} Contrincante: {self.puntos_pc}")

        if self.puntos_jugador == 3:
            messagebox.showinfo("Resultado", "Tú Ganaste")
            self.ventana.destroy()
        elif self.puntos_pc == 3:
            messagebox.showerror("Resultado", "Tú Perdiste")
            self.ventana.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoPiedraPapelTijera(root)
    root.mainloop()