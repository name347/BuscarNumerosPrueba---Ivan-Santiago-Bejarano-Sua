import tkinter as tk
from tkinter import messagebox

class PedroResponde:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pedro Responde")
        self.ventana.geometry("400x250")
        
        self.frase_automatica = "Pedro por favor responde"
        self.respuesta_oculta = ""
        self.modo_truco = False
        self.indice_letra = 0
        
        self.crear_interfaz()

    def crear_interfaz(self):
        texto_titulo = tk.Label(self.ventana, text="El Oráculo Virtual", font=("Arial", 10))
        texto_titulo.pack(pady=6)

        tk.Label(self.ventana, text="Haz tu petición a Pedro:", font=("Arial", 10)).pack()
        self.entrada_peticion = tk.Entry(self.ventana, font=("Arial", 10))
        self.entrada_peticion.pack(pady=6)
        
        # Vinculación del evento de teclado al método de la clase
        self.entrada_peticion.bind("<Key>", self.detectar_tecla)

        tk.Label(self.ventana, text="Escribe tu pregunta:", font=("Arial", 10)).pack()
        self.entrada_pregunta = tk.Entry(self.ventana, font=("Arial", 10))
        self.entrada_pregunta.pack(pady=6)

        boton_preguntar = tk.Button(self.ventana, text="Haz tu pregunta", command=self.procesar_respuesta, bg="#FFFFFF", fg="Black")
        boton_preguntar.pack(pady=6)

        self.texto_resultado = tk.Label(self.ventana, text="Pedro está esperando...", font=("Arial", 10))
        self.texto_resultado.pack(pady=6)

    def detectar_tecla(self, event):
        if event.char == ".":
            self.modo_truco = not self.modo_truco
            if self.indice_letra < len(self.frase_automatica):
                self.entrada_peticion.insert(tk.END, self.frase_automatica[self.indice_letra])
                self.indice_letra += 1
            return "break" 

        if self.modo_truco:
            if event.keysym != "BackSpace": 
                self.respuesta_oculta += event.char

            if self.indice_letra < len(self.frase_automatica):
                self.entrada_peticion.insert(tk.END, self.frase_automatica[self.indice_letra])
                self.indice_letra += 1
            return "break" 

    def procesar_respuesta(self):
        pregunta = self.entrada_pregunta.get()
        peticion = self.entrada_peticion.get()
        
        if not peticion or not pregunta:
            messagebox.showwarning("Advertencia", "Debes rellenar ambos campos.")
            return
            
        if self.respuesta_oculta:
            self.texto_resultado.config(text=f"Pedro dice:\n{self.respuesta_oculta.strip().lower()}")
        else:
            self.texto_resultado.config(text="Pedro dice:\nNo tienes el suficiente respeto ni fe para conocer la respuesta.")

        # Reinicio de propiedades
        self.respuesta_oculta = ""
        self.modo_truco = False
        self.indice_letra = 0
        self.entrada_peticion.delete(0, tk.END)
        self.entrada_pregunta.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = PedroResponde(root)
    root.mainloop()