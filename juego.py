from abc import abstractmethod


class Personaje:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.__vida = vida
        self.nivel = nivel  

    def Recibir_daño(self, cantidad):
       if cantidad > 0:
            self.__vida -= cantidad
            print(f"{self.nombre} ha recibido {cantidad} de daño."
                f"Vida restante: {self.__vida}")
            
            if  self.__vida <= 0:
                self.__vida = 0
                print(f"{self.nombre} ha caido en combate.")
 
            else:
                print(f"{self.nombre} esquivo.")
            return self.__vida > 0

@abstractmethod
    def atacar(self):   

    def get_vida(self):
        return self.__vida
    
class Guerrero(Personaje):
    def __init__(self, nombre, vida, nivel, fuerza):
        super().__init__(nombre, vida, nivel)
        self.fuerza = fuerza

    def atacar(self):
        Daño = self.nivel+self.fuerza
        print(f"{self.nombre} ataca con fuerza {Daño}.")
        print(f"{self.nombre} realiza un ataque poderoso con fuerza {Daño}.")

class Mago(Personaje):
    def __init__(self, nombre, vida, nivel, mana):
        super().__init__(nombre, vida, nivel)
        self.mana = mana
    def atacar(self):
        Daño = self.nivel+self.mana
        return Daño
    def curar(self):
        if self.mana >= 10:
           curar = 30
           self.mana -= 10
           return curar
        else:
            return 0
        
