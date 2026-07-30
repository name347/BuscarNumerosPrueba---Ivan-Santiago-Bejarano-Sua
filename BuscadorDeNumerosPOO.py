import random

class AdivinadorDeNumeros:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.intentos = 10
        self.intento_actual = 1

    def jugar(self):
        print("Adivinador de Numeros")
        print("Adivina un numero entre 1 y 100 con 10 intentos")

        while self.intentos > 0:
            print("")
            print("Intento Numero " + str(self.intento_actual))
            print("Te quedan " + str(self.intentos) + " intentos")
            
            adivina = self.pedir_numero()
            if adivina is None:
                continue

            if adivina == self.number:
                print("Adivinaste el numero secreto")
                return

            if adivina < self.number:
                print("El numero secreto es MAYOR a: " + str(adivina))
            else:
                print("El numero secreto es MENOR a: " + str(adivina))

            self.intentos -= 1
            self.intento_actual += 1

        print("Fin del juego")
        print("Se acabaron tus intentos. El numero era: " + str(self.number))

    def pedir_numero(self):
        try:
            entrada = input("Ingresa un numero: ")
            return int(entrada)
        except ValueError:
            print("Ingresaste un numero no valido")
            return None

if __name__ == "__main__":
    juego = AdivinadorDeNumeros()
    juego.jugar()