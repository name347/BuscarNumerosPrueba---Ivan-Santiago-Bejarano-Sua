class Libro: 
    def __init__(self, titulo, categoria, autor): 
        self._titulo = titulo 
        self._categoria = categoria 
        self._autor = autor 
        self.p = False 
        
    def _prestar(self): 
        if not self.p: 
            self.p = True 
            return f"El libro {self._titulo} ha sido prestado" 
        else: 
            return f"El libro {self._titulo} ya estaba prestado" 
            
    def devolver(self): 
        self.p = False 
        
    def esta_prestado(self): 
        return not self.p

L1 = Libro("100 años de soledad", "Aventura", "Gabriel") 
L2 = Libro("Anita", "Comedia", "Nicoll") 

L1._prestar() 
L1.devolver() 
L2._prestar() 

class Biblioteca: 
    def __init__(self, nombre): 
        self.nombre = nombre
        self.lista_de_libros = []
        
    def agregar_libro(self, libro): 
        self.lista_de_libros.append(libro) 
        print(f"{libro._titulo} agregado a la biblioteca") 
        
    def mostrar_libros(self): 
        pass